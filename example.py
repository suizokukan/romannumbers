#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#    Romannumbers Copyright (C) 2012 suizokukan
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
###############################################################################
"""
        Romannumbers by suizokukan (suizokukan AT orange DOT fr)
        ________________________________________________________________________

        example.py
        ________________________________________________________________________

        Use this file to see how to call the romannumbers module.
"""
from romannumbers import romannumbers

print(romannumbers.from_roman("XIX"))
print(romannumbers.to_roman(1))
print(romannumbers.to_roman(100))
