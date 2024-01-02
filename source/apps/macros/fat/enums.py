from enum import Enum, auto

class FatLevel(Enum):
    is_low_fat = auto()
    is_normal_fat = auto()
    is_high_fat = auto()

@staticmethod
def calculate_fat_level(fat, kcal):
    fat_kcal = fat * 9
    fat_percentage = fat_kcal / kcal * 100

    if fat_percentage < 15:
        return FatLevel.is_low_fat.name
    elif fat_percentage <= 30:
        return FatLevel.is_normal_fat.name
    else:
        return FatLevel.is_high_fat.name