# Roman numbers    

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
` $ nosetests
or
` $ python -m unittest tests/tests.py
