#Create a class containing a set of integers. The class should have the following functionality implemented:
# The sum of elements in the set.
# Arithmetic mean of elements in the set.
# Maximum of the elements in the set.
# Minimum of the elements in the set.
# Test all the possibilities of the created class using unit testing (unittest).

class IntegerSet:
    def __init__(self, numbers=None):
        self.numbers = set(numbers)
    
    def sum_elements(self):
        return sum(self.numbers)
    
    def arithmetic_mean(self):
        return sum(self.numbers) / len(self.numbers)
    
    def max_element(self):
        return max(self.numbers)
    
    def min_element(self):
        return min(self.numbers)
