"""
Run with: python seed_data.py
(from inside gamehub_back/ directory, with venv active)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamehub_back.settings')
django.setup()

from api.models import Genre, Game
from django.contrib.auth.models import User

# ── Superuser ─────────────────────────────────────────────────────────────────
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gamehub.dev', 'admin1234')
    print('Superuser created: admin / admin1234')

# ── Genres ────────────────────────────────────────────────────────────────────
genres_data = [
    {'name': 'Action',    'slug': 'action',    'description': 'Fast-paced combat and adventure'},
    {'name': 'RPG',       'slug': 'rpg',       'description': 'Deep stories and character progression'},
    {'name': 'Strategy',  'slug': 'strategy',  'description': 'Think before you act'},
    {'name': 'Shooter',   'slug': 'shooter',   'description': 'First and third-person shooting games'},
    {'name': 'Historical','slug': 'historical','description': 'Battles and empires across the ages'},
]
genres = {}
for g in genres_data:
    obj, _ = Genre.objects.get_or_create(slug=g['slug'], defaults=g)
    genres[g['slug']] = obj
print(f'{Genre.objects.count()} genres ready.')

# ── Games ─────────────────────────────────────────────────────────────────────
IMAGE_BASE = '/assets/image/'
games_data = [
    {
        'title': 'Baldur\'s Gate 3',
        'price': 5499, 'original_price': 6999, 'discount': 21,
        'description': 'Award-winning RPG with unprecedented choices and consequences set in the D&D universe.',
        'image': IMAGE_BASE + 'bg3.png', 'rating': 4.9,
        'genre': genres['rpg'], 'developer': 'Larian Studios', 'release_date': 'Aug 3, 2023',
    },
    {
        'title': 'Battlefield 1',
        'price': 1999, 'original_price': 3499, 'discount': 43,
        'description': 'Experience the dawn of all-out war in the brutal first world war setting.',
        'image': IMAGE_BASE + 'battlefield1.jpg', 'rating': 4.5,
        'genre': genres['shooter'], 'developer': 'DICE', 'release_date': 'Oct 21, 2016',
    },
    {
        'title': 'Chivalry 2',
        'price': 1299, 'original_price': 2499, 'discount': 48,
        'description': 'Epic medieval multiplayer slasher with 64-player battles and limb-cutting combat.',
        'image': IMAGE_BASE + 'chivalry2.png', 'rating': 4.2,
        'genre': genres['action'], 'developer': 'Torn Banner Studios', 'release_date': 'Jun 8, 2021',
    },
    {
        'title': 'Total War: Attila',
        'price': 2499,
        'description': 'Lead the Huns or defend Rome in this brutal strategy epic set in the late Roman era.',
        'image': IMAGE_BASE + 'attila.png', 'rating': 4.3,
        'genre': genres['strategy'], 'developer': 'Creative Assembly', 'release_date': 'Feb 17, 2015',
    },
    {
        'title': 'Mount & Blade II: Bannerlord',
        'price': 3999, 'original_price': 4999, 'discount': 20,
        'description': 'Build your empire from nothing in a massive medieval sandbox with real-time battles.',
        'image': IMAGE_BASE + 'bannerlord.png', 'rating': 4.6,
        'genre': genres['historical'], 'developer': 'TaleWorlds', 'release_date': 'Oct 25, 2022',
    },
]

for gd in games_data:
    Game.objects.get_or_create(title=gd['title'], defaults=gd)

print(f'{Game.objects.count()} games ready.')
print('\nDone! Run: python manage.py runserver')
