#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42
NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1:0>6d}!'

EMAIL = NEWS.format(NTYPE, RNUM, friend=FNAME)

'''
IGNORE SCRATCHWORK BELOW

EMAIL = NEWS.format("great", 210, friend="Chad")
EMAIL = NEWS.format(friend=FNAME, NTYPE, RNUM)
scratch work


NEWS = NEWS.format(a,b,%06d)'''
