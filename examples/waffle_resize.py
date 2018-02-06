from guizero import App, Waffle, Slider, Text

def change_dim(slider):
    print("Changing width to " + str(g_width.value))
    grid.width = g_width.value
    grid.height = g_height.value
    print("Grid width is " + str(grid.width))

app = App("Changing size", layout="grid")

grid = Waffle(app, width=4, height=4, pad=0, grid=[1,0])

# Width
width_text = Text(app, text="Width", grid=[0,3])
g_width = Slider(app, start=0, end=20, command=change_dim, grid=[1,3])
g_width.value = 4

# Height
height_text = Text(app, text="Height", grid=[0,4])
g_height = Slider(app, start=0, end=20, command=change_dim, grid=[1,4])
g_height.value = 4


app.display()
