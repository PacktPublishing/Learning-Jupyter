from ipywidgets import widgets
from IPython.display import display

button = widgets.Button(description="Submit");
display(button)

def on_button_clicked(widget):
    print("Clicked Button:" + widget.description);
    
button.on_click(on_button_clicked);
