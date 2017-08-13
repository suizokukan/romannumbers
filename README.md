# Roman numbers, v. 0.0.1

Micro-library to convert Roman numbers from|to Arabic numbers.
  
# how to use the module :

` from romannumbers import romannumbers

` print(romannumbers.from_roman("XIX"))
... will print 19

` print(romannumbers.to_roman(1))
... will print "I"

` print(romannumbers.to_roman(100))
... will print "CIX"

# tests
Use check_the_code.sh to check code's quality and launch unittests.
    
` $ nosetests
or
` $ python -m unittest tests/tests.py
