#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, request

import prime_tester

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.context_processor
def inject_globals():
    return {
        "something": [
            "СмеШНОе",
            "cRAZy",
            "weIRD",
            "что ЕЩЕ зА"
        ]
    }


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/wrong')
def leto():
    return flask.render_template(
        'wrong.html'
    )


@app.route('/index')
def letoleto():
    return flask.render_template(
        'index.html'
    )


@app.route('/wth', methods = ['GET'])
def im_going_to_test_your_number():
    result = 0
    if request.method == 'GET':
        text = request.args.get('text')                  ### НЕ РАБОТАЕТ!!!!!!
        if text is not None:
            result = prime_tester.is_prime(int(text))[0]
    return flask.render_template(
        'wth.html',
        name = str(result)
    )

if __name__ == '__main__':
   app.run(debug = True)
