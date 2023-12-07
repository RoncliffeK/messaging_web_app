from flask import Flask, render_template
import pandas as pd
import sqlite3

app = Flask(__name__)

# Load messages from CSV into SQLite database
df = pd.read_csv('messages.csv')
conn = sqlite3.connect('db.sqlite')
df.to_sql('messages', conn, index=False, if_exists='replace')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agent_portal')
def agent_portal():
    # Fetch messages from the database
    messages = pd.read_sql('SELECT * FROM messages', conn)
    return render_template('agent_portal.html', messages=messages.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
