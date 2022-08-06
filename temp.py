import matplotlib

matplotlib.use("TkAgg")

from matplotlib.figure import figure
from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg,
	NavigationToolbar2Tk
)

data = {
	"One" : 1,
	"Two" : 2,
	"Three" : 3,
	"Four" : 4,
	"Five" : 5
}

word = data.keys()
value = data.values()

figure = Figure(figsize=(6, 4), dpi = 400)

figure_canvas = FigureCanvasTkAgg(figure, self)

NavigationToolbar2Tk(figure_canvas, self)

axes = figure.add_subplot()
