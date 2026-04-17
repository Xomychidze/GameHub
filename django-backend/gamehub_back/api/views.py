from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from http import HTTPMethod, HTTPStatus
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Game, Genre, Purchase, Review
from .serializers import (
    GameSerializer, GenreSerializer,
    RegisterSerializer, LoginSerializer,
    PurchaseSerializer, ReviewSerializer,
)


# ─── AUTH — FBV ──────────────────────────────────────────────────────────────

@api_view([HTTPMethod.POST])
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
        }, status=HTTPStatus.CREATED)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view([HTTPMethod.POST])
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
        return Response({'error': 'Invalid credentials'}, status=HTTPStatus.UNAUTHORIZED)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view([HTTPMethod.POST])
@permission_classes([IsAuthenticated])
def logout_view(request: Request) -> Response:
    try:
        token = RefreshToken(request.data.get('refreshToken'))
        token.blacklist()
    except Exception:
        pass
    return Response({'message': 'Logged out'})


# ─── GAMES — FBV (list + create) ─────────────────────────────────────────────

@api_view([HTTPMethod.GET, HTTPMethod.POST])
@permission_classes([AllowAny])
def games_list(request: Request) -> Response:
    if request.method == HTTPMethod.GET:
        games = Game.objects.filter(is_active=True).select_related('genre')
        return Response(GameSerializer(games, many=True).data)

    # POST: только для авторизованных
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=HTTPStatus.UNAUTHORIZED)
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


# ─── GENRES — CBV ────────────────────────────────────────────────────────────

class GenreListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(GenreSerializer(Genre.objects.all(), many=True).data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():   # ← было is_valid (без скобок) — это баг!
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


# ─── GAME DETAIL — CBV (retrieve / update / delete) ──────────────────────────

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
            return Response({'error': 'Not found'}, status=HTTPStatus.NOT_FOUND)
        return Response(GameSerializer(game).data)

    def put(self, request, pk):
        game = self._get_game(pk)
        if not game:
            return Response({'error': 'Not found'}, status=HTTPStatus.NOT_FOUND)
        serializer = GameSerializer(game, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        game = self._get_game(pk)
        if not game:
            return Response({'error': 'Not found'}, status=HTTPStatus.NOT_FOUND)
        game.delete()
        return Response(status=HTTPStatus.NO_CONTENT)


# ─── PURCHASES — CBV ─────────────────────────────────────────────────────────

class PurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        purchases = Purchase.objects.filter(user=request.user).select_related('game', 'game__genre')
        return Response(PurchaseSerializer(purchases, many=True).data)

    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            game = serializer.validated_data['game']
            serializer.save(user=request.user, price=game.price)
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


# ─── REVIEWS — CBV ───────────────────────────────────────────────────────────

class ReviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, game_id):
        reviews = Review.objects.filter(game_id=game_id).select_related('user')
        return Response(ReviewSerializer(reviews, many=True).data)

    def post(self, request, game_id):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=HTTPStatus.UNAUTHORIZED)
        data = {**request.data, 'game': game_id}
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
