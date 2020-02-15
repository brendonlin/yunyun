import re


class Question(object):
    commonAlert = "Incorrect input, please re-enter."

    def __init__(self, message, checks=[], parses=[]):
        self.message = message
        self.checks = checks
        self.parses = parses

    def ask(self):
        response = None
        while response is None:
            userInput = getInput(self.message)
            response = userInput
            isCorrect = True
            if len(self.checks) > 0:
                isCorrect = all([check(userInput)
                                 for check in self.checks])
            if isCorrect and len(self.parses) > 0:
                for parse in self.parses:
                    response = parse(response)
            if response is None:
                print(self.commonAlert)
        return response


class Rules():

    @staticmethod
    def notEmpty(x):
        return len(str(x)) > 0

    def inRange(valueRange=[]):
        def wapper(x):
            return x in valueRange
        return wapper


def splitStr(x):
    return re.split(",|，", x.replace(" ", ""))


class QuestionFactory():
    def askTitle(self):
        question = Question(
            message="What's the theme of this discussion: ",
            checks=[Rules.notEmpty],
            parses=[lambda x: re.sub(r"[^\w]", "", x)]
        )
        result = question.ask()
        return result

    def askIsReadExists(self, existsName):
        message = f"Find existing record '{existsName}'.Use this file? Y/N "
        question = Question(
            message=message,
            checks=[Rules.notEmpty],
            parses=[lambda x: x in ["Y", "y"]],
        )
        result = question.ask()
        return result

    def askSamples(self):
        message = "What's the objects to compare (separated by comma): "
        question = Question(
            message=message,
            checks=[Rules.notEmpty],
            parses=[splitStr],
        )
        result = question.ask()
        return result

    def askFeatures(self):
        message = "What's the features to compare (separated by comma): "
        question = Question(
            message=message,
            checks=[Rules.notEmpty],
            parses=[splitStr],
        )
        result = question.ask()
        return result

    def askWeight(self, feature):
        message = f"For {feature}, how much weight do you think? \
Choose from -2, -1, 0, 1, 2: "
        question = Question(
            message=message,
            checks=[Rules.notEmpty, Rules.inRange(
                ["-2", "-1", "0", "1", "2"])],
            parses=[lambda x: int(x)],
        )
        result = question.ask()
        return result

    def askScore(self, feature, sample):
        message = f"For {feature}, what's the score of {sample}? \
Choose from 0, 1, 2: "
        question = Question(
            message=message,
            checks=[Rules.notEmpty, Rules.inRange(
                ["0", "1", "2"])],
            parses=[lambda x: int(x)],
        )
        result = question.ask()
        return result


def getInput(text):
    return input(text)
