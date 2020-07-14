#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:36:00 2020

@author: mo
"""
import os
import fxcmpy

path = os.getcwd()

token_path = path + "/keys/fxcm_key.txt"

con = fxcmpy.fxcmpy(access_token = open(token_path, 'r').read().strip('\n'), log_level = 'error', server='demo')

pair = 'LUR/USD'


