if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')

from pylis import code

def test_get():
    x = code.get()

    assert "TitleNumber" in x[0]
    assert "TitleName" in x[0]

def test_get_chapters():
    title_number = 42.1
    x = code.get_chapters(title_number)

    assert x["TitleNumber"] == str(title_number)

def test_get_sections():
    title_number = 42.1
    chapter_num = 1
    x = code.get_sections(title_number, chapter_num)

    assert x["TitleNumber"] == str(title_number)
    assert x["ChapterNum"] == str(chapter_num)

def test_get_section_details():
    section_number = "42.1-11"
    x = code.get_section_details(section_number)

    assert x["ChapterList"][0]["SectionNumber"] == section_number
  