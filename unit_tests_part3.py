import unittest

class TestKeywordToTitles(unittest.TestCase):
    def test_normal_case1(self):
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

  
    def test_empty_metadata1(self):
        metadata = []
        expected_output = {}
        self.assertEqual(keyword_to_titles(metadata), expected_output)

    def test_no_keywords1(self):
      metadata = [
          (1, "Title1", "Author1", "2023", []),
          (2, "Title2", "Author2", "2023", []),
      ]
      expected_output = {}
      self.assertEqual(keyword_to_titles(metadata), expected_output)



    def test_normal_case2(self):
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


    
    def test_empty_metadata2(self):
        """Test the function with empty metadata input."""
        metadata = []
        expected = {}
        result = title_to_info(metadata)
        self.assertEqual(result, expected)

    def test_single_entry_metadata2(self):
        """Test the function with a single metadata entry."""
        metadata = [
            ["Article1", "Author1", "2024-11-19", 100]
        ]
        expected = {
            "Article1": {
                "author": "Author1",
                "timestamp": "2024-11-19",
                "length": 100
            }
        }
        result = title_to_info(metadata)
        self.assertEqual(result, expected)

    def test_multiple_entries_metadata2(self):
        """Test the function with multiple metadata entries."""
        metadata = [
            ["Article1", "Author1", "2024-11-19", 100],
            ["Article2", "Author2", "2024-11-18", 200],
            ["Article3", "Author3", "2024-11-17", 300]
        ]
        expected = {
            "Article1": {
                "author": "Author1",
                "timestamp": "2024-11-19",
                "length": 100
            },
            "Article2": {
                "author": "Author2",
                "timestamp": "2024-11-18",
                "length": 200
            },
            "Article3": {
                "author": "Author3",
                "timestamp": "2024-11-17",
                "length": 300
            }
        }
        result = title_to_info(metadata)
        self.assertEqual(result, expected)

    def test_incorrect_metadata_format2(self):
        """Test the function with improperly formatted metadata."""
        metadata = [
            ["Article1", "Author1", "2024-11-19"],  # Missing 'length'
            ["Article2"]  # Incomplete data
        ]
        with self.assertRaises(IndexError):
            title_to_info(metadata)

    def test_metadata_with_varied_lengths2(self):
        """Test the function with varying lengths in metadata."""
        metadata = [
            ["Article1", "Author1", "2024-11-19", 100],
            ["Article2", "Author2", "2024-11-18", 0]  # Length as zero
        ]
        expected = {
            "Article1": {
                "author": "Author1",
                "timestamp": "2024-11-19",
                "length": 100
            },
            "Article2": {
                "author": "Author2",
                "timestamp": "2024-11-18",
                "length": 0
            }
        }
        result = title_to_info(metadata)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

