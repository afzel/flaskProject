from flask import Flask, jsonify, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=True)

cpu = [
  { 'cpu': "5.2 %" }
]



@app.route('/')
def get_cpu():
  return jsonify(cpu)


@app.route('/', methods=['POST'])
def add_cpu():
  cpu.append(request.get_json())
  return '', 204

if __name__ == '__main__':
    app.run()