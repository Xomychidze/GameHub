"""
Запуск: python seed_data.py
Заполняет базу данных жанрами и играми (те же данные, что были в Angular mock).
Запускать из папки gamehub_back/ (рядом с manage.py).
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamehub_back.settings')
django.setup()

from api.models import Genre, Game

# ─── Жанры ───────────────────────────────────────────────────────────────────
genres_data = [
    {'name': 'RPG',          'slug': 'rpg',           'description': 'Role-playing games'},
    {'name': 'Metroidvania', 'slug': 'metroidvania',  'description': 'Action-exploration platformer'},
    {'name': 'Action',       'slug': 'action',        'description': 'Fast-paced action games'},
    {'name': 'Strategy',     'slug': 'strategy',      'description': 'Strategy games'},
    {'name': 'Shooter',      'slug': 'shooter',       'description': 'Shooter games'},
    {'name': 'Open World',   'slug': 'open-world',    'description': 'Open world games'},
    {'name': 'Sandbox',      'slug': 'sandbox',       'description': 'Sandbox games'},
]

genres = {}
for g in genres_data:
    obj, _ = Genre.objects.get_or_create(slug=g['slug'], defaults=g)
    genres[g['slug']] = obj
print(f"✓ Genres: {len(genres)}")

# ─── Игры ─────────────────────────────────────────────────────────────────────
games_data = [
    {
        'title': 'Hollow Knight: Silksong',
        'price': 2499, 'rating': 4.9,
        'image': 'assets/image/silksong.jpg',
        'genre': 'metroidvania',
        'developer': 'Team Cherry', 'release_date': 'TBA',
        'description': 'Играй за Хорнет — охотницу и принцессу, исследующую новое огромное королевство насекомых.',
    },
    {
        'title': 'Chivalry 2',
        'price': 3499, 'original_price': 5999, 'discount': 42, 'rating': 4.1,
        'image': 'assets/image/chivalry2.png',
        'genre': 'action',
        'developer': 'Torn Banner Studios', 'release_date': '8 июня 2021',
        'description': 'Эпические средневековые сражения на 64 игрока.',
    },
    {
        'title': 'Mount & Blade II: Bannerlord',
        'price': 4999, 'rating': 4.3,
        'image': 'assets/image/bannerlord.png',
        'genre': 'strategy',
        'developer': 'TaleWorlds Entertainment', 'release_date': '30 октября 2022',
        'description': 'Строй армию, завоёвывай земли и стань правителем в огромном средневековом мире.',
    },
    {
        'title': 'Battlefield 1',
        'price': 2999, 'original_price': 4999, 'discount': 40, 'rating': 4.4,
        'image': 'assets/image/battlefield1.jpg',
        'genre': 'shooter',
        'developer': 'DICE', 'release_date': '21 октября 2016',
        'description': 'Масштабные сражения Первой мировой войны.',
    },
    {
        'title': 'Heroes of Might & Magic III: HD Edition',
        'price': 1499, 'rating': 4.8,
        'image': 'assets/image/homm3.jpg',
        'genre': 'strategy',
        'developer': 'New World Computing', 'release_date': '28 февраля 1999',
        'description': 'Легендарная пошаговая стратегия в HD.',
    },
    {
        'title': 'Grand Theft Auto V',
        'price': 3999, 'rating': 4.7,
        'image': 'assets/image/gtav.jpg',
        'genre': 'open-world',
        'developer': 'Rockstar North', 'release_date': '17 сентября 2013',
        'description': 'Три преступника, один мегаполис. Ограбления, погони и хаос в Лос-Сантосе.',
    },
    {
        'title': 'Frostpunk 2',
        'price': 5499, 'rating': 4.5,
        'image': 'assets/image/frostpunk2.jpg',
        'genre': 'strategy',
        'developer': '11 bit studios', 'release_date': '20 сентября 2024',
        'description': 'Управляй последним городом человечества в постапокалиптическом ледяном мире.',
    },
    {
        'title': "Garry's Mod",
        'price': 999, 'rating': 4.6,
        'image': 'assets/image/garrysmod.png',
        'genre': 'sandbox',
        'developer': 'Facepunch Studios', 'release_date': '29 ноября 2006',
        'description': 'Физический конструктор без правил.',
    },
    {
        'title': 'Squad',
        'price': 4499, 'rating': 4.2,
        'image': 'assets/image/squad.png',
        'genre': 'shooter',
        'developer': 'Offworld Industries', 'release_date': '23 сентября 2020',
        'description': 'Реалистичный тактический шутер с упором на командную работу.',
    },
    {
        'title': 'Europa Universalis IV',
        'price': 3999, 'rating': 4.5,
        'image': 'assets/image/eu4.png',
        'genre': 'strategy',
        'developer': 'Paradox Development Studio', 'release_date': '13 августа 2013',
        'description': 'Управляй государством от 1444 до 1821 года.',
    },
    {
        'title': 'The Elder Scrolls V: Skyrim Special Edition',
        'price': 2999, 'original_price': 4999, 'discount': 40, 'rating': 4.6,
        'image': 'assets/image/skyrim.png',
        'genre': 'rpg',
        'developer': 'Bethesda Game Studios', 'release_date': '28 октября 2016',
        'description': 'Легендарная RPG в мире викингов и драконов.',
    },
    {
        'title': 'Hollow Knight',
        'price': 1499, 'rating': 4.9,
        'image': 'assets/image/hollowknight.png',
        'genre': 'metroidvania',
        'developer': 'Team Cherry', 'release_date': '24 февраля 2017',
        'description': 'Исследуй огромное подземное королевство насекомых.',
    },
    {
        'title': 'Clair Obscur: Expedition 33',
        'price': 6999, 'rating': 4.8,
        'image': 'assets/image/expedition33.png',
        'genre': 'rpg',
        'developer': 'Sandfall Interactive', 'release_date': '24 апреля 2025',
        'description': 'Пошаговая RPG с кинематографическим нарративом.',
    },
    {
        'title': 'Kingdom Come: Deliverance Royal Edition',
        'price': 3999, 'original_price': 6999, 'discount': 43, 'rating': 4.4,
        'image': 'assets/image/kcd.jpg',
        'genre': 'rpg',
        'developer': 'Warhorse Studios', 'release_date': '13 февраля 2018',
        'description': 'Реалистичная RPG в средневековой Богемии 1403 года.',
    },
    {
        'title': 'The Witcher 3: Wild Hunt',
        'price': 2499, 'original_price': 4999, 'discount': 50, 'rating': 5.0,
        'image': 'assets/image/witcher3.png',
        'genre': 'rpg',
        'developer': 'CD Projekt RED', 'release_date': '19 мая 2015',
        'description': 'Лучший ведьмак в лучшем из открытых миров.',
    },
    {
        'title': "Baldur's Gate 3",
        'price': 7999, 'rating': 5.0,
        'image': 'assets/image/bg3.png',
        'genre': 'rpg',
        'developer': 'Larian Studios', 'release_date': '3 августа 2023',
        'description': 'Лучшая RPG десятилетия. D&D 5e в формате видеоигры.',
    },
    {
        'title': 'Cyberpunk 2077',
        'price': 2999, 'original_price': 5999, 'discount': 50, 'rating': 4.2,
        'image': 'assets/image/cyberPunk2077.jpg',
        'genre': 'rpg',
        'developer': 'CD Projekt RED', 'release_date': '10 декабря 2020',
        'description': 'Найт-Сити никогда не спит. Стань наёмником V.',
    },
    {
        'title': 'Minecraft',
        'price': 10000, 'rating': 5.0,
        'image': 'assets/image/minecraft.jpg',
        'genre': 'sandbox',
        'developer': 'Mojang Studios', 'release_date': '18 ноября 2011',
        'description': 'Строй, выживай, исследуй. Мир без ограничений.',
    },
    {
        'title': 'The Witcher 4',
        'price': 10000, 'rating': 4.0,
        'image': 'assets/image/witcher.jpeg',
        'genre': 'rpg',
        'developer': 'CD Projekt RED', 'release_date': 'TBA',
        'description': 'Новая глава в мире Ведьмака. Новый герой, новые монстры.',
    },
    {
        'title': 'Total War: Attila',
        'price': 3499, 'rating': 4.3,
        'image': 'assets/image/attila.png',
        'genre': 'strategy',
        'developer': 'Creative Assembly', 'release_date': '17 февраля 2015',
        'description': 'Останови Аттилу или стань им.',
    },
]

created = 0
for g in games_data:
    genre_slug = g.pop('genre')
    g['genre'] = genres[genre_slug]
    g.setdefault('original_price', None)
    g.setdefault('discount', None)
    g.setdefault('is_active', True)
    _, new = Game.objects.get_or_create(title=g['title'], defaults=g)
    if new:
        created += 1

print(f"✓ Games created: {created} (skipped existing)")
print("Done! Run the server: python manage.py runserver")
