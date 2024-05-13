import unittest
import requests


class TestCatFactsAPI(unittest.TestCase):
    base_url = "https://cat-fact.herokuapp.com"

    def test_retrieving_cat_fact(self):
        response = requests.get(f"{self.base_url}/facts")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertTrue(len(data) > 0)

    def test_retrieving_cat_facts_correct_type(self):
        response = requests.get(f"{self.base_url}/facts")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertTrue(all(fact['type'] == 'cat' for fact in data))


if __name__ == '__main__':
    unittest.main()
