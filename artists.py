#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


THE_GREAT_QUESTION = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')
STATEMENTS = THE_GREAT_QUESTION.split(". ")	
ARTISTS = STATEMENTS[:4]
NUM_ARTISTS = len(ARTISTS)
CHARACTERS = len(THE_GREAT_QUESTION)