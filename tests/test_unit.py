from flask_testing import TestCase
from application import app, db
from application.model import Note
from flask import url_for


class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        tasks = Note( description='new task')
        db.session.add(tasks)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)

    def test_about_get(self):
        response = self.client.get(url_for("about"))
        self.assert200(response)

    def test_login_get(self):
        response = self.client.get(url_for("login"))
        self.assert200(response)

    def test_register_get(self):
        response = self.client.get(url_for("sign_up"))
        self.assert200(response)

    def test_register_get(self):
        response = self.client.get(url_for("logout"))
        self.assert200(response)

    
    def test_create_team_get(self):
        response = self.client.get(url_for("creat_task"))
        self.assert200(response)

class TestRead(TestBase):
    def test_read_home_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"new task", response.data)

    def test_read_(self):
        response = self.client.get(url_for("about"))
        self.assertIn(b"about", response.data)

class TestCreate(TestBase):
    
    def test_create_user(self):
        response = self.client.post(
            url_for("creat-task"),
            json={"description":'new new task'},
            follow_redirects=True)
        new_task = Note.query.get(2)
        self.assertEqual("new new task", new_task.description)   