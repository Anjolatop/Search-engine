import unittest

class TestKeywordToTitles(unittest.TestCase):
    def test_normal_case(self):
        metadata = [
            (1, "Title1", "Author1", "2023", ["keyword1", "keyword2"]),
            (2, "Title2", "Author2", "2023", ["keyword2", "keyword3"]),
            (3, "Title3", "Author3", "2023", ["keyword1", "keyword3", "keyword4"]),
        ]
        expected_output = {
            "keyword1": [1, 3],
            "keyword2": [1, 2],
            "keyword3": [2, 3],
            "keyword4": [3],
        }
        self.assertEqual(keyword_to_titles(metadata), expected_output)

  
    def test_empty_metadata(self):
        metadata = []
        expected_output = {}
        self.assertEqual(keyword_to_titles(metadata), expected_output)

    def test_no_keywords(self):
      metadata = [
          (1, "Title1", "Author1", "2023", []),
          (2, "Title2", "Author2", "2023", []),
      ]
      expected_output = {}
      self.assertEqual(keyword_to_titles(metadata), expected_output)



    def test_normal_case(self):
        metadata = [
            ("Title1", "Author1", "2023-01-01", 500),
            ("Title2", "Author2", "2023-01-02", 1000),
            ("Title3", "Author3", "2023-01-03", 750),
        ]
        expected_output = {
            "Title1": {"author": "Author1", "timestamp": "2023-01-01", "length": 500},
            "Title2": {"author": "Author2", "timestamp": "2023-01-02", "length": 1000},
            "Title3": {"author": "Author3", "timestamp": "2023-01-03", "length": 750},
        }
        self.assertEqual(title_to_info(metadata), expected_output)
