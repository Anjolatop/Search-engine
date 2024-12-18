from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

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

    def test_keyword_found3(self):
        """Test when the keyword is found in the dictionary."""
        keyword_to_titles = {
            "science": ["Article1", "Article2"],
            "technology": ["Article3"]
        }
        keyword = "science"
        expected = ["Article1", "Article2"]
        result = search(keyword, keyword_to_titles)
        self.assertEqual(result, expected)

    def test_keyword_not_found3(self):
        "Test when the keyword is not in the dictionary."
        keyword_to_titles = {
            "science": ["Article1", "Article2"],
            "technology": ["Article3"]
        }
        keyword = "art"
        expected = []
        result = search(keyword, keyword_to_titles)
        self.assertEqual(result, expected)

    def test_empty_dictionary3(self):
        """Test when the dictionary is empty."""
        keyword_to_titles = {}
        keyword = "science"
        expected = []
        result = search(keyword, keyword_to_titles)
        self.assertEqual(result, expected)

    def test_articles_within_max_length4(self):
        """Test when some articles have lengths less than or equal to max_length."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"length": 100},
            "Article2": {"length": 200},
            "Article3": {"length": 300},
        }
        max_length = 200
        expected = ["Article1", "Article2"]
        result = article_length(max_length, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_no_articles_within_max_length4(self):
        """Test when no articles have lengths less than or equal to max_length."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"length": 400},
            "Article2": {"length": 500},
            "Article3": {"length": 600},
        }
        max_length = 300
        expected = []
        result = article_length(max_length, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_all_articles_within_max_length4(self):
        """Test when all articles have lengths less than or equal to max_length."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"length": 50},
            "Article2": {"length": 100},
            "Article3": {"length": 150},
        }
        max_length = 200
        expected = ["Article1", "Article2", "Article3"]
        result = article_length(max_length, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_multiple_authors5(self):
        """Test when multiple authors are associated with different articles."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"author": "Author1"},
            "Article2": {"author": "Author2"},
            "Article3": {"author": "Author1"},
        }
        expected = {
            "Author1": ["Article1", "Article3"],
            "Author2": ["Article2"]
        }
        result = key_by_author(article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_single_author5(self):
        """Test when all articles are written by the same author."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"author": "Author1"},
            "Article2": {"author": "Author1"},
            "Article3": {"author": "Author1"},
        }
        expected = {
            "Author1": ["Article1", "Article2", "Article3"]
        }
        result = key_by_author(article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_no_articles5(self):
        """Test when there are no articles to process."""
        article_titles = []
        title_to_info = {}
        expected = {}
        result = key_by_author(article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_author_found6(self):
        """Test when the specified author has written some of the articles."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"author": "Author1"},
            "Article2": {"author": "Author2"},
            "Article3": {"author": "Author1"},
        }
        author = "Author1"
        expected = ["Article1", "Article3"]
        result = filter_to_author(author, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_author_not_found6(self):
        """Test when the specified author has written none of the articles."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"author": "Author1"},
            "Article2": {"author": "Author2"},
            "Article3": {"author": "Author3"},
        }
        author = "Author4"
        expected = []
        result = filter_to_author(author, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_author_with_case_and_whitespace_variations6(self):
        """Test when the author's name has case or leading/trailing whitespace differences."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"author": "Author1"},
            "Article2": {"author": "Author2"},
            "Article3": {"author": "Author1"},
        }
        author = "  author1  "  # Case and whitespace variation
        expected = ["Article1", "Article3"]
        result = filter_to_author(author, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_keyword_found7(self):
        """Test when the keyword is found, and some articles are associated with it."""
        article_titles = ["Article1", "Article2", "Article3", "Article4"]
        keyword_to_titles = {
            "science": ["Article1", "Article3"],
            "technology": ["Article2"]
        }
        keyword = "science"
        expected = ["Article2", "Article4"]  # Articles not associated with "science"
        result = filter_out(keyword, article_titles, keyword_to_titles)
        self.assertEqual(result, expected)

    def test_keyword_not_found(self):
        """Test when the keyword is not found, so all articles are returned."""
        article_titles = ["Article1", "Article2", "Article3", "Article4"]
        keyword_to_titles = {
            "science": ["Article1", "Article3"],
            "technology": ["Article2"]
        }
        keyword = "art"
        expected = ["Article1", "Article2", "Article3", "Article4"]  # No filtering
        result = filter_out(keyword, article_titles, keyword_to_titles)
        self.assertEqual(result, expected)

    def test_no_articles_with_keyword7(self):
        """Test when there are no articles with the specified keyword."""
        article_titles = ["Article1", "Article2", "Article3"]
        keyword_to_titles = {
            "science": []
        }
        keyword = "science"
        expected = ["Article1", "Article2", "Article3"]  # No articles to filter out
        result = filter_out(keyword, article_titles, keyword_to_titles)
        self.assertEqual(result, expected)

    def test_articles_from_specific_year8(self):
        """Test when articles from a specific year are returned correctly."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"timestamp": 1609567200},  # Jan 2, 2021
            "Article2": {"timestamp": 1612137600},  # Feb 1, 2021
            "Article3": {"timestamp": 1622505600},  # Jun 1, 2021
        }
        year = 2021
        expected = ["Article1", "Article2", "Article3"]
        result = articles_from_year(year, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_articles_from_different_year8(self):
        """Test when articles from a different year are returned correctly."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"timestamp": 1609567200},  # Jan 2, 2021
            "Article2": {"timestamp": 1612137600},  # Feb 1, 2021
            "Article3": {"timestamp": 1577944800},  # Jan 2, 2020
        }
        year = 2020
        expected = ["Article3"]
        result = articles_from_year(year, article_titles, title_to_info)
        self.assertEqual(result, expected)

    def test_no_articles_from_year8(self):
        """Test when no articles are from the specified year."""
        article_titles = ["Article1", "Article2", "Article3"]
        title_to_info = {
            "Article1": {"timestamp": 1609567200},  # Jan 2, 2021
            "Article2": {"timestamp": 1612137600},  # Feb 1, 2021
            "Article3": {"timestamp": 1614556800},  # Mar 1, 2021
        }
        year = 2020
        expected = []  # No articles from 2020
        result = articles_from_year(year, article_titles, title_to_info)
        self.assertEqual(result, expected)
# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
