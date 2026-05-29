class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print("Название ресторана: " + self.restaurant_name)
        print("Тип кухни: " + self.cuisine_type)
        print("Рейтинг: " + str(self.rating))

    def update_rating(self, new_rating):
        self.rating = new_rating

r = Restaurant("Хачапури и вино", "Грузинская")
r.update_rating(5)
r.describe_restaurant()