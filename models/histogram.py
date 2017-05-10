"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import sys
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class PlotBarChart:

    @staticmethod
    def init(app):

        app.figure = plt.figure()
        app.canvas = FigureCanvas(app.figure)
        app.toolbar = NavigationToolbar(app.canvas, app)

        app.histogram_bnt_plot = QtGui.QPushButton('Plot')
        app.histogram_bnt_plot.clicked.connect(lambda: PlotBarChart.plot(app))

        app.histogram_layout.addWidget(app.toolbar)
        app.histogram_layout.addWidget(app.canvas)
        app.histogram_layout.addWidget(app.histogram_bnt_plot)

    @staticmethod
    def plot(app):
        data = [np.random.random() for i in range(10)]

        ax = app.figure.add_subplot(111)

        ax.hold(False)
        ax.plot(data, '*-')

        app.canvas.draw()


    #     N = 5
    #     men_means = (20, 35, 30, 35, 27)
    #     men_std = (2, 3, 4, 1, 2)
    #
    #     ind = np.arange(N)  # the x locations for the groups
    #     width = 0.35  # the width of the bars
    #
    #     fig, ax = plt.subplots()
    #     rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)
    #
    #     women_means = (25, 32, 34, 20, 25)
    #     women_std = (3, 5, 2, 3, 3)
    #     rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)
    #
    #     # add some text for labels, title and axes ticks
    #     ax.set_ylabel('Scores')
    #     ax.set_title('Scores by group and gender')
    #     ax.set_xticks(ind + width / 2)
    #     ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
    #
    #     ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
    #
    #     PlotBarChart.autolabel(rects1, ax)
    #     PlotBarChart.autolabel(rects2, ax)
    #
    #     app.histogram_widget.addWidget(plt.plot())
    #
    # @staticmethod
    # def autolabel(rects, ax):
    #     """
    #     Attach a text label above each bar displaying its height
    #     """
    #     for rect in rects:
    #         height = rect.get_height()
    #         ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
    #                 '%d' % int(height),
    #                 ha='center', va='bottom')