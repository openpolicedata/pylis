if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import admin

def test_get():
    admins = admin.get()
    assert "TitleNumber" in admins[0]
    assert "TitleName" in admins[0]
    assert "AgencyList" in admins[0]

def test_get_agencies():
    title_num = 1
    agencies = admin.get_agencies(title_num)
    assert agencies["TitleNumber"] == str(title_num)

def test_get_chapters():
    title_num = 1
    agency_num = 17
    chapters = admin.get_chapters(title_num, agency_num)

    assert chapters["TitleNumber"] == str(title_num)
    assert chapters["AgencyList"][0]["AgencyNumber"] == str(agency_num)

def test_get_sections():
    title_num = 1
    agency_num = 17
    chapter_num = 10
    x = admin.get_sections(title_num, agency_num, chapter_num)

    assert x["TitleNumber"] == str(title_num)
    assert x["AgencyList"][0]["AgencyNumber"] == str(agency_num)
    assert x["AgencyList"][0]["ChapterList"][0]["ChapterNumber"] == str(chapter_num)

def test_get_section_details():
    title_num = 1
    agency_num = 17
    chapter_num = 11
    section_num = 10
    x = admin.get_section_details(title_num, agency_num, chapter_num, section_num)

    assert x["TitleNumber"] == str(title_num)
    assert x["AgencyList"][0]["AgencyNumber"] == str(agency_num)
    assert x["AgencyList"][0]["ChapterList"][0]["ChapterNumber"] == str(chapter_num)
    assert x["AgencyList"][0]["ChapterList"][0]["Sections"][0]["SectionNumber"] == str(section_num)
