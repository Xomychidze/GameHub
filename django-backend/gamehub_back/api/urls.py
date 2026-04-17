from django.urls import path
from . import views

urlpatterns = [
    # ── Auth ──────────────────────────────
    path('auth/register/', views.register_view,  name='auth-register'),
    path('auth/login/',    views.login_view,      name='auth-login'),
    path('auth/logout/',   views.logout_view,     name='auth-logout'),

    # ── Games ─────────────────────────────
    path('games/',         views.games_list,              name='games-list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game-detail'),

    # ── Genres ────────────────────────────
    path('genres/',        views.GenreListView.as_view(), name='genres-list'),

    # ── Purchases ─────────────────────────
    path('purchases/',     views.PurchaseView.as_view(),  name='purchases'),

    # ── Reviews ───────────────────────────
    path('games/<int:game_id>/reviews/', views.ReviewView.as_view(), name='game-reviews'),
]
