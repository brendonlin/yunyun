from yunyun import thinkdata


def test_thinkData():
    title = "RouteChoose001"
    samples = ["Plane", "Train"]
    features = ["Distance", "Price"]
    weights = [-1, -2]
    scores = [[1, 2], [2, 1]]
    tkdata = thinkdata.ThinkData(title, samples, features, weights, scores)
    print("")
    print(tkdata)
    filepath = tkdata.save(saveDir="tests/data")
    tkdata_ = thinkdata.readExists(filepath, title)
    assert tkdata_.scores == tkdata.scores


def testParseHeader():
    cases = [("price(2)", ("price", 2))]
    for case in cases:
        header, excepted = case
        result = thinkdata.parseHeader(header)
        assert result == excepted
