from ipywidgets import widgets
from IPython.display import display
text.on_submit(handle_submit)
display(text)

def handle_submit(sender):
    print(text.value)

text.on_submit(handle_submit)
