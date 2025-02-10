#task1 - class Circle
#Check if radii of two circles are equal (the == operator);
#Compare the lengths of two circles (the operators: >, <, <=, >=);
#Proportionally change the circle size by changing its radius (the operators: +, -, +=, -=).

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def __eq__(self,otherObj):
        if self.radius == otherObj.radius:
            return True
        else:
            return False

    def __gt__(self,otherObj):
        if self.radius > otherObj.radius:
            print(f'First circle is bigger')
        else:
            print(f'Second circle is bigger')
    
    def __add__(self,otherObj):
        return self.radius + otherObj.radius
    
    def __sub__(self, otherObj):
        new_radius = self.radius - otherObj.radius
        return new_radius

circle1 = Circle(10)
circle2 = Circle(8)
print(circle1 == circle2)
print(circle2 > circle1)
print(circle1 + circle2)
print(circle1 - circle2)

#task2 - complex class for complex numbers
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

num1 = Complex(3, 2)
num2 = Complex(1, 4)

print(num1 + num2)  
print(num1 - num2)  
print(num1 * num2)  
print(num1 / num2)  

#task3 - airplane class
#Check if the airplane types are equal (the == operator);
#Increasing and decreasing the number of passengers in the cabin (the operators: +, -, +=, -=);
#Compare two airplanes for the maximum possible number of passengers on board (the operators: >, <, <=, >=).

class Airplane:
    def __init__(self, type, passengers, maximum):
        self.type = type
        self.passengers = passengers
        self.maximum = maximum
        self.current_passengers = 0

    def __eq__(self,other):
        if self.type == other.type:
            return True
        else:
            return False
        
    def __add__(self, passengers):
        if self.current_passengers + passengers <= self.maximum:
            self.current_passengers += passengers
        else:
            raise ValueError("Exceeding maximum passenger limit")
        return self
        
    def __gt__(self,other):
        if self.maximum > other.maximum:
            return (f'Higher passenger capacity')
        else:
            return (f'Lower passenger capacity')
    
    def __lt__(self,other):
        if self.maximum < other.maximum:
            return (f'Lower passenger capacity')
        else:
            return (f'Higher passenger capacity')
        
plane1 = Airplane('boeing',180,200)
plane2 = Airplane('airbus',250,360)

print(plane1 == plane2)
print(plane1 < plane2)
plane1 += 10
print(plane1.passengers) 

#task4 - Apartment
#Check if the areas of the apartments are equal (the == operator);
#Check if the areas of the apartments are not equal (the != operator);
#Compare the prices of two apartments (the operators: >).

class Apartment:
    def __init__(self, area, price):
        self.area = area
        self.price = price
    
    def __eq__(self, other):
        return self.area == other.area
    
    def __ne__(self, other):
        return self.area != other.area
    
    def __gt__(self, other):
        return self.price > other.price

apartment1 = Apartment(1000, 500000)
apartment2 = Apartment(1200, 600000)
apartment3 = Apartment(1000, 550000)

print(apartment1 == apartment2)  
print(apartment1 == apartment3)  
print(apartment1 != apartment2)  
print(apartment1 != apartment3)  
print(apartment1 > apartment2)  
print(apartment2 > apartment3) 