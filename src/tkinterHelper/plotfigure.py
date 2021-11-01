import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)
from matplotlib.figure import Figure


class PlotFigure(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        """OptionMenu

        Args:
            root: root or frame where the plot figure be added
        """
        super().__init__(root, *args, **kwargs)

        # plot axis
        self._fig = Figure()
        self._canvas = FigureCanvasTkAgg(self._fig, master=root)
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(fill='both', expand=True)

        # toolbar
        toolbarFrame = tk.Frame(root)
        toolbarFrame.pack(side='bottom', fill='x')
        self._toolbar = NavigationToolbar2Tk(self._canvas, toolbarFrame)

    @property
    def fig(self) -> Figure:
        return self._fig

    def updatePlot(self):
        self._fig.canvas.draw()
        self._fig.canvas.flush_events()
