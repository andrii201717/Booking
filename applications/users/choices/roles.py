from enum import Enum

class UserRoles(str, Enum):
    ADMIN = 'Адміністратор'
    HOST = 'Орендодавець'
    GUEST = 'Орендар'

    @classmethod
    def choices(cls):
        return [(member.name, member.value) for member in cls]