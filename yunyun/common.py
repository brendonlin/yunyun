import sys
import os
import csv


def writeCSV(filepath, rows, headers):
    with open(filepath, "w", newline="") as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        spamwriter.writerow(headers)
        for row in rows:
            spamwriter.writerow(row)


def readCSV(filepath):
    rows = []
    with open(filepath, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:
            rows.append(list(row))
    headers = rows.pop(0)
    return rows, headers


def checkIsExists(saveDir, title: str):
    filenames = os.listdir(saveDir)
    for filename in filenames:
        if title in filename:
            return filename
    return False


def catchKeyboardInterrupt(func, *args, **kwargs):
    def wapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except KeyboardInterrupt:
            sys.exit()
        return result
    return wapper
