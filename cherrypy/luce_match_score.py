
def luce_match_score(self, **kwargs):

    import psycopg2

    from luce_database_credentials import database_connection_details as database_connection_details

    database_connection = psycopg2.connect(database_connection_details)
    database_cursor = database_connection.cursor()

    select_query = 'select image_id, image_url, title, count(id) from sidebyside group by image_id, image_url, title order by count(id) desc'

    database_cursor.execute(select_query)

    score_table = []
    score_table.append('<table> <tr> <td> Rank </td> <td> Image </td> <td> Title </td> <td> Votes </td>')
    rank = 0
    for row in database_cursor.fetchall():
        rank += 1
        score_table.append('<tr> <td>#{0}</td> <td><img src="{1}" alt="{2}"></td> <td>{2}</td> <td><b>{3}</b></td> </tr>'.format(rank, row[1], row[2], row[3]))

    page_source = []
    
    page_source.append('<title>Favorite artworks</title>')
        
    page_source.append('<link rel="stylesheet" type="text/css" href="/static/main.css"> <link rel="stylesheet" type="text/css" href="/static/gumby.css">')
    page_source.append('<div class="row"> <div class="ten columns" style="text-align: center;"> <br> <a href="luce_match">Play again!</a> <br> <h2> Favorite Artworks </h2> </div> </div> ')

    page_source.append('<div class="row">')
    page_source.extend(score_table)
    page_source.append('</div>')
    
    return page_source
