class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана:", self.restaurant_name)
        print("Тип кухни:", self.cuisine_type)

    def open_restaurant(self):
        print("Ресторан открыт!")

r1 = Restaurant("Италия", "Итальянская")
r2 = Restaurant("Сушивок", "Японская")
r3 = Restaurant("Бургер Хаус", "Американская")

r1.describe_restaurant()
print()
r2.describe_restaurant()
print()
r3.describe_restaurant()