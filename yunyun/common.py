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