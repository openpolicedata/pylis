if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import auth

def test_get():
    auth.get()

def test_get_details():
    assert 1 == 0