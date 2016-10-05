Byterun
=======

This is a pure-Python implementation of a Python bytecode execution virtual
machine.  I ([Ned Batchelder](https://github.com/nedbat)) started it to get a better understanding of bytecodes so I could
fix branch coverage bugs in coverage.py.

[![Build Status](https://travis-ci.org/djhenderson/byterun.svg?branch=master)](https://travis-ci.org/djhenderson/byterun)

For local unit tests:

	cygwin:

		$ python -m unittest discover  2>&1 > t27.log

		$ python3 -m unittest discover  2>&1 > t34.log

	windows:

		+py27 ; python -m unittest discover  > tw27.log

		+py34 ; python -m unittest discover  > tw34.log

		+py35 ; python -m unittest discover  > tw35.log

		+py36 ; python -m unittest discover  > tw36.log
