import os
import time
import re
from tabulate import tabulate
from .common import writeCSV, readCSV


class ThinkData:
    def __init__(
        self, title: str, samples: list, features: list, weights: list, scores: list
    ):
        self.title = title
        self.samples = samples
        self.features = features
        self.weights = weights
        self.scores = scores
        assert len(self.scores) == len(self.features)
        for col in self.scores:
            assert len(col) == len(self.samples)

    @property
    def nrow(self):
        return len(self.samples)

    @property
    def ncol(self):
        nSampleCol = 1
        nFinalScoreCol = 1
        return len(self.features) + nSampleCol + nFinalScoreCol

    @property
    def headers(self):
        featureHeaders = []
        for i in range(len(self.features)):
            header = "{feature}({weight})".format(
                feature=self.features[i], weight=self.weights[i]
            )
            featureHeaders.append(header)
        return ["Options"] + featureHeaders + ["Final score(Sorted)"]

    @property
    def rows(self):
        rows = []
        for i in range(self.nrow):
            sample = self.samples[i]
            values = [col[i] for col in self.scores]
            finalScore = weightSum(values, self.weights)
            row = [sample] + values + [finalScore]
            rows.append(row)
        # sortedRows = sorted(rows, key=lambda x: x[-1], reverse=True)
        return rows

    @property
    def table(self):
        rows = sorted(self.rows, key=lambda x: x[-1], reverse=True)
        return tabulate(rows, headers=self.headers)

    def __str__(self):
        return self.table

    def save(self, saveDir):
        """save data as csv file"""
        filename = "".join([self.title, ".csv"])
        filepath = os.path.join(saveDir, filename)
        writeCSV(filepath, rows=self.rows, headers=self.headers)
        return filepath


def readExists(filepath, title):
    rows, headers = readCSV(filepath)
    samples = []
    weights = []
    features = []
    scores = []
    for header in headers[1:-1]:
        # search = re.search(r"(.+)\((-?\d+)\)", header)
        feature, weight = parseHeader(header)
        features.append(feature)
        weights.append(weight)
    for row in rows:
        row.pop()
        samples.append(row.pop(0))
    for i in range(len(features)):
        colSocre = [row[i] for row in rows]
        scores.append([int(x) for x in colSocre])
    tkdata = ThinkData(title, samples, features, weights, scores)
    return tkdata


def parseHeader(header):
    search = re.search(r"(.+)\((-?\d+)\)", header)
    feature, weight = search.groups()
    weight = int(weight)
    return feature, weight


def uniqueId():
    uid = time.strftime("%Y%m%d%H%m%S", time.localtime())
    return uid


def weightSum(values, weights):
    s = 0
    for i in range(len(values)):
        s += values[i] * weights[i]
    return s
