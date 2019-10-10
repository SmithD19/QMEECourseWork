# Variable scope

# variables in functions are invisible outside of that
# function and will not persist after the function has
# run. These are called local variables

# global variables are visile inside and outside of
# functions. they are assigned using global and '_'
# as a prefix

# Global not assigned
_a_global = 10


def a_function():
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ", _a_global)
    print("Inside the function, the value is ", _a_local)
    return None


a_function()

print("Outside the function, the value is ", _a_global)


## Global assigned

_a_global = 10

def a_function():
    global _a_global
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ", _a_global)
    print("Inside the function, the value is ", _a_local)
    return None

a_function()
print("Outside the function, the value is", _a_global)