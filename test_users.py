import unittest
from unittest.mock import patch, Mock
from users import fetch_user_data, BASE_URL, headers

class TestFetchUserData(unittest.TestCase):
    @patch('users.requests.get')
    def test_successful_fetch(self, mock_get):
        expected_data = {'data': {'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}, 'support': {'url': 'https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral', 'text': 'Tired of writing endless social media content? Let Content Caddy generate it for you.'}}

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        result = fetch_user_data(7)

        self.assertEqual(result, expected_data)
        
        url = f"{BASE_URL}7"

        mock_get.assert_called_once_with(url, headers=headers)

    @patch('users.requests.get')
    def test_user_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        url = f"{BASE_URL}786"

        with self.assertRaises(ValueError):
            fetch_user_data(786)
        
        mock_get.assert_called_once_with(url, headers=headers)
        
if __name__ == '__main__':
    unittest.main()