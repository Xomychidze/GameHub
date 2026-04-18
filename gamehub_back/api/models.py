from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    slug = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    original_price = models.FloatField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    image = models.CharField(max_length=500, blank=True, default='')
    rating = models.FloatField(default=0.0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='games')
    developer = models.CharField(max_length=200, blank=True, default='')
    release_date = models.CharField(max_length=100, blank=True, default='TBA')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='purchases')
    price = models.FloatField()
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} — {self.game.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default='')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField(default=5.0)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} → {self.game.title} ({self.rating}★)"
