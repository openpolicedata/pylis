if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import uncodified_acts

def test_get_chapters():
    uncodified_acts.get_chapters(2020)
    
def test_get_chapters_sorted_by_subject(year):
    uncodified_acts.get_chapters_sorted_by_subject(year)
        
def test_get_chapter_details():
    assert 1==0