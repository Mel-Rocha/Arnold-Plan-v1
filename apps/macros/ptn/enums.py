from enum import Enum, auto

class PtnLevel(Enum):
    is_low_ptn = auto()
    is_normal_ptn = auto()
    is_high_ptn = auto()

@staticmethod
def calculate_ptn_level(ptn, kcal):
    ptn_kcal = ptn * 4
    ptn_percentage = ptn_kcal / kcal * 100

    if ptn_percentage < 10:
        return PtnLevel.is_low_ptn.name
    elif ptn_percentage <= 15:
        return PtnLevel.is_normal_ptn.name
    else:
        return PtnLevel.is_high_ptn.name
