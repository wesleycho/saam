
def collections(self, **kwargs):

    from luce_credentials import username, password
    import requests
    from requests.auth import HTTPBasicAuth

    q = kwargs.get('q')
    rows = kwargs.get('rows')
    fq = kwargs.get('fq')
    start = kwargs.get('start')

    request_url = ['http://edan-api.si.edu/metadataService?applicationID=HACK&wt=json']

    if q is not None:
        request_url.append('&q={0}'.format(q))

    if rows is not None:
        request_url.append('&rows={0}'.format(rows))

    if fq is not None:
        request_url.append('&fq={0}'.format(fq))

    if start is not None:
        request_url.append('&start={0}'.format(start))

    
        
    return str(requests.get(''.join(request_url), auth=HTTPBasicAuth(username, password)).json())
