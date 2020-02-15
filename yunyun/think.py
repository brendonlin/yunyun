# -*- coding:utf-8 -*-
# think like a robot
import os
import time
from .thinkdata import ThinkData, readExists
from .question import QuestionFactory
from . import common


USER_PATH = os.path.expanduser("~")

SAVE_DIR = os.path.join(USER_PATH, "Documents", "Yunyun")

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


def main():
    print("程序已启动，请根据提示输入。")
    query = QuestionFactory()
    title = query.askTitle()
    existsName = common.checkIsExists(SAVE_DIR, title)
    isReadExists = False
    if existsName:
        isReadExists = query.askIsReadExists(existsName)
    if isReadExists:
        filepath = os.path.join(SAVE_DIR, existsName)
        tdata = readExists(filepath, title)
        print("读取历史记录完毕。")
    else:
        print("开始创建新的记录。")
        tdata = humanInputData(title)
    tdata.save(SAVE_DIR)
    print("存储完毕。正在处理数据...")
    x = time.time()
    result = tdata.table
    taketime = time.time() - x
    time.sleep(max(1 - taketime, 0))
    print("处理结束。请查看结果。\n")
    time.sleep(0.5)
    print(f"Topic:{tdata.title}\n")
    print(tdata)
    return result


def humanInputData(title):
    """Input data by human"""
    query = QuestionFactory()
    samples = query.askSamples()
    features = query.askFeatures()
    weights = [query.askWeight(feature) for feature in features]
    scores = []
    for feature in features:
        colScores = [query.askScore(feature, sample) for sample in samples]
        scores.append(colScores)
    tdata = ThinkData(title, samples, features, weights, scores)
    return tdata
