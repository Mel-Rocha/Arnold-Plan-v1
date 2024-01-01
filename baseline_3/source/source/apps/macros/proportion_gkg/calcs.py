class ProportionGKG:
    def __init__(self, weight, cho, ptn, fat):
        self.cho_proportion = cho / weight
        self.ptn_proportion = ptn / weight
        self.fat_proportion = fat / weight
        self.cho = self.cho_proportion * weight


