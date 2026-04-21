from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Genre, Game, Purchase, Profile, Review


# ── Plain Serializers ────────────────────────────────────────────────────────

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ReviewActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=['like', 'dislike'])


# ── Model Serializers ────────────────────────────────────────────────────────

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'slug']


class GameSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source='genre', write_only=True, required=False
    )
    # camelCase aliases — совместимость с Angular
    releaseDate = serializers.CharField(source='release_date', required=False)
    originalPrice = serializers.FloatField(
        source='original_price', required=False, allow_null=True
    )
    screenshots = serializers.JSONField(required=False, default=list)  # ← добавлено

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'price', 'originalPrice', 'discount',
            'description', 'image', 'rating',
            'genre', 'genre_id',
            'developer', 'releaseDate',
            'screenshots',   # ← добавлено
            'is_active',
        ]


class PurchaseSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(), source='game', write_only=True
    )
    purchasedAt = serializers.DateTimeField(source='purchased_at', read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'game', 'game_id', 'price', 'purchasedAt']
        read_only_fields = ['price', 'purchasedAt']


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    purchasedGames = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'bio', 'avatar', 'purchasedGames']

    def get_purchasedGames(self, obj):
        purchases = obj.user.purchases.select_related('game', 'game__genre')
        return PurchaseSerializer(purchases, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'username', 'game', 'rating', 'text', 'likes', 'dislikes', 'createdAt']
        read_only_fields = ['likes', 'dislikes', 'createdAt']
        extra_kwargs = {'game': {'write_only': True}}
