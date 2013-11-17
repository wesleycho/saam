
def luce_zoom(self, **kwargs):

    score = int(kwargs.get('score', 0))
    artwork = kwargs.get('artwork', 'nothing_yet')
    oldname = kwargs.get('oldname')

    if artwork == 'correct':
        score += 1
    elif artwork == 'nope':
        score -= 1    

    import psycopg2
    import random

    from luce_database_credentials import database_connection_details as database_connection_details

    database_connection = psycopg2.connect(database_connection_details)
    database_cursor = database_connection.cursor()

    titles = []

    one_artwork_query = 'select id, title, image_url from sidebyside order by random() limit 1'
    database_cursor.execute(one_artwork_query)
    (art_id, art_realtitle, art_image) = database_cursor.fetchone()
   
    two_titles_query = 'select title from sidebyside where id != {0} order by random() limit 2'.format(art_id)
    database_cursor.execute(two_titles_query)

    for fake_title in database_cursor.fetchall():
        titles.append(fake_title[0])

    titles.append(art_realtitle)
    random.shuffle(titles)

    page_source = []

    with open('googleanalytics.txt') as header_file:
        page_source.append(header_file.read())

    page_source.append('<title>Identification game</title>')

    page_source.append('<link rel="stylesheet" type="text/css" href="/static/main.css"> <link rel="stylesheet" type="text/css" href="/static/gumby.css">')

    page_source.append('<div class="row"> <div class="ten columns" style="text-align: center;">')
    page_source.append('<h2>Hey what is the name of this artwork?</h2>')
    page_source.append('</div> </div>')

    page_source.append('\n\n<!-- HEY DON\'T CHEAT BY LOOKING AT THE SOURCE! :) -->\n\n')

    page_source.append('<div class="row"> <div class="centered ten columns"> <div class="row">')

    for title in titles:
        if title == art_realtitle:
            page_source.append('\n\n<div class="four columns" style="text-align: center;"><form method="post" action="luce_zoom"><input type="hidden" name="score" value="{0}"><input type="hidden" name="artwork" value="correct"><input style="white-space: normal;" type="submit" value="{1}"></form></div>'.format(score, title))
        else:
            page_source.append('\n\n<div class="four columns" style="text-align: center;"><form method="post" action="luce_zoom"><input type="hidden" name="score" value="{0}"><input type="hidden" name="oldname" value="{2}"><input type="hidden" name="artwork" value="nope"><input style="white-space: normal;" type="submit" value="{1}"></form></div>'.format(score, title, art_realtitle))
    page_source.append('</div> </div>')

    page_source.append('<table cellpadding=4 style="vertical-align: middle; text-align: center;"> <tr> <td>')
    page_source.append('\n\n<iframe src="http://ids.si.edu/ids/dynamic?id={0}&container.width=800&container.height=600" height=600 width=800 scrolling="no"></iframe>'.format(art_image))
    
    page_source.append('</td><td>')
    page_source.append('Your score: <b>{0}</b>'.format(score))

    if artwork == 'correct':
        page_source.append('&nbsp; <b> <br> <br> YOU JUST GOT A POINT <br> WAY TO IDENTIFY ART <br> LIKE A SUPERSTAR</b> <!-- <br> That is a haiku by the way :) :) :) :) :) :) ^ -->')
    elif artwork == 'nope':
        page_source.append('&nbsp; <b> <br> <br> That was incorrect <br> But it\'s a good chance to learn <br> Here\'s the correct name:</b><br> {0}'.format(oldname))

    page_source.append('<br> <br> <br> <br> <br> <br>')
    page_source.append('<form method="post" action="luce_zoom_score"><input type="hidden" name="score" value="{0}">Are you done playing? <br> You\'ll retire in glory. <br> Just enter your name.<br> &nbsp; <br> <input type="text" name="name" value="Enter your name"><input type="submit" value="End the game and retire in glory"></form>'.format(score))
    
    page_source.append('</td></tr></table>')
    page_source.append('</div>')                    
    
    return page_source
