from workout import app
from flask_testing import TestCase
from user import User
from flask_login import current_user, LoginManager, login_user
from werkzeug.security import generate_password_hash
import unittest


class MyTest(TestCase):

    def create_app(self):

        app.config['TESTING'] = True
        app.config['MONGO_URI'] = 'mongodb://'
        return app

    def setUp(self):
        self.client = app.test_client()
        pass

    def tearDown(self):
        pass

    # Tests if pages load correctly - user not authenticated

    def test_loading_index(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')

    def test_loading_register(self):
        response = self.client.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('register.html')

    def test_loading_login(self):
        response = self.client.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')

    def test_loading_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')

    def test_loading_groups(self):
        response = self.client.get('/muscle_groups', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')

    def test_loading_category(self):
        response = self.client.get('/<category>', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')

    def test_loading_my_exercises(self):
        response = self.client.get('/my_exercises', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')

    # Test Registration Form

    def test_username_too_short(self):
        """
        Test if error message gets displayed
        when username provided by user is too short
        """
        response = self.client.post('/register',
                                    data=dict(username='ab',
                                              password='abcde',
                                              password2='abcde',
                                              ))
        data = response.data.decode('utf-8')
        assert 'Field must be between 3 and 25 characters long' in data

    def test_password_too_short(self):
        """
        Test if error message gets displayed
        when password provided by user is too short
        """
        response = self.client.post('/register',
                                    data=dict(username='abcde',
                                              password='abc',
                                              password2='abc',
                                              ))
        data = response.data.decode('utf-8')
        assert 'Field must be between 5 and 50 characters long' in data

    def test_password_repeated(self):
        """
        Test if error message gets displayed
        when password is repeated incorrectly
        """
        response = self.client.post('/register',
                                    data=dict(username='abcde',
                                              password='abc',
                                              password2='xyz',
                                              ))
        data = response.data.decode('utf-8')
        assert 'Field must be equal to password' in data

    # Test Login Form

    def test_no_username(self):
        """
        Test if error message gets displayed
        when no username is provided by user at login
        """
        response = self.client.post('/login',
                                    data=dict(username='',
                                              password='abcde'
                                              ))
        data = response.data.decode('utf-8')
        assert 'Please enter a valid username' in data

    def test_no_password(self):
        """
        Test if error message gets displayed
        when no password is provided by user at login
        """
        response = self.client.post('/login',
                                    data=dict(username='abcde',
                                              password=''
                                              ))
        data = response.data.decode('utf-8')
        assert 'Please enter your password' in data

    # Test Password Hashing

    def test_password_hashing(self):
        u = User(username='abcde')
        password_hash = generate_password_hash('abcde')
        self.assertFalse(u.check_password(password_hash, 'vwxyz'))
        self.assertTrue(u.check_password(password_hash, 'abcde'))

    # Test Example Login

    def test_login(self):

        login_manager = LoginManager()
        login_manager.init_app(app)

        with app.test_request_context():

            # create and log in user
            currentUser = User(username='abcde')
            login_user(currentUser)

            # test that user was logged in
            assert current_user.is_active
            assert current_user.is_authenticated
            assert current_user == currentUser


if __name__ == '__main__':
    unittest.main()
