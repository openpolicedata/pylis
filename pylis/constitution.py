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
    This service returns the list of Articles in the Constitution located here: law.lis.virginia.gov/constitution
    '''
    r = requests.get(
        f"{_url}/ConstitutionArticlesGetListOfJson", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)
    
def get_sections(article_number):
    '''
    This service returns the details of a given Constitution by 'articleNumber'
    '''
    r = requests.get(
        f"{_url}/ConstitutionSectionsGetListOfXml/{article_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)
        
def get_section_details(article_number, section_number):
    '''
    This service returns the details of a given Constitution by 'articleNumber' and 'sectionNumber'
    '''
    r = requests.get(
        f"{_url}/ConstitutionSectionDetailsJson/{article_number}/{section_number}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)