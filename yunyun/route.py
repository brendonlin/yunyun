
from flask import Flask, render_template, jsonify, request
import numpy as np
import pandas as pd
import pdb
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data_submit', methods=['POST'])
def data_submit():
    '''输出一个算好的表格即可'''
    formdata = request.form.to_dict()
    feature_weights = []
    scores = []
    for key in formdata:
        weight_match = re.match("^weight_(.*)", key)
        if weight_match:
            value = int(formdata[key])
            feature_weights.append([weight_match.groups()[0], value])
        else:
            score_match = re.match("^score_(.*)", key)
            if score_match:
                value = int(formdata[key])
                scores.append(score_match.groups()[0].split('_') + [value])
    # pd.DataFrame(scores)
    print(feature_weights, scores)
    feature_weights = [x[1] for x in feature_weights]
    df = parse(feature_weights, scores)
    return df.to_html(classes='" id = "result_table', index=False)


def parse(feature_weights, scores):
    df = pd.DataFrame(scores)
    df.columns = ['feature', 'solution', 'score']
    df.set_index(['solution', 'feature'], inplace=True)
    df = df.unstack()
    df.columns = df.columns.get_level_values('feature')
    profit_arr = cal_profit(df.values, feature_weights)
    df['profit'] = profit_arr
    df.loc['weight'] = feature_weights + ['-']
    df.reset_index(inplace=True)
    return df


def cal_profit(score_arr, feature_weights):
    '''计算最后的利润'''
    return np.mat(score_arr) * np.mat(feature_weights).T
