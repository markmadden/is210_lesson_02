#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""More data types?"""

import decimal
import fractions

from decimal import Decimal
from fractions import Fraction

FLOATVAR = 0.1
DECIMALVAR = Decimal(0.1)
FRACTIONVAR = 1 / 10

DF_EQUALITY = DECIMALVAR == FRACTIONVAR
ARE_INEQUAL = DECIMALVAR != FRACTIONVAR != FLOATVAR
