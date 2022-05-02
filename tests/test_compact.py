if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import compact

def test_get():
    compact.get()

def test_get_details():
    assert 1 == 0