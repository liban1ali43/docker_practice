from flask import Flask
import MySQLdb
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    db = MySQLdb.connect(
        host="mydb",
        user="root",
        passwd=os.environ["DB_PASSWORD"],
        db="mysql"
    )
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, world! MySQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
