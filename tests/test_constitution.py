if __name__ == "__main__":
	import sys
	sys.path.append('../pylis')
from pylis import constitution

def test_get():
    x = constitution.get()

    assert "ArticleNumber" in x[0]

def test_get_sections():
    article_num = 1
    x = constitution.get_sections(article_num)

    assert x["ArticleNumber"] == str(article_num)
        
def test_get_section_details():
    article_num = 1
    section_num = 2
    x = constitution.get_section_details(article_num, section_num)

    assert x["ArticleNumber"] == str(article_num)
    assert x["Sections"][0]["SectionNumber"] == str(section_num)