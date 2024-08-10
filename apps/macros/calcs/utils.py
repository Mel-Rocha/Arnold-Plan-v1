from enum import Enum, auto


class Level(Enum):
    is_low = auto()
    is_normal = auto()
    is_high = auto()


class CalcMacroLevel:
    """
    Calculates and classifies the macronutrient based on the total energy value (i.e. total calories/day).
    """
    @staticmethod
    def calculate_level(amount, kcal, kcal_per_unit, low_threshold, high_threshold):
        """
        calculate the level of any macronutrient. It considers the amount of macronutrient (in grams),
        the total calories in the diet, the calories provided per unit of the macronutrient and the classification
        thresholds (low, normal, high).
        """
        # Calculates the energy value of the macronutrient
        nutrient_kcal = amount * kcal_per_unit
        # Calculates the percentage of the nutrient in relation to the total caloric value
        percentage = nutrient_kcal / kcal * 100

        # Determines level based on percentage
        if percentage < low_threshold:
            return Level.is_low.name
        elif percentage <= high_threshold:
            return Level.is_normal.name
        else:
            return Level.is_high.name

    def calculate_macro_level(self, amount, kcal, macro_type):
        thresholds = {
            'cho': (4, 55, 75),
            'fat': (9, 15, 30),
            'ptn': (4, 10, 15),
        }

        if macro_type not in thresholds:
            raise ValueError(f"Invalid macro_type: {macro_type}")

        kcal_per_unit, low_threshold, high_threshold = thresholds[macro_type]
        return self.calculate_level(amount, kcal, kcal_per_unit, low_threshold, high_threshold)


if __name__ == "__main__":
    # Criação de uma instância da classe CalcMacroLevel
    calc = CalcMacroLevel()

    # Exemplo de uso para calcular o nível de carboidratos (CHO)
    cho_amount = 150  # quantidade de carboidratos em gramas
    total_kcal = 2000  # total de calorias na dieta
    cho_level = calc.calculate_macro_level(cho_amount, total_kcal, 'cho')
    print(f"O nível de carboidratos é: {cho_level}")

    # Exemplo de uso para calcular o nível de gorduras (Fat)
    fat_amount = 40  # quantidade de gorduras em gramas
    fat_level = calc.calculate_macro_level(fat_amount, total_kcal, 'fat')
    print(f"O nível de gorduras é: {fat_level}")

    # Exemplo de uso para calcular o nível de proteínas (Ptn)
    ptn_amount = 70  # quantidade de proteínas em gramas
    ptn_level = calc.calculate_macro_level(ptn_amount, total_kcal, 'ptn')
    print(f"O nível de proteínas é: {ptn_level}")
