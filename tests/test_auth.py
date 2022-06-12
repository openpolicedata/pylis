if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import auth

def test_get():
    x = auth.get()

    assert "Name" in x[0]
    assert "ShortName" in x[0]

def test_get_details():
    short_name = 'alcohol-beverage-control-authority'
    x = auth.get_details(short_name)
    assert x["ShortName"] == short_name