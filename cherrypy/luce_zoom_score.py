def luce_zoom_score(self, **kwargs):

    score = int(kwargs.get('score', -9999))
    name = kwargs.get('name', 'Art Enthusiast')

    if name == 'Enter your name':
        name = 'Art Enthusiast'

    import psycopg2

    from luce_database_credentials import database_connection_details as database_connection_details

    database_connection = psycopg2.connect(database_connection_details)
    database_cursor = database_connection.cursor()

    # Insert high score here.

    if name != 'Art Enthusiast' and score != -9999:
        insert_high_score_query = "insert into zoom_highscores (name, score) values ('{0}', {1})".format(name, score)
        database_cursor.execute(insert_high_score_query)
        database_connection.commit()

    high_score_query = "select name, score from zoom_highscores order by score desc limit 50"
    database_cursor.execute(high_score_query)

    score_table = []
    rank = 0
    for score in database_cursor.fetchall():
        rank += 1
        score_table.append('<tr> <td> {0} </td> <td> {1} </td> <td> {2} </td> </tr>'.format(rank, score[0], score[1]))

    page_source = []

    page_source.append('<title>High scores: Identification game</title>')

    page_source.append('<link rel="stylesheet" type="text/css" href="/static/main.css"> <link rel="stylesheet" type="text/css" href="/static/gumby.css">')

    page_source.append('<div class="row"> <div class="eight columns" style="text-align: center">')
    page_source.append('<h2>WALL OF CHAMPIONS</h2> <BR> Nice score you\'ve got there <BR> But it would be a real shame <br> If something happened <br> <a href="luce_zoom">Play again!</a> <br> &nbsp; <br> <table>')
    page_source.extend(score_table)
    page_source.append('</table> </div> </div>')

    return page_source

                        
        
    
