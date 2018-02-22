#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:45:52 2018

@author: sam
"""

import os
from flask_app import flask_app

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0' ,port=5000)