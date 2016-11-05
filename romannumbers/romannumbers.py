#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    Romannumbers Copyright (C) 2012 Suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of Romannumbers.
#    Romannumbers is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Romannumbers is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Romannumbers.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
        Romannumbers by suizokukan (suizokukan AT orange DOT fr)
        ________________________________________________________________________

        Conversion between Roman numbers and Arabic numbers.
        ________________________________________________________________________

        Code largely inspired by Dive Into Python (http://www.diveintopython3.net/)
"""
VERSION = "0.0.0"

import re

ROMANNUMERALMAP = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('C', 100),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),
                   ('X', 10),
                   ('IX', 9),
                   ('V', 5),
                   ('IV', 4),
                   ('I', 1))

ROMANNUMERALPATTERN = re.compile("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")

#///////////////////////////////////////////////////////////////////////////////
def from_roman(src):
    """
        from_roman() function
        ________________________________________________________________________

        convert Roman numeral to an integer
        ________________________________________________________________________

        ARGUMENT:
        ▪ src : (str) the source string

        RETURNED VALUE : (bool)success
                         (int)result | (str)error message
    """
    if not src:
        return (False,
                "Can't convert a null string into a Roman numeral.")
    if not ROMANNUMERALPATTERN.search(src):
        return (False,
                "Invalid Roman numeral: %s" % src)

    result = 0
    index = 0
    for numeral, integer in ROMANNUMERALMAP:
        while src[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return (True, result)

#///////////////////////////////////////////////////////////////////////////////
def to_roman(src):
    """
        to_roman() function
        ________________________________________________________________________

        convert an integer to a Roman numeral
        ________________________________________________________________________

        ARGUMENT:
        ▪ src : (str) the integer to be converted

        RETURNED VALUE : (bool)success
                         (str)result | (str)error message
    """
    if src < 1:
        return (False,
                "Can't convert an integer smaller than 1")

    result = ""
    for numeral, integer in ROMANNUMERALMAP:
        while src >= integer:
            result += numeral
            src -= integer

    return (True, result)
