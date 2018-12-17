import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

# Get Abbreviation
def getAbb(obj):
    for i, v in enumerate(obj):
        obj[i] = obj[i][obj[i].find("(") + 1:obj[i].find(")")]
    return obj

# Get Total Access each Year
def getAccessYr(data, limit, column='LastAccess'):
    access = pd.DatetimeIndex(data[column]).year.value_counts().head(limit).sort_value()
    return access

# Set text to each plot
def setPlotText(data, x, y, val='', halign='right', valign='bottom', color='black'):
    for i, v in enumerate(data):
        plt.text(i+(x), v+(y), str(v) + val, horizontalalignment=halign, verticalalignment=valign, color=color, fontweight='bold')

# Show plot
def showPlot(title, xlabel='', ylabel=''):
    # Set plot title
    plt.title(title)
    # Set plot label
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Show plot
    plt.show()
