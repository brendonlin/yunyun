import re


class Question(object):
    commonAlert = "输入有误，请重新输入"

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
            message="请输入本次思考的主题：",
            checks=[Rules.notEmpty],
            parses=[lambda x: re.sub(r"[^\w]", "", x)]
        )
        result = question.ask()
        return result

    def askIsReadExists(self, existsName):
        question = Question(
            message=f"发现既有的记录'{existsName}'。是否使用该文件。Y/N",
            checks=[Rules.notEmpty],
            parses=[lambda x: x in ["Y", "y"]],
        )
        result = question.ask()
        return result

    def askSamples(self):
        question = Question(
            message="请输入要对比的对象（中文或英文逗号分隔每个对象）：",
            checks=[Rules.notEmpty],
            parses=[splitStr],
        )
        result = question.ask()
        return result

    def askFeatures(self):
        question = Question(
            message="请输入要比较的特征（中文或英文逗号分隔每个对象）：",
            checks=[Rules.notEmpty],
            parses=[splitStr],
        )
        result = question.ask()
        return result

    def askWeight(self, feature):
        message = f"对于{feature}，你觉得权重有多大，请在-2,-1,0,1,2中选择："
        question = Question(
            message=message,
            checks=[Rules.notEmpty, Rules.inRange(
                ["-2", "-1", "0", "1", "2"])],
            parses=[lambda x: int(x)],
        )
        result = question.ask()
        return result

    def askScore(self, feature, sample):
        message = f"对于{feature}，你觉得{sample}怎么样，请在0,1,2中选择："
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
