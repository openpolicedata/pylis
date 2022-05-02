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
    This service returns a list of the Charters located here: law.lis.virginia.gov/charters
    '''
    r = requests.get(
        f"{_url}/ChartersGetListOfJson", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)

def get_details(short_name):
    '''
    This service returns the details of a given Charter by 'shortName'
    '''
    r = requests.get(
        f"{_url}/ChartersGetDetailJson/{short_name}", 
        verify=_path_to_cert, 
        headers=_headers)
    return json.loads(r.text)