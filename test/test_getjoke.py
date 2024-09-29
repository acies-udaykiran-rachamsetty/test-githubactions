import unittest
from unittest.mock import patch, Mock
from src.customexception import RandomException
import requests
from src.getjoke import get_joke, fetch_joke, transform_joke

class TestJokeAPI(unittest.TestCase):

    def test_fetch_joke_success(self):
        with patch('src.getjoke.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = [{
                'setup': 'Where do APIs go to eat?',
                'punchline': 'To the RESTaurant.',
                'id': 123
            }]
            mock_get.return_value = mock_response

            joke = fetch_joke()

            self.assertIsNotNone(joke)
            self.assertEqual(joke['setup'], 'Where do APIs go to eat?')
            self.assertEqual(joke['punchline'], 'To the RESTaurant.')

    def test_fetch_joke_failure(self):
        with patch('src.getjoke.requests.get') as mock_get:
            mock_get.side_effect = requests.RequestException("API failure")

            with self.assertRaises(RandomException) as context:
                fetch_joke()

            self.assertIn("API failure", str(context.exception))


    def test_get_joke(self):
        with patch('src.getjoke.fetch_joke') as mock_fetch_joke, \
            patch('src.getjoke.transform_joke') as mock_transform_joke:
            
            mock_fetch_joke.return_value = {
                'setup': "Why don't programmers like nature?",
                'punchline': "It has too many bugs."
            }
            
            mock_transform_joke.return_value = "Setup: Why don't programmers like nature? | Punchline: It has too many bugs."

            joke = get_joke()

            self.assertEqual(joke, "Setup: Why don't programmers like nature? | Punchline: It has too many bugs.")


if __name__ == '__main__':
    unittest.main()
