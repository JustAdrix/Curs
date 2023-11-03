from flask import Flask
from api import tasks

app = Flask(__name__)
app.register_blueprint(tasks.bp)

if __name__ == '__main__':
    app.run(debug=True)
