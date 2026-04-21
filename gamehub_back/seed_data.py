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

# ── Superuser ────────────────────────────────────────────────────────────────
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gamehub.dev', 'admin1234')
    print('Superuser created: admin / admin1234')

# ── Genres ───────────────────────────────────────────────────────────────────
genres_data = [
    {'name': 'RPG',          'slug': 'rpg',          'description': 'Deep stories and character progression'},
    {'name': 'Metroidvania', 'slug': 'metroidvania', 'description': 'Action-exploration platformer'},
    {'name': 'Action',       'slug': 'action',       'description': 'Fast-paced combat and adventure'},
    {'name': 'Strategy',     'slug': 'strategy',     'description': 'Think before you act'},
    {'name': 'Shooter',      'slug': 'shooter',      'description': 'First and third-person shooting games'},
    {'name': 'Open World',   'slug': 'open-world',   'description': 'Open world action-adventure'},
    {'name': 'Sandbox',      'slug': 'sandbox',      'description': 'Sandbox and creative games'},
]

genres = {}
for g in genres_data:
    obj, created = Genre.objects.get_or_create(slug=g['slug'], defaults=g)
    genres[g['slug']] = obj
    if created:
        print(f"  Genre created: {g['name']}")

print(f'{Genre.objects.count()} genres ready.')

# ── Games ────────────────────────────────────────────────────────────────────
IMG = 'assets/image/'

