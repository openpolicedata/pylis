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

def get_chapters(year):
    '''
    This service returns the list of chapters in the Uncodified Acts by 'year' located here: law.lis.virginia.gov/uncodifiedacts
    '''
    r = requests.get(
        f"{_url}/UncodifiedActChapterByYearGetListOfJson/{year}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)
    
def get_chapters_sorted_by_subject(year):
    '''
    This service returns the list of chapters sorted by subject in the Uncodified Acts by 'year'
    '''
    r = requests.get(
        f"{_url}/UncodifiedActChapterBySubjectGetListOfJson/{year}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)
        
def get_chapter_details(year, session, chapter):
    '''
    This service returns the details of a chapter in the Uncodified Acts by 'year', 'session' and 'chapter'
    '''
    r = requests.get(
        f"{_url}/UncodifiedActSectionGetSectionDetailsJson/{year}/{session}/{chapter}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)