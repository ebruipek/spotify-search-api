import json
import unittest
import app 
from flask_restful.utils import http_status_message
from werkzeug.exceptions import HTTPException

class TestSpotifySearchApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_getting_tracks(self):
        resp = self.app.get(path='/tracks/{}'.format('rock'), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_genre_not_found(self):
        resp = self.app.get(path='/tracks/{}'.format('r'), content_type='application/json')
        self.assertEqual(resp.status_code, 404)

if __name__ == '__main__':
    unittest.main()