games_data = [
    {
        'title': 'Hollow Knight: Silksong',
        'price': 2499,
        'description': 'Играй за Хорнет — охотницу и принцессу, исследующую новое огромное королевство насекомых. Каждый уголок мира полон тайн, смертоносных врагов и эпических боссов.',
        'image': IMG + 'silksong.jpg',
        'rating': 4.9,
        'genre': genres['metroidvania'],
        'developer': 'Team Cherry',
        'release_date': 'TBA',
        'screenshots': [IMG + 'silksong.jpg'],
    },
    {
        'title': 'Chivalry 2',
        'price': 3499,
        'original_price': 5999,
        'discount': 42,
        'description': 'Эпические средневековые сражения на 64 игрока. Мечи, топоры, осадные орудия и крики боли — всё это Chivalry 2.',
        'image': IMG + 'chivalry2.png',
        'rating': 4.1,
        'genre': genres['action'],
        'developer': 'Torn Banner Studios',
        'release_date': '8 июня 2021',
        'screenshots': [IMG + 'chivalry2.png'],
    },
    {
        'title': 'Mount & Blade II: Bannerlord',
        'price': 4999,
        'description': 'Строй армию, завоёвывай земли и стань правителем в огромном средневековом мире. Глубокая система политики, торговли и сражений.',
        'image': IMG + 'bannerlord.png',
        'rating': 4.3,
        'genre': genres['strategy'],
        'developer': 'TaleWorlds Entertainment',
        'release_date': '30 октября 2022',
        'screenshots': [IMG + 'bannerlord.png'],
    },
    {
        'title': 'Battlefield 1',
        'price': 2999,
        'original_price': 4999,
        'discount': 40,
        'description': 'Масштабные сражения Первой мировой войны — от окопов Европы до пустынь Аравии. Один из лучших шутеров серии по атмосфере.',
        'image': IMG + 'battlefield1.jpg',
        'rating': 4.4,
        'genre': genres['shooter'],
        'developer': 'DICE',
        'release_date': '21 октября 2016',
        'screenshots': [IMG + 'battlefield1.jpg'],
    },
    {
        'title': 'Heroes of Might & Magic III: HD Edition',
        'price': 1499,
        'description': 'Легендарная пошаговая стратегия в HD. Собирай армии, захватывай замки, побеждай героев. Классика, не стареющая десятилетиями.',
        'image': IMG + 'homm3.jpg',
        'rating': 4.8,
        'genre': genres['strategy'],
        'developer': 'New World Computing',
        'release_date': '28 февраля 1999',
        'screenshots': [IMG + 'homm3.jpg'],
    },
    {
        'title': 'Grand Theft Auto V',
        'price': 3999,
        'description': 'Три преступника, один мегаполис. Ограбления, погони и хаос в Лос-Сантосе. Онлайн-режим с сотнями часов контента.',
        'image': IMG + 'gtav.jpg',
        'rating': 4.7,
        'genre': genres['open-world'],
        'developer': 'Rockstar North',
        'release_date': '17 сентября 2013',
        'screenshots': [IMG + 'gtav.jpg'],
    },
    {
        'title': 'Frostpunk 2',
        'price': 5499,
        'description': 'Управляй последним городом человечества в постапокалиптическом ледяном мире. Каждое решение — моральная дилемма.',
        'image': IMG + 'frostpunk2.jpg',
        'rating': 4.5,
        'genre': genres['strategy'],
        'developer': '11 bit studios',
        'release_date': '20 сентября 2024',
        'screenshots': [IMG + 'frostpunk2.jpg'],
    },
    {
        'title': "Garry's Mod",
        'price': 999,
        'description': 'Физический конструктор без правил. Создавай, разрушай, играй во что хочешь. Тысячи мастерской-модов на любой вкус.',
        'image': IMG + 'garrysmod.png',
        'rating': 4.6,
        'genre': genres['sandbox'],
        'developer': 'Facepunch Studios',
        'release_date': '29 ноября 2006',
        'screenshots': [IMG + 'garrysmod.png'],
    },
    {
        'title': 'Squad',
        'price': 4499,
        'description': 'Реалистичный тактический шутер с упором на командную работу и коммуникацию. Без слаженной команды не выжить.',
        'image': IMG + 'squad.png',
        'rating': 4.2,
        'genre': genres['shooter'],
        'developer': 'Offworld Industries',
        'release_date': '23 сентября 2020',
        'screenshots': [IMG + 'squad.png'],
    },
    {
        'title': 'Europa Universalis IV',
        'price': 3999,
        'description': 'Управляй государством от 1444 до 1821 года. Дипломатия, торговля, войны и колонии. Бесконечная реиграбельность.',
        'image': IMG + 'eu4.png',
        'rating': 4.5,
        'genre': genres['strategy'],
        'developer': 'Paradox Development Studio',
        'release_date': '13 августа 2013',
        'screenshots': [IMG + 'eu4.png'],
    },
    {
        'title': 'The Elder Scrolls V: Skyrim Special Edition',
        'price': 2999,
        'original_price': 4999,
        'discount': 40,
        'description': 'Легендарная RPG в мире викингов и драконов. Тысячи часов приключений, квестов и модов.',
        'image': IMG + 'skyrim.png',
        'rating': 4.6,
        'genre': genres['rpg'],
        'developer': 'Bethesda Game Studios',
        'release_date': '28 октября 2016',
        'screenshots': [IMG + 'skyrim.png'],
    },
    {
        'title': 'Hollow Knight',
        'price': 1499,
        'description': 'Исследуй огромное подземное королевство насекомых. Мрачная атмосфера, сложные боссы и невероятный саундтрек.',
        'image': IMG + 'hollowknight.png',
        'rating': 4.9,
        'genre': genres['metroidvania'],
        'developer': 'Team Cherry',
        'release_date': '24 февраля 2017',
        'screenshots': [IMG + 'hollowknight.png'],
    },
    {
        'title': 'Clair Obscur: Expedition 33',
        'price': 6999,
        'description': 'Пошаговая RPG с кинематографическим нарративом и уникальной боевой системой. Французская студия, мировой уровень.',
        'image': IMG + 'expedition33.png',
        'rating': 4.8,
        'genre': genres['rpg'],
        'developer': 'Sandfall Interactive',
        'release_date': '24 апреля 2025',
        'screenshots': [IMG + 'expedition33.png'],
    },
    {
        'title': 'Kingdom Come: Deliverance Royal Edition',
        'price': 3999,
        'original_price': 6999,
        'discount': 43,
        'description': 'Реалистичная RPG в средневековой Богемии 1403 года. Без магии — только история, выживание и честный бой.',
        'image': IMG + 'kcd.jpg',
        'rating': 4.4,
        'genre': genres['rpg'],
        'developer': 'Warhorse Studios',
        'release_date': '13 февраля 2018',
        'screenshots': [IMG + 'kcd.jpg'],
    },
    {
        'title': 'The Witcher 3: Wild Hunt',
        'price': 2499,
        'original_price': 4999,
        'discount': 50,
        'description': 'Лучший ведьмак в лучшем из открытых миров. Гвинт, монстры и сложные выборы. Две масштабные DLC в комплекте.',
        'image': IMG + 'witcher3.png',
        'rating': 5.0,
        'genre': genres['rpg'],
        'developer': 'CD Projekt RED',
        'release_date': '19 мая 2015',
        'screenshots': [IMG + 'witcher3.png'],
    },
    {
        'title': 'Total War: Attila',
        'price': 3499,
        'description': 'Останови Аттилу или стань им. Падение Западной Римской империи в твоих руках.',
        'image': IMG + 'attila.png',
        'rating': 4.3,
        'genre': genres['strategy'],
        'developer': 'Creative Assembly',
        'release_date': '17 февраля 2015',
        'screenshots': [IMG + 'attila.png'],
    },
    {
        'title': "Baldur's Gate 3",
        'price': 7999,
        'description': 'Лучшая RPG десятилетия. D&D 5e в формате видеоигры — свобода выбора, глубокий нарратив и кооператив.',
        'image': IMG + 'bg3.png',
        'rating': 5.0,
        'genre': genres['rpg'],
        'developer': 'Larian Studios',
        'release_date': '3 августа 2023',
        'screenshots': [IMG + 'bg3.png'],
    },
    {
        'title': 'Cyberpunk 2077',
        'price': 2999,
        'original_price': 5999,
        'discount': 50,
        'description': 'Найт-Сити никогда не спит. Стань наёмником V и вступи в смертельную игру с корпорациями за выживание.',
        'image': IMG + 'cyberPunk2077.jpg',
        'rating': 4.2,
        'genre': genres['rpg'],
        'developer': 'CD Projekt RED',
        'release_date': '10 декабря 2020',
        'screenshots': [IMG + 'cyberPunk2077.jpg'],
    },
    {
        'title': 'Minecraft',
        'price': 10000,
        'description': 'Строй, выживай, исследуй. Мир без ограничений и правил — только твоя фантазия определяет пределы.',
        'image': IMG + 'minecraft.jpg',
        'rating': 5.0,
        'genre': genres['sandbox'],
        'developer': 'Mojang Studios',
        'release_date': '18 ноября 2011',
        'screenshots': [IMG + 'minecraft.jpg'],
    },
    {
        'title': 'The Witcher 4',
        'price': 10000,
        'description': 'Новая глава в мире Ведьмака. Новый герой, новые монстры, знакомая глубина выбора и последствий.',
        'image': IMG + 'witcher.jpeg',
        'rating': 4.0,
        'genre': genres['rpg'],
        'developer': 'CD Projekt RED',
        'release_date': 'TBA',
        'screenshots': [IMG + 'witcher.jpeg'],
    },
]

created_count = 0
for gd in games_data:
    _, created = Game.objects.get_or_create(title=gd['title'], defaults=gd)
    if created:
        created_count += 1

print(f'{created_count} new games added. Total: {Game.objects.count()} games ready.')
print('\nDone! Run: python manage.py runserver')
