from yunyun import models


def test_thinkData():
    title = "RouteChoose001"
    samples = ["Plane", "Train"]
    features = ["Distance", "Price"]
    weights = [-1, -2]
    scores = [[1, 2], [2, 1]]
    tkdata = models.ThinkData(title, samples, features, weights, scores)
    print("")
    print(tkdata)
    filepath = tkdata.save(saveDir="tests/data")
    tkdata_ = models.readExists(filepath, title)
    assert tkdata_.scores == tkdata.scores


def testParseHeader():
    cases = [("price(2)", ("price", 2))]
    for case in cases:
        header, excepted = case
        result = models.parseHeader(header)
        assert result == excepted
