#Task1:
#Implement a class Car. Class fields should store the following: model, year of release, manufacturer, engine capacity, color, price. 
#Implement class methods for data input and output, provide access to individual fields through class methods.

class Car:
    def __init__(self,model,year_of_release,manufacturer,engine_capacity,color,price):
        self.__model = model
        self.__year_of_release = year_of_release
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    def your_input(self):
        self.__model = input("Enter model: ")
        self.__year_of_release = int(input("Enter year of release: "))
        self.__manufacturer = input("Enter manufacturer: ")
        self.__engine_capacity = float(input("Enter engine capacity: "))
        self.__color = input("Enter color: ")
        self.__price = int(input("Enter price: "))
        return f'The info is as follows - {self.__model},{self.__year_of_release},{self.__manufacturer},{self.__engine_capacity},{self.__color},{self.__price}.'

    def showInfo(self):
        return f'The car is a {self.__color} {self.__model} made in {self.__year_of_release} by {self.__manufacturer} with the engine capacity of {self.__engine_capacity}. The price is {self.__price}.'
    
car1 = Car('Kodiaq','2021','Skoda','2.0 L','black','800.000 CZK')
print(car1.showInfo())
print(car1.your_input())

#Task2
#Implement a class Book. Class fields should store the following: title, year of release, publisher, genre, author, price. 
# # #Implement class methods for data input and output, provide access to individual fields through class methods.

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def set_title(self, title):
        self.__title = title
    
    def get_title(self):
        return self.__title

    def set_year(self, year):
        self.__year = year
    
    def get_year(self):
        return self.__year

    def set_publisher(self, publisher):
        self.__publisher = publisher
    
    def get_publisher(self):
        return self.__publisher

    def set_genre(self, genre):
        self.__genre = genre
    
    def get_genre(self):
        return self.__genre

    def set_author(self, author):
        self.__author = author
    
    def get_author(self):
        return self.__author

    def set_price(self, price):
        self.__price = price
    
    def get_price(self):
        return self.__price

    def input_data(self):
        self.__title = input("Enter title: ")
        self.__year = int(input("Enter year of release: "))
        self.__publisher = input("Enter publisher: ")
        self.__genre = input("Enter genre: ")
        self.__author = input("Enter author: ")
        self.__price = int(input("Enter price: "))
        print(f'The info is as follows - {self.__title}, {self.__year}, {self.__publisher}, {self.__genre}, {self.__author}, {self.__price}.')

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Year of Release: {self.__year}")
        print(f"Publisher: {self.__publisher}")
        print(f"Genre: {self.__genre}")
        print(f"Author: {self.__author}")
        print(f"Price: {self.__price}")       

book1 = Book("The Great Gatsby", 1925, "Scribner", "Novel", "F. Scott Fitzgerald", 350)
book1.display_info()
book1.input_data()

#task3
# #Implement a class Stadium. Class fields shout store the following: stadium's name, date of opening, country, city, seating capacity.
# #Implement class methods for data input and output, provide access to individual fields through class methods.

class Stadium:
    def __init__(self, name, opening_date, country, city, seating_capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__seating_capacity = seating_capacity

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_opening_date(self, opening_date):
        self.__opening_date = opening_date
    
    def get_opening_date(self):
        return self.__opening_date

    def set_country(self, country):
        self.__country = country
    
    def get_country(self):
        return self.__country

    def set_city(self, city):
        self.__city = city
    
    def get_city(self):
        return self.__city

    def set_seating_capacity(self, seating_capacity):
        self.__seating_capacity = seating_capacity
    
    def get_seating_capacity(self):
        return self.__seating_capacity

    def input_data(self):
        self.__name = input("Enter stadium's name: ")
        self.__opening_date = input("Enter date of opening (DD-MM-YYYY): ")
        self.__country = input("Enter country: ")
        self.__city = input("Enter city: ")
        self.__seating_capacity = int(input("Enter seating capacity: "))
        print(f'The info is as follows - {self.__name}, {self.__opening_date}, {self.__country}, {self.__city}, {self.__seating_capacity}.')

    def display_info(self):
        print(f"The stadium name is called {self.__name} located in {self.__city}, {self.__country} from {self.__opening_date}. The seating capacity is {self.__seating_capacity}.")

stadium1 = Stadium("Camp Nou", "24-09-1957", "Spain", "Barcelona", 99354)
stadium1.display_info()
stadium1.input_data()

