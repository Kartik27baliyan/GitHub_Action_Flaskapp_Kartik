from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f"{self.id} {self.todo}"

def todo_serializer(todo):
    return {"id": todo.id, "todo": todo.todo}

@app.route("/", methods=["GET"])
def home():
    return jsonify([*map(todo_serializer, TodoList.query.all())])

@app.route("/todo-create", methods=["POST"])
def todo_create():
    request_data = json.loads(request.data)
    todo = TodoList(todo=request_data["todo"])
    db.session.add(todo)
    db.session.commit()
    return {"201": "todo created successfully"}

if __name__ == "__main__":
    app.run(debug=True)
