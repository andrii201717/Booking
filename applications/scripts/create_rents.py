import os
import django
import random
from datetime import timedelta, date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Booking.settings")
django.setup()

from applications.rentals.models import Rent
from applications.users.models import User
from applications.rooms.models import Room
from applications.rentals.choices.rental_status import RentStatus


def create_rents():
    guests = list(User.objects.filter(role="GUEST"))
    rooms = list(Room.objects.filter(is_deleted=False))

    if not guests or not rooms:
        print("❌ Недостатньо гостей або квартир.")
        return

    # Перемішуємо списки
    random.shuffle(guests)
    random.shuffle(rooms)

    # Створюємо лише стільки записів, скільки дозволяє коротший список
    count = min(len(guests), len(rooms))

    for i in range(count):
        guest = guests[i]
        room = rooms[i]

        start_date = date.today() + timedelta(days=random.randint(1, 30))
        end_date = start_date + timedelta(days=random.randint(3, 14))

        rent = Rent.objects.create(
            guest=guest,
            room=room,
            start_date=start_date,
            end_date=end_date,
            status=random.choice([status.name for status in RentStatus])
        )

        print(f"✅ Створено Rent: {guest.email} -> Room {room.id}")


if __name__ == "__main__":
    create_rents()