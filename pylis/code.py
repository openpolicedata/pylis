import requests
import json

if __name__ == '__main__':
    from defs import _url
    from defs import _path_to_cert
    from defs import _headers
else:
    from .defs import _url
    from .defs import _path_to_cert
    from .defs import _headers

def get():
    '''
    This service returns a list of Titles in the Code of Virginia located here: law.lis.virginia.gov/vacode
    '''
    r = requests.get(
        f"{_url}/CoVTitlesGetListOfJson", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_chapters(title_number):
    '''
    This service returns a list of the Chapters in the Code of Virginia by 'titleNumber'
    '''
    r = requests.get(
        f"{_url}/CoVChaptersGetListOfJson/{title_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_sections(title_number, chapter_number):
    '''
    This service returns a list of the Sections in the Code of Virginia by 'titleNumber' and 'chapterNumber'
    '''
    r = requests.get(
        f"{_url}/CoVSectionsGetListOfJson/{title_number}/{chapter_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_section_details(section_number):
    '''
    This service returns the Section detail in the Code of Virginia by 'sectionNumber'
    '''
    r = requests.get(
        f"{_url}/CoVSectionsGetSectionDetailsJson/{section_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)