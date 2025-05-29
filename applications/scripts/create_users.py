# import os
# import django
#
# # Налаштування Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Booking.settings')  # змінити, якщо інша назва
# django.setup()
#
# from django.utils import timezone
# from applications.users.models.user import User
#
# users_data = [
#     {
#         "username": "user1_lex",
#         "email": "user1_lex@example.com",
#         "first_name": "Олександр",
#         "last_name": "Іванов",
#         "role": "GUEST",
#         "phone": "+380501234567",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1990-03-15",
#         "password": "password1"
#     },
#     {
#         "username": "user2_maria",
#         "email": "user2_maria@example.com",
#         "first_name": "Марія",
#         "last_name": "Петренко",
#         "role": "HOST",
#         "phone": "+380931112233",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1985-07-22",
#         "password": "password2"
#     },
#     {
#         "username": "user3_ivan",
#         "email": "user3_ivan@example.com",
#         "first_name": "Іван",
#         "last_name": "Сидоренко",
#         "role": "GUEST",
#         "phone": "+380671234567",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1993-01-10",
#         "password": "password3"
#     },
#     {
#         "username": "user4_anna",
#         "email": "user4_anna@example.com",
#         "first_name": "Анна",
#         "last_name": "Ковальчук",
#         "role": "HOST",
#         "phone": "+380951112233",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1997-12-01",
#         "password": "password4"
#     },
#     {
#         "username": "user5_serhiy",
#         "email": "user5_serhiy@example.com",
#         "first_name": "Сергій",
#         "last_name": "Литвин",
#         "role": "GUEST",
#         "phone": "+380991234567",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1988-06-30",
#         "password": "password5"
#     },
#     {
#         "username": "user6_olga",
#         "email": "user6_olga@example.com",
#         "first_name": "Ольга",
#         "last_name": "Романенко",
#         "role": "HOST",
#         "phone": "+380981122334",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1995-09-18",
#         "password": "password6"
#     },
#     {
#         "username": "user7_pavel",
#         "email": "user7_pavel@example.com",
#         "first_name": "Павло",
#         "last_name": "Захаренко",
#         "role": "GUEST",
#         "phone": "+380631234567",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1992-02-11",
#         "password": "password7"
#     },
#     {
#         "username": "user8_tetyana",
#         "email": "user8_tetyana@example.com",
#         "first_name": "Тетяна",
#         "last_name": "Мельник",
#         "role": "HOST",
#         "phone": "+380971234567",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1987-04-07",
#         "password": "password8"
#     },
#     {
#         "username": "user9_dmytro",
#         "email": "user9_dmytro@example.com",
#         "first_name": "Дмитро",
#         "last_name": "Шевченко",
#         "role": "GUEST",
#         "phone": "+380661234567",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1991-11-25",
#         "password": "password9"
#     },
#     {
#         "username": "user10_iryna",
#         "email": "user10_iryna@example.com",
#         "first_name": "Ірина",
#         "last_name": "Ткаченко",
#         "role": "HOST",
#         "phone": "+380941234567",
#         "is_staff": False,
#         "is_active": True,
#         "date_joined": timezone.now(),
#         "birth_day": "1996-08-13",
#         "password": "password10"
#     }
# ]
#
# for data in users_data:
#     password = data.pop("password")
#     user = User(**data)
#     user.set_password(password)
#     user.save()
#     print(f"✅ Користувач {user.username} створений з паролем '{password}'")