#! /usr/bin/env python3


from bottle import route, run


@route('/')
def home():
    return "it\'s my text home page!"


run(host='localhost', port=9999)
