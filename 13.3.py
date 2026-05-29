class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print("Название ресторана:", self.restaurant_name)
        print("Тип кухни:", self.cuisine_type)
        print("Рейтинг:", self.rating)

    def open_restaurant(self):
        print("Ресторан открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print("Рейтинг обновлён до", new_rating)


newRestaurant = Restaurant("Хачапури и вино", "Грузинская")

newRestaurant.describe_restaurant()

newRestaurant.update_rating(5)

newRestaurant.describe_restaurant()