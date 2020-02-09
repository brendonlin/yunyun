# -*- coding:utf-8 -*-
# think like a robot
# import time
import re
import os
import time

# from io import StringIO
from .models import ThinkData, readExists

SAVE_DIR = "tests/data"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


def main():
    print("程序已启动。请根据提示输入。")
    x = input("请输入本次思考的主题：")
    title = re.sub(r"[^\w]", "", x)
    existsName = checkIsExists(SAVE_DIR, title)
    isReadExists = False
    if existsName:
        x = input(f"发现既有的记录{existsName}。是否使用该文件。Y/N")
        if x in ["Y", "y"]:
            isReadExists = True
    if isReadExists:
        filepath = os.path.join(SAVE_DIR, existsName)
        tdata = readExists(filepath, title)
    else:
        print("开始创建新的记录")
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
    x = input("请输入要对比的对象（中文或英文逗号分隔每个对象）：")
    samples = splitStr(x)
    x = input("请输入要比较的特征（中文或英文逗号分隔每个对象）：")
    features = splitStr(x)
    weights = []
    for feature in features:
        message = f"对于{feature}，你觉得权重有多大，请在-2,-1,0，1，2中选择："
        x = input(message)
        weights.append(int(x))
    scores = []
    for feature in features:
        colScores = []
        for sample in samples:
            message = f"对于{feature}，你觉得{sample}怎么样，请在0,1,2中选择："
            x = input(message)
            colScores.append(int(x))
        scores.append(colScores)
    tdata = ThinkData(title, samples, features, weights, scores)
    return tdata


def checkIsExists(saveDir, title):
    filenames = os.listdir(saveDir)
    for filename in filenames:
        if title in filename:
            return filename


def searchExistsData():
    """搜索并读取既有的数据"""
    # flag_select = ctypes.windll.user32.MessageBoxW(
    #     0, "请问是否新建数据？\n确定点击是，自定义点击否，退出点击取消", "提示", 3
    # )
    # if flag_select == 7:
    #     os.startfile(SAVE_DIR_PATH)
    #     input_filename = input("请输入文件的名称：")
    #     filename = ""
    #     for x in os.listdir(SAVE_DIR_PATH):
    #         if input_filename in x:
    #             filename = x
    #             break
    #     if not filename:
    #         ctypes.windll.user32.MessageBoxW(0, "抱歉！未找到该文件", "提示", 1)
    #         sys.exit()

    #     file_save_path = os.path.join(SAVE_DIR_PATH, filename)
    #     with open(file_save_path, "r") as f:
    #         stream = f.read()
    #     import pandas as pd

    #     data = pd.read_csv(StringIO(stream), index_col=0)
    #     return data
    # elif flag_select == 2:
    #     sys.exit()
    pass


def splitStr(x):
    return re.split(",|，", x.replace(" ", ""))


# def cal_profit(score_arr, weights):
#     """计算最后的利润"""
#     return np.mat(score_arr) * np.mat(weights).T


# def splitdata(data):
#     """分割数据集为几个部分"""
#     config = {}
#     config["samples"] = np.array(data.index)[:-1]
#     config["features"] = np.array(data.columns)
#     config["score_arr"] = data.values[:-1]
#     config["weights"] = data.values[-1]
#     return config


# def scoreSolutions(data):
#     """对输入的数据集进行处理"""
#     config = splitdata(data)
#     profit_arr = cal_profit(config["score_arr"], config["weights"])
#     profit_arr = profit_arr.A.flatten()
#     best_sol = config["samples"][profit_arr.argmax()]
#     import pandas as pd

#     ser = pd.Series(profit_arr, index=config["samples"])
#     ser.name = "final_score"
#     result = pd.concat([data, ser], axis=1)
#     return result
