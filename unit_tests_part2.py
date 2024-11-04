from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    def test_search(self):
        self.assertEqual(search(''), [])
        self.assertEqual(search('anjola'), [])
        expected_result = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('SOCCER'), expected_result)
        self.assertEqual(search(' soccer '), expected_result)
    
    def test_article_length(self):
        metadata = [
            ['History of Soccer', 'David Beckham', 1234567890, 100],
            ['Football Rules and Regulations', 'Pelé', 1234567891, 200]
        ]
        max_length = 100
        self.assertEqual(article_length(max_length, metadata), [['History of Soccer', 'David Beckham', 1234567890, 100]])
        metadata = [
            ['The Comprehensive Guide to Football Tactics', 'Alex Ferguson', 1234567890, 100],
            ['Football Rules and Regulations', 'Johan Cruyff', 1234567891, 200]
        ]
        max_length = 50
        self.assertEqual(article_length(max_length, metadata), [])
        metadata = [
            ['History of Soccer', 'David Beckham', 1234567890, 100],
            ['Football Rules', 'Pelé', 1234567891, 200]
        ]
        max_length = 400
        self.assertEqual(article_length(max_length, metadata), metadata)

    def test_unique_authors(self):
        metadata = [
            ['History of Soccer', 'David Beckham', 1234567890, 100],
            ['Football Rules and Regulations', 'Pelé', 1234567891, 200],
            ['Soccer in the Modern Era', 'David Beckham', 1234567892, 300]
        ]
        self.assertEqual(unique_authors(5, metadata), [metadata[0], metadata[1]])
        metadata = [
            ['History of Soccer', 'David Beckham', 1234567890, 100],
            ['Football Strategy', 'Johan Cruyff', 1234567891, 200],
            ['Soccer Legends', 'Pelé', 1234567892, 300]
        ]
        self.assertEqual(unique_authors(2, metadata), [metadata[0], metadata[1]])
        metadata = [
            ['History of Soccer', 'David Beckham', 1234567890, 100],
            ['Soccer Techniques', 'david beckham', 1234567891, 200]
        ]
        self.assertEqual(unique_authors(2, metadata), [metadata[0]])

    def test_most_recent_article(self):
        metadata = [['Evolution of Football Tactics', 'Alex Ferguson', 1234567890, 1500]]
        self.assertEqual(most_recent_article(metadata), metadata[0])
        metadata = [
            ['History of the World Cup', 'Pelé', 1234567890, 2000],
            ['Modern Soccer Techniques', 'Cristiano Ronaldo', 1234567895, 1800],
            ['The Rise of Women’s Soccer', 'Marta Vieira', 1234567800, 2100]
        ]
        self.assertEqual(most_recent_article(metadata), metadata[1])
        metadata = [
            ['The Art of Defending', 'Paolo Maldini', 1234567890, 1600],
            ['Goalkeeping Mastery', 'Manuel Neuer', 1234567890, 1700]
        ]
        self.assertEqual(most_recent_article(metadata), metadata[0])

    def test_favorite_author(self):
        metadata = [
            ['The Evolution of Soccer', 'Lionel Messi', 1234567890, 1500],
            ['Mastering Free Kicks', 'David Beckham', 1234567891, 2000]
        ]
        self.assertEqual(favorite_author('David Beckham', metadata), True)
        metadata = [
            ['The Evolution of Soccer', 'Lionel Messi', 1234567890, 1500],
            ['Mastering Free Kicks', 'David Beckham', 1234567891, 2000]
        ]
        self.assertEqual(favorite_author('Cristiano Ronaldo', metadata), False)
        metadata = [
            ['The Evolution of Soccer', 'Lionel Messi', 1234567890, 1500],
            ['Mastering Free Kicks', 'David Beckham', 1234567891, 2000]
        ]
        self.assertEqual(favorite_author('david beckham', metadata), True)

    def test_title_and_author(self):
        metadata = [['The History of the World Cup', 'Pelé', 1234567890, 1500]]
        self.assertEqual(title_and_author(metadata), [('The History of the World Cup', 'Pelé')])
        metadata = [
            ['The Evolution of Soccer', 'Lionel Messi', 1234567890, 1500],
            ['Goalkeeping Mastery', 'Manuel Neuer', 1234567891, 1700]
        ]
        self.assertEqual(title_and_author(metadata), [
            ('The Evolution of Soccer', 'Lionel Messi'),
            ('Goalkeeping Mastery', 'Manuel Neuer')
        ])
        self.assertEqual(title_and_author([]), [])

    def test_refine_search(self):
        metadata = [
            ['The History of the World Cup', 'Pelé', 1234567890, 2000, ['world', 'cup', 'soccer', 'history']],
            ['Soccer Strategies', 'Johan Cruyff', 1234567891, 1800, ['soccer', 'strategy', 'tactics']],
            ['Advanced Goalkeeping Techniques', 'Manuel Neuer', 1234567892, 1900, ['goalkeeping', 'techniques', 'soccer']]
        ]
        search_results = [metadata[0], metadata[1]]
        self.assertEqual(refine_search('world', search_results), [metadata[0]])
        metadata = [
            ['The History of the World Cup', 'Pelé', 1234567890, 2000, ['world', 'cup', 'soccer', 'history']],
            ['Soccer Strategies', 'Johan Cruyff', 1234567891, 1800, ['soccer', 'strategy', 'tactics']]
        ]
        search_results = [metadata[0], metadata[1]]
        self.assertEqual(refine_search('Techniques', search_results), [])
        metadata = [
            ['The Art of Free Kicks', 'David Beckham', 1234567890, 1600, ['free', 'kicks', 'soccer']],
            ['Goal Scoring Techniques', 'Cristiano Ronaldo', 1234567891, 1700, ['goal', 'scoring', 'techniques']]
        ]
        search_results = [metadata[0]]
        self.assertEqual(refine_search('FREE', search_results), [metadata[0]])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
