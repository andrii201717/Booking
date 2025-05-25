from enum import Enum

class RoomType(str, Enum):
    one_room_apartment = "1-кімнатна квартира (вітальня і спальня разом, з кухнею та ванною)"
    two_room_apartment = "2-кімнатна квартира (спальня та вітальня окремо)"
    three_room_apartment = "3-кімнатна квартира (спальня, дитяча або кабінет, вітальня)"
    shared_apartment = "Кімната у спільній квартирі (спільне житло з іншими)"
    granny_flat = "Окрема невелика квартира в межах приватного будинку"
    apartment = "Квартира в багатоквартирному будинку"
    single_family_house = "Будинок на одну родину"
    two_family_house = "Будинок на дві родини"
    townhouse = "Таунхаус (ряд будинків з’єднані стіною)"
    semi_detached_house = "Половина дуплексу (спарений будинок)"
    luxury_apartment = "Сучасна або елітна квартира з повним обладнанням"

    @classmethod
    def choices(cls):
        return [(member.name, member.value) for member in cls]