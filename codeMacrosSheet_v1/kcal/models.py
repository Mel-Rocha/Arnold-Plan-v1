from enum import Enum, auto

class KcalLevel(Enum):
    is_low_kcal = auto()
    is_normal_kcal = auto()
    is_high_kcal = auto()

def calculate_kcal(cho, ptn, fat):
    return (cho * 4) + (ptn * 4) + (fat * 9)

def calculate_kcal_level(kcal):
    if kcal < 1500:
        return KcalLevel.is_low_kcal.name
    elif kcal <= 2000:
        return KcalLevel.is_normal_kcal.name
    else:
        return KcalLevel.is_high_kcal.name
