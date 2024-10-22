from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_empty_keyword(self, input_mock):
        keyword = ''
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_whitespace_keyword(self, input_mock):
        keyword = '    '
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo', 'Noise (music)', '1922 in music', 'Ken Kennedy (computer scientist)', '1986 in music', 'Spain national beach soccer team', 'Kevin Cadogan', 'Endogenous cannabinoid', '2009 in music', 'Rock music', 'Medical value travel', 'Lights (musician)', 'List of soul musicians', 'Human computer', 'Aube (musician)', 'List of overtone musicians', 'Black dog (ghost)', 'USC Trojans volleyball', 'Tim Arnold (musician)', '2007 Bulldogs RLFC season', 'Peter Brown (music industry)', 'Mexican dog-faced bat', 'Embryo drawing', 'Old-time music', 'Arabic music', 'C Sharp (programming language)', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Will Johnson (soccer)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Fiskerton, Lincolnshire', 'Reflection-oriented programming', 'B (programming language)', 'Richard Wright (musician)', 'Voice classification in non-classical music', 'Dalmatian (dog)', '1936 in music', 'Guide dog', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steven Cohen (soccer)', 'Steve Perry (musician)', '2009 Louisiana Tech Bulldogs football team', 'David Gray (musician)', 'Craig Martin (soccer)', 'Georgia Bulldogs football', 'Time travel', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'Python (programming language)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Endoglin', 'Indian classical music', 'Sun dog', '1996 in music', 'Lua (programming language)', 'Single-board computer', 'Mets de Guaynabo (volleyball)', \"United States men's national soccer team 2009 results\", 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'China national soccer team', 'Covariance and contravariance (computer science)', 'English folk music (1500–1899)', 'Personal computer', 'The Mandogs', 'David Levi (musician)', 'Scores (computer virus)', 'Digital photography', 'George Crum (musician)', 'Solver (computer science)', 'Georgia Bulldogs football under Robert Winston', 'Wildlife photography', 'Traditional Thai musical instruments', 'Landseer (dog)', 'Charles McPherson (musician)', 'Comparison of programming languages (basic instructions)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Spawning (computer gaming)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Ruby (programming language)', 'Texture (music)', 'List of computer role-playing games', 'Register (music)', 'Mode (computer interface)', '2007 in music', 'List of video games with time travel', '2008 in music', 'Semaphore (programming)', \"Wake Forest Demon Deacons men's soccer\"]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_non_existent_keyword(self, input_mock):
        keyword = 'unicorn'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_case_insensitivity(self, input_mock):
        keyword = 'DOG'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_special_characters_keyword(self, input_mock):
        keyword = '@#%!&'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_favorite_article_found(self, input_mock):
        keyword = 'dog'
        advanced_option = 4
        favorite_article = 'Guide dog'

        output = get_print(input_mock, [keyword, advanced_option, favorite_article])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) +  '\n' + print_advanced_option(advanced_option) + favorite_article + '\n' + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\nYour favorite article is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_favorite_article_not_found(self, input_mock):
        keyword = 'dog'
        advanced_option = 4
        favorite_article = 'non-existent article'

        output = get_print(input_mock, [keyword, advanced_option, favorite_article])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + favorite_article + '\n' + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\nYour favorite article is not in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_max_title_length(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        max_length = 10

        output = get_print(input_mock, [keyword, advanced_option, max_length])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(max_length) + '\n' + "\nHere are your articles: ['Guide dog', 'Endoglin', 'Sun dog']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_max_number_of_articles(self, input_mock):
        keyword = 'dog'
        advanced_option = 2
        max_articles = 5

        output = get_print(input_mock, [keyword, advanced_option, max_articles])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(max_articles) + '\n' + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_random_article(self, input_mock):
        keyword = 'dog'
        advanced_option = 3
        index = 2

        output = get_print(input_mock, [keyword, advanced_option, index])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(index) + '\n' + "\nHere are your articles: Endogenous cannabinoid\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_multiple_keywords(self, input_mock):
        keyword = 'dog'
        advanced_option = 5
        additional_keyword = 'bat'

        output = get_print(input_mock, [keyword, advanced_option, additional_keyword])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + additional_keyword + '\n' + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
