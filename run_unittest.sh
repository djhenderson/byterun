:
# script to run unittest

# work around differendes in unittest between python versions

python -c 'from __future__ import print_function
import pip
import six
import tox
print("INFO: pip (%s)" % pip.__version__)
print("INFO: six (%s)" % six.__version__)
print("INFO: tox (%s)" % tox.__version__)
'

PYVERSION=$(python -c "from __future__ import print_function; import sys; print('%d_%d'%sys.version_info[:2])")

echo "INFO: PYVERSION=${PYVERSION}"

# python -m unittest -h

case ${PYVERSION} in
2_7|3_3|3_4|3_5|3_6)
	echo "INFO: python -m unittest discover -b"
	python -m unittest discover -b
	;;
2_6)
	echo "INFO: python -m unittest"
	python -m unittest
	;;
2_5|3_0|3_1)
	echo "INFO: not installed on Travis-CI"
	;;
*)
	echo "WARNING: $0 is not configured for Python version ${PYVERSION}"
	;;
esac

#
