from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
return render_template('index.html',)
