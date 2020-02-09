import os
from yunyun import common


def test_writeAndReadCSV():
    rows = [["1", "2"], ["3", "4"]]
    headers = ["a", "b"]
    fp = "tests/data/testCSV.csv"
    common.writeCSV(fp, rows, headers)
    assert os.path.exists(fp)
    rows_, headers_ = common.readCSV(fp)
    assert headers_ == headers
    assert rows_ == rows
    os.remove(fp)

