from ipywidgets import *
w = IntSlider()
w.keys

#
from ipywidgets import *
Text(value='You can not change this text!', disabled=True)

#
from ipywidgets import *
w = IntSlider()
original = w.value
w.value = 5
original, w.value
