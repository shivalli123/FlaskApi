import unittest
from unittest.mock import patch, MagicMock
from productscrape import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('requests.get')
    def test_get_product_details_success(self, mock_get):
        # test response for the first URL
        test_response1 = MagicMock()
        test_response1.status_code = 200
        test_response1.json.return_value = {
            "contents": [
                {
                    "mainContent": [
                        {
                            "contents": [
                                {
                                    "records": [
                                        {
                                            "attributes": {
                                                "product.displayName": "Nulux Reflective High-Rise Track Tight 25\"",
                                                "product.allAvailableSizes": ["10"]
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        # Configure mock_get side effect
        mock_get.return_value = test_response1

        # Make a request to the endpoint
        response = self.app.get('/get_product_details')

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains two product details
        expected_data = [
            {'product_display_name': 'Nulux Reflective High-Rise Track Tight 25\"',
             'sizes_available': ["10"]}
        ]
        self.assertEqual(len(response.json), 1)  # Check length of response
        self.assertEqual(response.json, expected_data)

    @patch('requests.get')
    def test_error_handling(self, mock_get):
        # test response for the first URL
        test_response1 = MagicMock()
        test_response1.status_code = 500

        # Configure mock_get side effect
        mock_get.return_value = test_response1

        # Make a request to the endpoint
        response = self.app.get('/get_product_details')

        # Check if the response status code is 500
        self.assertEqual(response.status_code, 500)

        # Check if the response contains the error message
        expected_data = {'error': 'Failed to fetch data from Lululemon API'}
        self.assertEqual(response.json, expected_data)

if __name__ == '__main__':
    unittest.main()
