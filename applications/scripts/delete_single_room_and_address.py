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
# from applications.rooms.models.locations import Address
# from applications.rooms.models.room import Room
#
#
# def run():
#     print("🧹 Видалення одного запису з Room і Address...")
#
#     try:
#         room = Room.objects.get(id=1)  # Або інший ID, який точно треба видалити
#         print(f"🗑 Видаляємо кімнату: {room.title} (id={room.id})")
#         Room.objects.filter(id=1).delete()
#     except Room.DoesNotExist:
#         print("❌ Кімната з id=1 не знайдена.")
#
#     try:
#         address = Address.objects.get(id=1)  # Або інший ID
#         print(f"🗑 Видаляємо адресу: {address.city}, {address.street} {address.house_number} (id={address.id})")
#         address.delete()
#     except Address.DoesNotExist:
#         print("❌ Адреса з id=1 не знайдена.")
#
#     print("✅ Завершено!")
#
#
# if __name__ == '__main__':
#     run()