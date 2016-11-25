import ipywidgets as widgets
from IPython.display import display
w = widgets.Dropdown(
    options={'Pen': 7732, 'Pencil': 102, 'Pad': 33331},
    description='Item:',
)
display(w)
w.value
