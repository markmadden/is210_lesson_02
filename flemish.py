#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
IND = FISHY.index("Spanish")
VAR1L = len("Spanish")
FLEMISH = FISHY[:19] + "Flemish" + FISHY[26:]

"""
ignore scratchwork below
a , b, c, d, e = FISHY.split(' ',4)
d = "Flemish"
FISHY = a + b + c + d + e"""
