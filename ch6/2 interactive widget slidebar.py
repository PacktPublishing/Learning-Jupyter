from ipywidgets import interact
# define a function to work with (cubes the number)
def myfunction(arg):
    return arg+1
interact(myfunction, arg=9);
