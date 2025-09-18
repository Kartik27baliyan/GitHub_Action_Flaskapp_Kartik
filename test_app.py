import unittest
import json
from main import app, db, TodoList

class FlaskApiTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
        self.app = app.test_client()
        
        # Push application context for database operations
        self.app_context = app.app_context()
        self.app_context.push()
        
        db.create_all()
        self.create_test_data()

    def create_test_data(self):
        item1 = TodoList(todo="Test task 1")
        item2 = TodoList(todo="Test task 2")
        db.session.add(item1)
        db.session.add(item2)
        db.session.commit()

    def test_home_endpoint(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test task 1", response.data)

    def test_todo_creation(self):
        json_data = {"todo": "New test task"}
        response = self.app.post("/todo-create",
                               data=json.dumps(json_data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"201":"todo created successfully"}\n')

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        # Pop the application context
        self.app_context.pop()

if __name__ == "__main__":
    unittest.main()
