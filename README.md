# GameHub — Full-Stack Game Store

A full-stack game store app: **Django REST API** backend + **Angular 19** frontend.

---

## 🚀 Quick Start

### Backend

```bash
cd gamehub_back
python -m venv venv
venv\Scripts\Activate.ps1     # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python seed_data.py               # seeds genres, games, admin user
python manage.py runserver        # → http://localhost:8000
```

**Admin:** `admin` / `admin1234`  
**API base:** `http://localhost:8000/api/`

### Frontend

```bash
# from the project root
npm install
ng serve                          # → http://localhost:4200
```

---

## 🔌 API Endpoints

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| POST | `/api/auth/register/` | — | Register new user |
| POST | `/api/auth/login/` | — | Login → returns JWT tokens |
| POST | `/api/auth/logout/` | ✅ | Blacklist refresh token |
| GET | `/api/games/` | — | List games (filter: `?genre=&search=&sort=`) |
| GET | `/api/games/:id/` | — | Game detail |
| GET | `/api/genres/` | — | All genres |
| GET | `/api/purchases/` | ✅ | My purchases |
| POST | `/api/purchases/` | ✅ | Buy a game `{ game_id }` |
| GET | `/api/profile/` | ✅ | My profile + library |
| PUT | `/api/profile/` | ✅ | Update bio |
| GET | `/api/games/:id/reviews/` | — | Game reviews |
| POST | `/api/games/:id/reviews/` | ✅ | Post review `{ rating, text }` |
| POST | `/api/reviews/:id/action/` | ✅ | Like/dislike `{ action: "like"\|"dislike" }` |

---

## 🏗 Project Structure

```
gamehub_back/         ← Django backend
├── api/
│   ├── models.py     ← Genre, Game, Purchase, Profile, Review
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── gamehub_back/
    └── settings.py

src/                  ← Angular 19 frontend
├── app/
│   ├── core/
│   │   ├── models/       ← TypeScript interfaces
│   │   ├── services/     ← AuthService, GameService, CartService, ProfileService
│   │   └── interceptors/ ← AuthInterceptor (JWT), AuthGuard
│   ├── features/
│   │   ├── store/        ← Game catalogue with genre filter + sort
│   │   ├── game-detail/  ← Game page with reviews + like/dislike
│   │   ├── cart/         ← Shopping cart + checkout
│   │   ├── library/      ← Purchased games
│   │   ├── profile/      ← User profile + bio editing
│   │   ├── login/
│   │   └── register/
│   └── shared/
│       ├── header/       ← Nav with auth state + cart badge
│       └── game-card/    ← Reusable card with add-to-cart
public/
└── assets/image/     ← Game cover images
```

---

## ✅ What was merged & fixed

### Backend
- ✅ JWT auth (`simplejwt`) with **register + login + logout** (token blacklist)
- ✅ Rich `Game` model: `title`, `image`, `rating`, `discount`, `developer`, `release_date`
- ✅ `Profile` model (bio, avatar) from `project_web`
- ✅ `Review` now has both `rating` (old) **and** `likes`/`dislikes` (new)
- ✅ Genre filtering, search and sorting on `/api/games/`
- ✅ `unique_together` on Purchase and Review (no duplicates)
- ✅ CORS + media files configured

### Frontend
- ✅ `AuthInterceptor` — JWT token attached to every request automatically
- ✅ `AuthGuard` — protects `/cart`, `/library`, `/profile`
- ✅ **Header** — shows username + logout when logged in, cart badge
- ✅ **Store** — genre filter pills + search + sort (all hit the API)
- ✅ **GameDetail** — reviews with star rating, like/dislike voting
- ✅ **Cart** — fully implemented with checkout via API
- ✅ **Library** — shows purchased games with search filter
- ✅ **Profile** — editable bio + recent purchases
- ✅ **GameCard** — discount badge, genre label, Add to Cart button
