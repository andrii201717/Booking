from enum import Enum


class RentStatus(str, Enum):
    PENDING = 'Очікується'
    CONFIRMED = 'Підтверджено'
    CANCELLED = 'Відміненно'
    DECLINED = 'Відмовлено'
    COMPLETED = 'Завершено'
    @classmethod
    def choices(cls):
        return [(member.name, member.value) for member in cls]