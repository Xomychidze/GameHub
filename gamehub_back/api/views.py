from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Game, Genre, Purchase, Profile, Review
from .serializers import (
    GameSerializer, GenreSerializer,
    RegisterSerializer, LoginSerializer,
    PurchaseSerializer, ProfileSerializer,
    ReviewSerializer, ReviewActionSerializer,
)


# AUTH

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request: Request) -> Response:
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'accessToken': str(refresh.access_token),
            'refreshToken': str(refresh),
            'user': {'id': user.id, 'username': user.username, 'email': user.email},
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request: Request) -> Response:
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'accessToken': str(refresh.access_token),
                'refreshToken': str(refresh),
                'user': {'id': user.id, 'username': user.username, 'email': user.email},
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request: Request) -> Response:
    try:
        token = RefreshToken(request.data.get('refreshToken'))
        token.blacklist()
    except Exception:
        pass
    return Response({'message': 'Logged out'})


# GAMES

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def games_list(request: Request) -> Response:
    if request.method == 'GET':
        qs = Game.objects.filter(is_active=True).select_related('genre')

        genre_id = request.query_params.get('genre')
        if genre_id:
            qs = qs.filter(genre_id=genre_id)

        search = request.query_params.get('search')
        if search:
            qs = qs.filter(title__icontains=search)

        sort = request.query_params.get('sort', 'title')
        allowed_sorts = {'title', '-title', 'price', '-price', 'rating', '-rating'}
        if sort in allowed_sorts:
            qs = qs.order_by(sort)

        return Response(GameSerializer(qs, many=True).data)

    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetailView(APIView):
    permission_classes = [AllowAny]

    def _get_game(self, pk):
        try:
            return Game.objects.select_related('genre').get(pk=pk)
        except Game.DoesNotExist:
            return None

    def get(self, request, pk):
        game = self._get_game(pk)
        if not game:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(GameSerializer(game).data)

    def put(self, request, pk):
        game = self._get_game(pk)
        if not game:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GameSerializer(game, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        game = self._get_game(pk)
        if not game:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GENRES
class GenreListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(GenreSerializer(Genre.objects.all(), many=True).data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(GenreSerializer(genre).data)


# PURCHASES

class PurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        purchases = Purchase.objects.filter(user=request.user).select_related('game', 'game__genre')
        return Response(PurchaseSerializer(purchases, many=True).data)

    def post(self, request):
        # Check if already purchased
        game_id = request.data.get('game_id')
        if Purchase.objects.filter(user=request.user, game_id=game_id).exists():
            return Response({'error': 'Already purchased'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            game = serializer.validated_data['game']
            serializer.save(user=request.user, price=game.price)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            purchase = Purchase.objects.select_related('game', 'game__genre').get(pk=pk, user=request.user)
        except Purchase.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(PurchaseSerializer(purchase).data)

    def delete(self, request, pk):
        try:
            purchase = Purchase.objects.get(pk=pk, user=request.user)
        except Purchase.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PROFILE

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        return Response(ProfileSerializer(profile).data)

    def put(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# REVIEWS
class ReviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, game_id):
        reviews = Review.objects.filter(game_id=game_id).select_related('user')
        return Response(ReviewSerializer(reviews, many=True).data)

    def post(self, request, game_id):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        if Review.objects.filter(user=request.user, game_id=game_id).exists():
            return Response({'error': 'Already reviewed'}, status=status.HTTP_400_BAD_REQUEST)
        data = {**request.data, 'game': game_id}
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_action(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewActionSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.validated_data['action'] == 'like':
            review.likes += 1
        else:
            review.dislikes += 1
        review.save()
        return Response(ReviewSerializer(review).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
