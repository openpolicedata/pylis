if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import charter

def test_get():
    x = charter.get()

    assert "Name" in x[0]
    assert "Type" in x[0]

def test_get_details():
    short_name = "chesterfield"
    x = charter.get_details(short_name)

    assert x["ShortName"] == short_name