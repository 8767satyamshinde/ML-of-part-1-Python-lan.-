def greet(name):
    return f"Hello, {name}"

# Assign function to a variable
say_hello = greet

# Call the function using the new variable
print(say_hello("swapnil"))  # Output: Hello, swapnil

# Passing a function as an argument
def execute_func(func, name):
    return func(name)

print(execute_func(greet, "Prachi"))  # Output: Hello, prachi


#In Python, functions are treated as first-class objects. 
# This means that functions can be passed as arguments to other functions, returned from a function, and assigned to variables.
