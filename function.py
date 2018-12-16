import pandas as pd

pd.options.mode.chained_assignment = None

# Get Abbreviation
def getAbb(obj):
    for i, v in enumerate(obj):
        obj[i] = obj[i][obj[i].find("(") + 1:obj[i].find(")")]
    return obj