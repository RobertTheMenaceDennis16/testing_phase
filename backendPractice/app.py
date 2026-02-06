'''
I will be building a simple Flask application to learn from
This should give you an idea of how to set up a basic Flask app backend.

'''
#pip install Flask flask-sqlalchemy
# if you want to use a database, you can install flask-sqlalchemy
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)          # create a Flask app instance/ this creates your server
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # configure the database URI and name it
db = SQLAlchemy(app)            # create a SQLAlchemy object and pass the Flask app to it

class Todo(db.Model):      # create a model for the Todo items
    id = db.Column(db.Integer, primary_key=True)  # unique id for each todo item
    title = db.Column(db.String(100), nullable=False)  # title of the todo item

with app.app_context():  # create the database tables
    db.create_all()

################################################################################################
#serve the home page
@app.route('/')
def home():
    return render_template('index.html')
################################################################################################
#API to get all todo items
@app.route('/todos',methods=['GET'])
def get_todos():
    todos = Todo.query.all()  

    return jsonify([{'id': t.id, 'title': t.title} for t in todos])
################################################################################################
#API to add a new todo item
@app.route('/todos',methods=['POST'])
def create_todo():
    data = request.json()  
    new_todo = Todo(title=data['title'])
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message':"created"})
################################################################################################
#API to delete a todo item
@app.route('/todos/<int:id>',methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message':"deleted"})
################################################################################################
if __name__ == '__main__':
    app.run(debug=True)   # run the Flask app in debug mode