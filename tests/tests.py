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

        tests/tests.py

        to launch the tests :

                $ nosetests

                or

                $ python -m unittest tests/tests.py
        ________________________________________________________________________

        class
          ▪ Tests
"""
import unittest

from romannumbers import romannumbers


class Tests(unittest.TestCase):
    """
        Tests class
        ________________________________________________________________________

        use this class to test the romannumbers/romannumbers.py file
        ________________________________________________________________________

        no class attribute

        no instance attribute

        methods :

        ● test__from_roman(self)
        ● test__to_roman(self)
    """

    def test__from_roman(self):
        """
            Tests.test__from_roman()
            ____________________________________________________________________

            Test of the romannumbers/romannumbers.py::from_roman() function
            ____________________________________________________________________

            no PARAMETER, no RETURNED VALUE
        """
        self.assertEqual(romannumbers.from_roman("XIX"),
                         (True, 19))
        self.assertEqual(romannumbers.from_roman("MXIX"),
                         (True, 1019))
        self.assertEqual(romannumbers.from_roman("MCMXCIX"),
                         (True, 1999))

        self.assertEqual(romannumbers.from_roman("MCCMXCIX")[0],
                         False)

    def test__to_roman(self):
        """
            Tests.test__to_roman()
            ____________________________________________________________________

            Test of the romannumbers/romannumbers.py::to_roman() function
            ____________________________________________________________________

            no PARAMETER, no RETURNED VALUE
        """
        self.assertEqual(romannumbers.to_roman(1),
                         (True, "I"))
        self.assertEqual(romannumbers.to_roman(1999),
                         (True, "MCMXCIX"))

        self.assertEqual(romannumbers.to_roman(0)[0],
                         False)
