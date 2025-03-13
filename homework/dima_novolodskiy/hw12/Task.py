class Flowers:

    def __init__(self, name, color, lifespan, price, stem_length):
        self.name = name
        self.color = color
        self.lifespan = lifespan
        self.price = price
        self.stem_length = stem_length


class Rose(Flowers):
    def __init__(self, color):
        super().__init__("Rose", color, 5, 250, 80)


class Lily(Flowers):
    def __init__(self, color):
        super().__init__("Lily", color, 2, 120, 30)


class Tulip(Flowers):
    def __init__(self, color):
        super().__init__("Tulip", color, 3, 100, 50)


class Orchid(Flowers):
    def __init__(self, color):
        super().__init__("Orchid", color, 4, 110, 60)


class Chrysanthemum(Flowers):
    def __init__(self, color):
        super().__init__("Chrysanthemum", color, 6, 90, 45)


class Bouquet:

    def __init__(self):
        self.bouquet = []

    def add_flower(self, flower):
        self.bouquet.append(flower)

    def get_total_price(self):
        return sum(flower.price for flower in self.bouquet)

    def get_lifespan_bouquet(self):
        return round(sum(flower.lifespan for flower in self.bouquet) / len(self.bouquet))

    def sorted_bouqoet(self, param):
        return sorted(self.bouquet, key=lambda flower: getattr(flower, param))

    def find_flower(self, param, value):
        return [flower for flower in self.bouquet if getattr(flower, param) == value]


bouquet_on_8_murch = Bouquet()
bouquet_on_8_murch.add_flower(Rose('red'))
bouquet_on_8_murch.add_flower(Tulip('yellow'))
bouquet_on_8_murch.add_flower(Orchid('white'))
bouquet_on_8_murch.add_flower(Orchid('red'))
bouquet_on_8_murch.add_flower(Chrysanthemum('pink'))
bouquet_on_8_murch.add_flower(Lily('white'))
