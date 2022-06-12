if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import uncodified_acts

def test_get_chapters():
    year = 2020
    x = uncodified_acts.get_chapters(year)

    # Year is null so can't compare
    assert "Chapter" in x
    
def test_get_chapters_sorted_by_subject():
    year = 2020
    x = uncodified_acts.get_chapters_sorted_by_subject(year)

    assert x[0]["Year"] == str(year)
    assert "Subject" in x[0]
        
def test_get_chapter_details():
    year = 2020
    session = 1
    chapter = 110
    x = uncodified_acts.get_chapter_details(year, session, chapter)

    assert x["Year"] == str(year)
    assert x["Session"] == str(session)
    assert x["Chapter"] == str(chapter)