#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:43:10 2018

@author: sam
"""

from flask import render_template
from flask_app import flask_app

from systeminfo import main

@flask_app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Hello'
    returnDict['title'] = 'COMP30670'
    returnDict['platform'] = main.get_platform()
    print(main.get_platform())
    return render_template('index.html', **returnDict)
