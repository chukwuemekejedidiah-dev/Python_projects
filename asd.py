class Car:
    def __init__(self, name, color, engine_type, raw_price, pretty_price, model, year):
        self.name = name
        self.color = color
        self.engine_type = engine_type
        self.raw_price = raw_price
        self.pretty_price = pretty_price
        self.model = model
        self.year = year

    def sound(self):
        print("I go vroom!")


Porsche = Car(
    name="911",
    color="white",
    engine_type="v6 engine",
    raw_price="3500000",
    pretty_price="$3.5 M",
    model="Porsche",
    year="2020"
)

Porsche.sound()