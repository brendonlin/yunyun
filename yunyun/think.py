# -*- coding:utf-8 -*-
# Think like a robot
import os
import time
from .thinkdata import ThinkData, readExists
from .question import QuestionFactory
from . import common


USER_PATH = os.path.expanduser("~")

SAVE_DIR = os.path.join(USER_PATH, "Documents", "Yunyun")

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


@common.catchKeyboardInterrupt
def main():
    print("Start yunyun.")
    query = QuestionFactory()
    title = query.askTitle()
    existsName = common.checkIsExists(SAVE_DIR, title)
    isReadExists = False
    if existsName:
        isReadExists = query.askIsReadExists(existsName)
    if isReadExists:
        filepath = os.path.join(SAVE_DIR, existsName)
        tdata = readExists(filepath, title)
        print("Reading exists data complete.")
    else:
        print("Creating new record.")
        tdata = humanInputData(title)
    tdata.save(SAVE_DIR)
    print("Save complete. Start processing data...")
    x = time.time()
    # result = tdata.table
    taketime = time.time() - x
    time.sleep(max(1 - taketime, 0))
    print("Processing complete. Please see the results.\n")
    time.sleep(0.5)
    print(f"Theme: {tdata.title}\n")
    print(tdata)
    # return result


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
