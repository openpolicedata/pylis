if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import compact

def test_get():
    x = compact.get()

    assert "ShortName" in x[0]

def test_get_details():
    short_name = 'compilation-of-compacts-and-related-records-and-reports'
    x = compact.get_details(short_name)

    assert x["ShortName"] == short_name