# Create a class for a number. The class should have the following functionality imple­mented:
# Write and read values.
# Convert a number to octal.
# Convert a number to hexadecimal.
# Convert a number to binary.
# Test all the possibilities of the created class using unit testing (unittest).

class Number:
    def __init__(self, value):
        self.value = value 
    
    def set_value(self, new_value):
        self.value = new_value
    
    def get_value(self):
        return self.value
    
    def to_octal(self):
        return oct(self.value)
    
    def to_hexadecimal(self):
        return hex(self.value)
    
    def to_binary(self):
        return bin(self.value)


num = Number(42)
print(num.get_value())      
print(num.to_octal())       
print(num.to_hexadecimal())  
print(num.to_binary())       

