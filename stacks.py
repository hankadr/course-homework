#task1 - user inputs a set of numbers from the keyboard. 
# The received numbers should be saved in a list (the type of list is selected based on the task below). 
# After this, display a menu offering the user the following items:
#Add a new number to the list (if such a number exists in the list, inform the user about it and do not add the number).
#Delete all occurrences of the number from the list (the user inputs a number to be deleted).
#Show the list contents (show the list from the beginning or the end based on the user's choice).
#Check if the list contains this value.
#Replace the value in the list (the user decides whether to replace only the first occurrence or all occurrences).
#The action is performed based on the user's choice, and the menu displays again.
        
def main():
    numbers = [] 
    user_input = input('Please submit the set of numbers separated by spaces: ')
    numbers = list(map(int, user_input.split())) 

    while True:
        print("\nMenu:")
        print("1. Add a new number")
        print("2. Delete all occurrences of a number")
        print("3. Show list contents")
        print("4. Check if the list contains a value")
        print("5. Replace a value")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            number = int(input('State the number you wish to add: '))
            if number in numbers:
                print('The number is already included.')
            else:
                numbers.append(number)
                print('The number has been added.')

        elif choice == '2':
            number = int(input('State the number you wish to remove: '))
            if number in numbers:
                numbers = [x for x in numbers if x != number]
                print('All occurrences removed.')
            else:
                print('Number not found in the list.')

        elif choice == '3':
            sorting = input('Ascending or descending? ').lower()
            if sorting == 'ascending':
                print(f'Here is the ascending list: {sorted(numbers)}')
            elif sorting == 'descending':
                print(f'Here is the descending list: {sorted(numbers, reverse=True)}')
            else:
                print('Invalid choice.')

        elif choice == '4':
            value = int(input('What value are we looking for? '))
            if value in numbers:
                print('The value is included.')
            else:
                print('Value is not included.')

        elif choice == '5':
            replaceable = int(input('Which value do you wish to replace? '))
            if replaceable in numbers:
                new_value = int(input('What is the new value? '))
                occurrence = input('Replace (f)irst occurrence or (a)ll occurrences? ').lower()

                if occurrence == 'f':
                    index = numbers.index(replaceable)
                    numbers[index] = new_value
                elif occurrence == 'a':
                    numbers = [new_value if x == replaceable else x for x in numbers]
                print('Replacement done.')
            else:
                print("Number not found in the list.")

        elif choice == "6":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

#task2 -  a stack class to work with strings (string stack). The stack should have a fixed size.
#Implement a set of operations for working with the stack:
#putting a string to stack;
#pushing a string from stack;
#counting the number of strings in stack;
#checking whether the stack is empty;
#checking whether the stack is full;
#clearing stack;
#getting a value without pushing the top string from stack.
#When the app starts, display a menu allowing the user to choose the required option.

class StringStack:
    def __init__(self,size):
        self.size = size
        self.stack = []

    def push(self,string):
        self.stack.append(string)
        return (f'{string} added to the stack.')
    
    def pop(self):
        if not self.stack:
            return "Stack is empty."
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.size
    
    def clear(self):
        return self.stack.clear()
    
    def peek(self):
        if not self.stack:
            return "Stack is empty."
        return self.stack[-1]
    
def menu():
    size = int(input("Enter the size of the stack: "))
    stack = StringStack(size)
    
    while True:
        print("\nMenu:")
        print("1. Push a string to stack")
        print("2. Pop a string from stack")
        print("3. Peek at the top string")
        print("4. Check if stack is empty")
        print("5. Check if stack is full")
        print("6. Get the number of strings in stack")
        print("7. Clear the stack")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            string = input("Enter a string to push: ")
            stack.push(string)
        elif choice == "2":
            popped = stack.pop()
            if popped is not None:
                print(f'Popped: "{popped}"')
        elif choice == "3":
            top = stack.peek()
            if top is not None:
                print(f'Top of stack: "{top}"')
        elif choice == "4":
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        elif choice == "5":
            print("Stack is full." if stack.is_full() else "Stack is not full.")
        elif choice == "6":
            print(f'Number of strings in stack: {stack.count()}')
        elif choice == "7":
            stack.clear()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()

#task3 - make stack from the task 2 without fixed size

class StringStack:
    def __init__(self):
        self.stack = []
    
    def push(self, string):
        self.stack.append(string)
        print(f'"{string}" pushed to stack.')
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty! Nothing to pop.")
            return None
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty! Nothing to peek.")
            return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def count(self):
        return len(self.stack)
    
    def clear(self):
        self.stack.clear()
        print("Stack cleared.")
    

def menu():
    stack = StringStack()
    
    while True:
        print("\nMenu:")
        print("1. Push a string to stack")
        print("2. Pop a string from stack")
        print("3. Peek at the top string")
        print("4. Check if stack is empty")
        print("5. Get the number of strings in stack")
        print("6. Clear the stack")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            string = input("Enter a string to push: ")
            stack.push(string)
        elif choice == "2":
            popped = stack.pop()
            if popped is not None:
                print(f'Popped: "{popped}"')
        elif choice == "3":
            top = stack.peek()
            if top is not None:
                print(f'Top of stack: "{top}"')
        elif choice == "4":
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        elif choice == "5":
            print(f'Number of strings in stack: {stack.count()}')
        elif choice == "6":
            stack.clear()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()










