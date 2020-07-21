# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from push_news_to_bot import start_go, dell, data_json, data_lits
import datetime

app = Flask(__name__)


def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def get_txts():
    with open('log', 'r') as t:
        return len(t.read().splitlines())


@app.route('/', methods=['GET'])
def write_txt():
    t1 = []
    try:
        with open('log', 'r') as t:
            for i in t:
                t1.append(eval(i))
        return render_template('index.html', txt=t1)
    except Exception:
        return '<a href="./get"><h1>无数据</h1></a>'


@app.route('/get', methods=['GET'])
def get():
    try:
        start_go()
        return render_template('get.html', data=data_lits)
    finally:
        dell()


@app.route('/api', methods=['GET'])
def api():
    try:
        start_go()
        return str(data_json).replace("'", '"')
    finally:
        dell()


@app.route('/add', methods=['POST'])
def add():
    addTXT, delTXT = [], []
    json = request.form.getlist('txt')
    with open('log', 'a+') as t:
        if get_txts() == 0:
            id = 1
        else:
            id = get_txts() + 1
        for i  in data_lits:
            i = "{}".format(i)
            if i not in json:
                j = eval(i)
                j['px'] = id
                new_t = j['title']
                j['title'] = new_t.replace("\n", '')
                t.write("{}\n".format(j))
                addTXT.append(eval(i))
                id += 1
            else:
                delTXT.append(eval(i))
    return render_template('add.html', addTXT=addTXT, delTXT=delTXT)


@app.route('/echo', methods=['GET'])
def echo():
    t1 = []
    try:
        with open('log', 'r') as t:
            for i in t:
                t1.append(eval(i))
        return render_template('echo.html', log=t1)
    except Exception:
        return '<a href="./get"><h1>无数据</h1></a>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
