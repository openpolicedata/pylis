if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import charter

def test_get():
    charter.get()

def test_get_details():
    assert 1 == 0