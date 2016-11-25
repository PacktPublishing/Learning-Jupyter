from ipywidgets import *
from IPython.display import display

slider = widgets.FloatSlider()
message = widgets.Text(value='Hello World')
container = widgets.Box(children=[slider, message])
container.layout.border = '1px black solid'

display(container)

#
from ipywidgets import *
from IPython.display import display

container = widgets.Box()
container.layout.border = '1px black solid'
display(container)

slider = widgets.FloatSlider()
message = widgets.Text(value='Hello World')
container.children=[slider, message]
