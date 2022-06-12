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
    This service returns a list of the Administratve Titles located here: law.lis.virginia.gov/admincode
    '''
    r = requests.get(
        f"{_url}/AdministrativeCodeGetTitleListOfJson", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_agencies(title_number):
    '''
    This service returns a list of the Administratve Agencies by 'titleNumber'
    '''
    r = requests.get(
        f"{_url}/AdministrativeCodeGetAgencyListOfJson/{title_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_chapters(title_number, agency_number):
    '''
    This service returns a list of the Administratve Chapters by 'titleNumber' and 'agencyNumber'
    '''
    r = requests.get(
        f"{_url}/AdministrativeCodeChapterListOfJson/{title_number}/{agency_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_sections(title_number, agency_number, chapter_number):
    '''
    This service returns a list of the Administratve Sections by 'titleNumber', 'agencyNumber' and 'chapterNumber'
    '''
    r = requests.get(
        f"{_url}/AdministrativeCodeGetSectionListOfJson/{title_number}/{agency_number}/{chapter_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_section_details(title_number, agency_number, chapter_number,section_number,section_number_point=0,section_number_colon=0):
    '''
    This service returns the Administratve Section detail by 'titleNumber', 'agencyNumber', 'chapterNumber', 
    'sectionNumber', 'sectionNumberPoint', 'sectionNumberColon' (if no point or colon, pass a 0 for each value)
    '''
    r = requests.get(
        f"{_url}/AdministrativeCodeGetSectionDetailsJson/{title_number}/{agency_number}/{chapter_number}/{section_number}/{section_number_point}/{section_number_colon}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)