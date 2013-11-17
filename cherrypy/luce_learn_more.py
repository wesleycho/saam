def luce_learn_more(self, **kwargs):

    import random
    import requests

    from luce_credentials import username, password
    from requests.auth import HTTPBasicAuth

    art_ids = [0, 1]
    art_ids[0] = kwargs.get('id1')
    art_ids[1] = kwargs.get('id2')

    for index, art_id in enumerate(art_ids):
        if art_id is None:
            art_ids[index] = random.randint(1,31114) # Luce has this many images

    page_source = []

    page_source.append('<title>Learn about these artworks</title>')
    page_source.append('<link rel="stylesheet" type="text/css" href="/static/main.css"> <link rel="stylesheet" type="text/css" href="/static/gumby.css">\n\n')

    with open('addthis_button.txt') as addthisbutton_file:
        page_source.append(addthisbutton_file.read())

    page_source.append('\n\n<div class="row"> <div class="ten columns" style="text-align: center;"> <h2> Learn more! </h2></div> </div>')

    for art_id in art_ids:

        request_url = 'http://edan-api.si.edu/metadataService?applicationID=HACK&rows=1&start={0}&wt=json&fq=online_media_type:Images'.format(art_id)
        response = requests.get(request_url, auth=HTTPBasicAuth(username, password)).json()

        title = response['response']['docs'][0]['descriptiveNonRepeating']['title']['content']
        image = response['response']['docs'][0]['descriptiveNonRepeating']['online_media']['media'][0]['content']
        url = response['response']['docs'][0]['descriptiveNonRepeating']['record_link']

        try:
            data_source = response['response']['docs'][0]['freetext']['dataSource'][0]['content']
            artist_name = response['response']['docs'][0]['freetext']['name'][0]['content']
            object_type = response['response']['docs'][0]['freetext']['objectType'][0]['content']
            phys_desc = response['response']['docs'][0]['freetext']['physicalDescription'][0]['content']
            date = response['response']['docs'][0]['freetext']['date'][0]['content']

        except Exception:

            pass

        page_source.append('<div class="row">')
        page_source.append('<div class="six columns" style="text-align: center"><a href="{0}" target="_blank"><img src="{1}"></a></div>'.format(url, image))

        page_source.append('<div class="six columns" style="text-align: center"> <table cellpadding=4 style="text-align: center; vertical-align: middle;">')

        page_source.append('<tr> <td colspan=2> <h3>{0} </h3> </td> </tr>'.format(title))
        
        page_source.append('<tr> <td>Artist: </td> <td> {0} </td> </tr>'.format(artist_name))
        page_source.append('<tr> <td>Date: </td> <td> {0} </td> </tr>'.format(date))
        page_source.append('<tr> <td>Source: </td> <td> {0} </td> </tr>'.format(data_source))
        page_source.append('<tr> <td>Type: </td> <td> {0} </td> </tr>'.format(object_type))
        page_source.append('<tr> <td>Description: </td> <td> {0} </td> </tr>'.format(phys_desc))

        page_source.append('</table> </div> </div>')

    page_source.append('<div class="row"> <div class="ten columns" style="text-align: center;">  <h4> Click on an image to open up the full details </h4> </div> </div>')

    return page_source
        
