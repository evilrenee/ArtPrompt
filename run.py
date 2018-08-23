from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'character.db'

def fetchMenu(con):
    beings = []
    cur = con.execute('SELECT * FROM beings ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        beings.append(list(row))

    genders = []
    cur = con.execute('SELECT * FROM genders ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        genders.append(list(row))

    ages = []
    cur = con.execute('SELECT * FROM ages ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        ages.append(list(row))

    genres = []
    cur = con.execute('SELECT * FROM genres ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        genres.append(list(row))

    physiques = []
    cur = con.execute('SELECT * FROM physiques ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        physiques.append(list(row))

    features = []
    cur = con.execute('SELECT * FROM features ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        features.append(list(row))

    traits = []
    cur = con.execute('SELECT * FROM traits ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        traits.append(list(row))

    times = []
    cur = con.execute('SELECT * FROM times ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        times.append(list(row))

    mediums = []
    cur = con.execute('SELECT * FROM mediums ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        mediums.append(list(row))

    return {'beings':beings, 'genders':genders, 'ages':ages, 'genres':genres, 'physiques':physiques, 'features':features, 'traits':traits, 'times':times, 'mediums':mediums}

@app.route('/')
def index():
    return render_template ('roller.html', title='prompts')

@app.route('/iframe')
def iframe():
    con = sqlite3.connect(DATABASE)
    menu = fetchMenu(con)
    con.close()
    return render_template ('iframe.html', category='character', beings=menu['beings'], genders=menu['genders'], ages=menu['ages'], genres=menu['genres'], physiques=menu['physiques'], features=menu['features'], traits=menu['traits'], mediums=menu['mediums'], times=menu['times'])
