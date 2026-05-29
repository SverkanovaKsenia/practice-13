class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана: " + self.restaurant_name)
        print("Тип кухни: " + self.cuisine_type)

r1 = Restaurant("Итальянский дворик", "Итальянская")
r2 = Restaurant("Суши-мастер", "Японская")
r3 = Restaurant("БР хаус", "Американская")

r1.describe_restaurant()
print()
r2.describe_restaurant()
print()
r3.describe_restaurant()