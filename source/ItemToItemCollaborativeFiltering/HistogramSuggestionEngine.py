import numpy as np
from sklearn.metrics import mean_squared_error

class HistogramSuggestionEngine:
    def __init__(self, fileName, trainDataSize, cellCount, separator):
        self.fileName = fileName
        self.trainDataSize = trainDataSize
        self.cellCount = cellCount
        self.separator = separator
        self.signalData = np.genfromtxt(fileName, filling_values = 0, delimiter = separator)

    def computeSuggestions(self):
        similarItems = []
        for i in range(self.trainDataSize):
            candidates = []
            for j in range(self.trainDataSize):
                if i == j:
                    continue
                else:
                    distance = mean_squared_error(self.signalData[i], self.signalData[j])
                    if len(candidates) < 10:
                        candidates.append((j, distance))
                    else:
                        worse = [index for (dist, index) in candidates if dist > distance]
                        if len(worse) > 0:
                            candidates[min(worse)] = (distance, j)
            candidates.sort(key=lambda tuple: tuple[1], reverse=False)
            similarItems.append(candidates)
        self.recommendations = np.array(similarItems)

"""filepath = ""
seperator = ","
train_size = 100000
cellCount = 8192
se = HistogramSuggestionEngine(filepath, train_size, cellCount, seperator)
se.computeSuggestions()
print(se.recommendations)"""
