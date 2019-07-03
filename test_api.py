import json
import unittest
from run import app

class TestSpotifySearchApp(unnittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_getting_tracks(self):
        resp = self.client.get(path='/tracks/{}'.format('rock'), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_genre_not_found(self):
        resp = self.client.get(path='/tracks/{}'.format('r'), content_type='application/json')
        self.assertEqual(resp.status_code, 404)

if __name__ == '__main__':
    unnittest.main()