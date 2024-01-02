from enum import Enum, auto

class ChoLevel(Enum):
    is_low_cho = auto()
    is_normal_cho = auto()
    is_high_cho = auto()

@staticmethod
def calculate_cho_level(cho, kcal):
    cho_kcal =  cho * 4
    cho_percentage = cho_kcal / kcal * 100

    if cho_percentage < 55:
        return ChoLevel.is_low_cho.name
    elif cho_percentage <= 75:
        return ChoLevel.is_normal_cho.name
    else:
        return ChoLevel.is_high_cho.name
