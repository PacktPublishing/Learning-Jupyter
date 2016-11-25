from ipywidgets import interactive
def myfunction(x):
    return x
w = interactive(myfunction, x= "Hello World ");
from IPython.display import display
display(w)
