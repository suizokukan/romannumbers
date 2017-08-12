echo "================================================================================"
echo "nosetests :"
nosetests

echo "================================================================================"
echo "flake8 all .py files :"
flake8 romannumbers/romannumbers.py
flake8 tests/tests.py
flake8 example.py

echo "================================================================================"
echo "pylint all .py files :"
pylint romannumbers/romannumbers.py
pylint tests/tests.py
pylint example.py

echo "... end"

