from yunyun import question
from unittest.mock import patch
# from unittest.mock import MagicMock


@patch('yunyun.question.getInput', return_value="Choose")
def test_askTitle(mockclass):
    expectedTitle = mockclass.return_value
    query = question.QuestionFactory()
    title = query.askTitle()
    assert expectedTitle == title


@patch('yunyun.question.getInput', return_value="Attack,Defense")
def test_askSamples(mockclass):
    expectedValue = mockclass.return_value.split(",")
    query = question.QuestionFactory()
    result = query.askSamples()
    assert result == expectedValue


def test_askWeight():
    cases = [
        ("-2", -2)
    ]
    feature = "Test"
    for rawInput, expectedValue in cases:
        with patch('yunyun.question.getInput', return_value=rawInput):
            query = question.QuestionFactory()
            result = query.askWeight(feature)
            assert result == expectedValue


def test_askScore():
    cases = [
        ("2", 2)
    ]
    feature = "Test"
    sample = "Attack"
    for rawInput, expectedValue in cases:
        with patch('yunyun.question.getInput', return_value=rawInput):
            query = question.QuestionFactory()
            result = query.askScore(feature, sample)
            assert result == expectedValue


def test_askIsReadExists():
    cases = [
        ("y", True),
        ("Y", True),
        ("N", False),
        ("any", False),
    ]
    existsName = "xxx.csv"
    for rawInput, expectedValue in cases:
        with patch('yunyun.question.getInput', return_value=rawInput):
            query = question.QuestionFactory()
            result = query.askIsReadExists(existsName)
            assert result == expectedValue
