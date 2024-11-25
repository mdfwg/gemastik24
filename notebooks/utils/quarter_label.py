import pandas as pd

def generateQuarterLabels(startDate, endDate, offset):
    labels = []
    currentDate = startDate
    while currentDate < endDate:
        nextDate = currentDate + pd.DateOffset(months=offset)
        label = f"{currentDate.strftime('%Y_%m')}-{(nextDate - pd.DateOffset(days=1)).strftime('%Y_%m')}"
        labels.append((currentDate, nextDate, label))
        currentDate = nextDate
    return labels

def assignQuarter(timestamp, quarterLabels):
    for startDate, endDate, label in quarterLabels:
        if startDate <= timestamp < endDate:
            return label
    return None

def labelQuarters(df, dateColumn, offset=3):
    start_date = df[dateColumn].min()
    end_date = df[dateColumn].max()
    quarter_labels = generateQuarterLabels(start_date, end_date, offset)
    df['quarter'] = df[dateColumn].apply(lambda x: assignQuarter(x, quarter_labels))
    return df