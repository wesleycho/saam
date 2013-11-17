
def luce_zoom(self, **kwargs):

    score = int(kwargs.get('score', 0))
    artwork = kwargs.get('artwork', 'nothing_yet')

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

    page_source.append('<title>Identification game</title>')

    page_source.append('<link rel="stylesheet" type="text/css" href="/static/main.css"> <link rel="stylesheet" type="text/css" href="/static/gumby.css">')

    page_source.append('<h2>Hey what is the name of this artwork?</h2>')

    page_source.append('Your score: <b>{0}</b>'.format(score))

    page_source.append('<form method="post" action="luce_zoom_score"><input type="hidden" name="score" value="{0}"><input type="text" name="name" value="Enter your name"><input type="submit" value="End the game and retire in glory"></form><hr>'.format(score))

    if artwork == 'correct':
        page_source.append('&nbsp; <b> YOU JUST GOT A POINT / WAY TO IDENTIFY ART / LIKE A SUPERSTAR</b> <br> That is a haiku by the way :) :) :) :) :) :) ^')

    page_source.append('\n\n<!-- HEY DON\'T CHEAT BY LOOKING AT THE SOURCE! :) -->\n\n')

    for title in titles:
        if title == art_realtitle:
            page_source.append('\n\n<form method="post" action="luce_zoom"><input type="hidden" name="score" value="{0}"><input type="hidden" name="artwork" value="correct"><input type="submit" value="{1}"></form>'.format(score, title))
        else:
            page_source.append('\n\n<form method="post" action="luce_zoom"><input type="hidden" name="score" value="{0}"><input type="hidden" name="artwork" value="nope"><input type="submit" value="{1}"></form>'.format(score, title))

    page_source.append('\n\n<iframe src="http://ids.si.edu/ids/dynamic?id={0}&container.width=1500&container.height=1500" height=2000 width=2000></iframe>'.format(art_image))
        
    return page_source
