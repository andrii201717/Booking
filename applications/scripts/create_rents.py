# import os
# import django
# import random
# from datetime import timedelta, date
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Booking.settings")
# django.setup()
#
# from applications.rentals.models import Rent
# from applications.users.models import User
# from applications.rooms.models import Room
# from applications.rentals.choices.rental_status import RentStatus
#
#
# def create_rents(n=5):
#     lessees = User.objects.filter(role="GUEST")
#     room_ids = [2, 3, 4, 5, 6]  # заміни на свої існуючі ID квартир
#     rooms = Room.objects.filter(id__in=room_ids, is_deleted=False)
#
#     if not lessees.exists() or not rooms.exists():
#         print("❌ Не знайдено орендарів або вказаних квартир.")
#         return
#
#     for _ in range(n):
#         lessee = random.choice(lessees)
#         room = random.choice(rooms)
#
#         start_date = date.today() + timedelta(days=random.randint(1, 30))
#         end_date = start_date + timedelta(days=random.randint(3, 14))
#
#         rent = Rent.objects.create(
#             lessee=lessee,
#             rent=room,
#             start_date=start_date,
#             end_date=end_date,
#             status=random.choice([status.name for status in RentStatus])
#         )
#
#         print(f"✅ Створено Rent: {rent}")
#
# if __name__ == "__main__":
#     create_rents()