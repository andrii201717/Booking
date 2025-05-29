# import os
# import sys
# import django
#
# # Додаємо до шляху корінь проєкту
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# sys.path.append(BASE_DIR)
#
# # Ініціалізація Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Booking.settings')
# django.setup()
#
# from django.utils import timezone
# from applications.rooms.models.locations import Address
# from applications.rooms.models.room import Room
# from applications.users.models import User
# from applications.rooms.choices.room_type import RoomType
#
#
# def run():
#     print("🚀 Starting to seed addresses and rooms...")
#
#     # Вибираємо перших 5 користувачів з роллю HOST
#     users = list(User.objects.filter(role='HOST')[:5])
#
#     if len(users) < 5:
#         print(f"⚠️ Знайдено лише {len(users)} користувачів з роллю HOST.")
#     if not users:
#         print("❌ Не знайдено користувачів з роллю HOST. Завершення.")
#         return
#
#     addresses_data = [
#         {'country': 'Germany', 'city': 'Berlin', 'street': 'Alexanderplatz', 'house_number': '7', 'apartment_number': '21', 'postal_code': '10178'},
#         {'country': 'Germany', 'city': 'Munich', 'street': 'Leopoldstraße', 'house_number': '45A', 'apartment_number': None, 'postal_code': '80802'},
#         {'country': 'Germany', 'city': 'Hamburg', 'street': 'Reeperbahn', 'house_number': '10', 'apartment_number': '5', 'postal_code': '20359'},
#         {'country': 'Germany', 'city': 'Frankfurt', 'street': 'Zeil', 'house_number': '112', 'apartment_number': None, 'postal_code': '60313'},
#         {'country': 'Germany', 'city': 'Cologne', 'street': 'Hohenzollernring', 'house_number': '23B', 'apartment_number': '14', 'postal_code': '50672'},
#     ]
#
#     # Обрізаємо, якщо користувачів менше 5
#     addresses_data = addresses_data[:len(users)]
#
#     addresses = []
#     for i, data in enumerate(addresses_data):
#         address = Address.objects.create(
#             **data,
#             owner=users[i]
#         )
#         addresses.append(address)
#
#     rooms_data = [
#         {
#             'title': 'Modern Apartment in Berlin',
#             'description': 'Cozy 2-room apartment in the center of Berlin.',
#             'price': 950.00,
#             'rooms_count': 2,
#             'room_type': RoomType.apartment.name,
#         },
#         {
#             'title': 'Spacious House in Munich',
#             'description': 'Family house with garden.',
#             'price': 1500.00,
#             'rooms_count': 4,
#             'room_type': RoomType.single_family_house.name,
#         },
#         {
#             'title': 'Studio near Hamburg nightlife',
#             'description': 'Small studio ideal for students.',
#             'price': 500.00,
#             'rooms_count': 1,
#             'room_type': RoomType.one_room_apartment.name,
#         },
#         {
#             'title': 'Flat in Frankfurt Zeil',
#             'description': 'Elegant 3-room flat with balcony.',
#             'price': 1200.00,
#             'rooms_count': 3,
#             'room_type': RoomType.apartment.name,
#         },
#         {
#             'title': 'Budget Room in Cologne',
#             'description': 'Simple room for rent in shared flat.',
#             'price': 350.00,
#             'rooms_count': 1,
#             'room_type': RoomType.one_room_apartment.name,
#         },
#     ]
#
#     rooms_data = rooms_data[:len(addresses)]
#
#     for i, data in enumerate(rooms_data):
#         Room.objects.create(
#             **data,
#             owner=addresses[i].owner,
#             address=addresses[i],
#             is_active=True,
#             created_at=timezone.now()
#         )
#
#     print("✅ Done seeding!")
#
#
# if __name__ == '__main__':
#     run()