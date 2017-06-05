from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
from matplotlib.figure import Figure



class PlotBarChart:

    @staticmethod
    def init(app):

        app.figure = Figure(facecolor='#6fa18f')
        app.canvas = FigureCanvas(app.figure)
        app.canvas.setParent(app)
        # app.figure.suptitle('Consumption by Equipment')

        # Since we have only one plot, we can use add_axes
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        app.axes = app.figure.add_subplot(111)

        app.axes.set_title('Consumption by Equipment')
        app.axes.set_xlabel('R$')
        app.axes.set_ylabel('Equipments')

        # Create the navigation toolbar, tied to the canvas
        app.mpl_toolbar = NavigationToolbar(app.canvas, app)

        app.histogram_layout.addWidget(app.mpl_toolbar)
        app.histogram_layout.addWidget(app.canvas)

    @staticmethod
    def plot(app, data):
        # equipments = ['TV', 'Air Conditioner', 'Fridge', 'Computer', 'Another Equipment']
        # data = [40, 1000, 20, 30, 4000]

        equipments = data.keys()
        data = data.values()

        x = range(len(data))

        # clear the axes and redraw the plot anew
        app.axes.clear()

        app.axes.barh(x, data, height=0.5, align='center', tick_label=equipments, color='#015f3d')

        app.axes.set_title('Consumption by Equipment')
        app.axes.set_xlabel('R$')
        app.axes.set_ylabel('Equipments')

        app.figure.tight_layout()
        app.canvas.draw()


class NavigationToolbar(NavigationToolbar2QT):

    toolitems = [t for t in NavigationToolbar2QT.toolitems if
                 t[0] == 'Save']