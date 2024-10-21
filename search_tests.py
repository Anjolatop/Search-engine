    def test_search(self):
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'] 
        expected_music_search_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        expected_animal_search_results = []
        expected_aandA_search_results = ['List of Canadian musicians', 'Edogawa, Tokyo', 'Spain national beach soccer team', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Medical value travel', 'Lights (musician)', 'List of soul musicians', 'Human computer', 'Aube (musician)', 'List of overtone musicians', 'Black dog (ghost)', 'USC Trojans volleyball', 'Tim Arnold (musician)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Embryo drawing', 'Arabic music', 'C Sharp (programming language)', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Reflection-oriented programming', 'B (programming language)', 'Richard Wright (musician)', 'Voice classification in non-classical music', 'Dalmatian (dog)', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', '2009 Louisiana Tech Bulldogs football team', 'David Gray (musician)', 'Craig Martin (soccer)', 'Georgia Bulldogs football', 'Time travel', 'Annie (musical)', 'Alex Turner (musician)', 'Python (programming language)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', 'Lua (programming language)', 'Single-board computer', 'Mets de Guaynabo (volleyball)', "United States men's national soccer team 2009 results", 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'China national soccer team', 'Covariance and contravariance (computer science)', 'Personal computer', 'The Mandogs', 'David Levi (musician)', 'Digital photography', 'George Crum (musician)', 'Georgia Bulldogs football under Robert Winston', 'Wildlife photography', 'Traditional Thai musical instruments', 'Landseer (dog)', 'Charles McPherson (musician)', 'Comparison of programming languages (basic instructions)', 'Paul Carr (musician)', 'Spawning (computer gaming)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Ruby (programming language)', 'List of computer role-playing games', 'Mode (computer interface)', 'List of video games with time travel', 'Semaphore (programming)', "Wake Forest Demon Deacons men's soccer"]
        self.assertEqual(search("DOG"), expected_dog_search_results)
        self.assertEqual(search("animal"), expected_animal_search_results)
        self.assertEqual(search(""), [])
        self.assertEqual(search(None), [])
        self.assertEqual(search("    a     "),expected_aandA_search_results)
        self.assertEqual(search("A"),expected_aandA_search_results)
        self.assertEqual(search("List of Canadian musicians"), ['List of Canadian musicians'])

    def test_title_length(self):
        expected_answer = ['short', 'longer', 'medium']
        self.assertEqual(title_length(10, ["         short", "longer", "medium", "longer than usual", "longer than usualer"]), expected_answer) 
        self.assertEqual(title_length(0, ["         short", "longer", "medium", "longer than usual", "longer than usualer"]), [])
        self.assertEqual(title_length(100, ["         short", "longer", "medium", "longer than usual", "longer than usualer"]), ["short", "longer", "medium", "longer than usual", "longer than usualer"])
        self.assertEqual(title_length(10, ["        ", "longer", "medium", "longer than usual", "longer than usualer"]),['longer', 'medium'])
        self.assertEqual(title_length(10, []), [])
        self.assertEqual(title_length(-5, ["hellooooooooooooooooooooooo"]), [])
      
    def test_article_count(self):
        self.assertEqual(article_count(-5, []), [])
        self.assertEqual(article_count(3, ["         ", "longer", "medium", "longer than usual", "longer than usualer"]), ["longer", "medium", "longer than usual"] )
        self.assertEqual(article_count(8, ["    ", "longer", "medium", "longer than usual", "longer than usualer"]),['longer', 'medium', 'longer than usual', 'longer than usualer'])
        self.assertEqual(article_count(0, ["    ", "longer", "medium", "longer than usual", "longer than usualer"]),[])
        self.assertEqual(article_count(1, ["    ", "longer", "medium", "longer than usual", "longer than usualer"]),['longer'])
        self.assertEqual(article_count(1, "hello",), [])
        self.assertEqual(article_count(8, []), [])
        self.assertEqual(article_count(4, ["longer", "medium", "longer than usual", "longer than usualer"]), ["longer", "medium", "longer than usual", "longer than usualer"])
        self.assertEqual(article_count(2, [ "           ", "     longer        ", "medium", "longer than usual", "longer than usualer"]), ['longer', 'medium'])
        self.assertEqual(article_count(2, [ "      ", "", "           "]), [])

    def test_random_article(self):
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(random_article(5, expected_dog_search_results), 'Mexican dog-faced bat')
        self.assertEqual(random_article(3, ["         ", "longer", "medium", "longer than usual", "longer than usualer"]), "longer than usual",)
        self.assertEqual(random_article(8, [" hi   ", "longer", "medium", "longer than usual", "longer than usualer"]),"")
        self.assertEqual(random_article(0, [" hi   ", "longer", "medium", "longer than usual", "longer than usualer"])," hi   ")
        self.assertEqual(random_article(1, ["    ", "longer", "medium", "longer than usual", "longer than usualer"]),'longer')
        self.assertEqual(random_article(8, []), "")
        self.assertEqual(random_article(4, ["longer", "medium", "longer than usual", "longer than usualer"]), "")

    def test_favorite_article(self):
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(favorite_article('    KEvin Cadogan   ', expected_dog_search_results), True)
        self.assertEqual(favorite_article('Kevin', expected_dog_search_results), False)
        self.assertEqual(favorite_article('endogEnoUs caNnabinoid', expected_dog_search_results), True)
        self.assertEqual(favorite_article("2007", expected_dog_search_results), False)
        self.assertEqual(favorite_article(",", expected_dog_search_results), False)
        self.assertEqual(favorite_article('2007 bulldogs rlfc season,expected_dog_search_results', expected_dog_search_results), False)
        self.assertEqual(favorite_article("Mexican", expected_dog_search_results), False)

    def test_multiple_keywords(self):
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(multiple_keywords("   en   ",['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'French pop music', 'Ken Kennedy (computer scientist)', 'Reflection-oriented programming', 'Steven Cohen (soccer)', "United States men's national soccer team 2009 results", 'Covariance and contravariance (computer science)', 'English folk music (1500–1899)', 'Solver (computer science)', 'Traditional Thai musical instruments', "Wake Forest Demon Deacons men's soccer"] )
        self.assertEqual(multiple_keywords("   EN   ",['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'French pop music', 'Ken Kennedy (computer scientist)', 'Reflection-oriented programming', 'Steven Cohen (soccer)', "United States men's national soccer team 2009 results", 'Covariance and contravariance (computer science)', 'English folk music (1500–1899)', 'Solver (computer science)', 'Traditional Thai musical instruments', "Wake Forest Demon Deacons men's soccer"] )
        self.assertEqual(multiple_keywords("   kev   ", ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords("     ",['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', 'Ken Kennedy (computer scientist)', '1986 in music', 'Spain national beach soccer team', '2009 in music', 'Rock music', 'Medical value travel', 'Lights (musician)', 'List of soul musicians', 'Human computer', 'Aube (musician)', 'List of overtone musicians', 'USC Trojans volleyball', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Embryo drawing', 'Old-time music', 'Arabic music', 'C Sharp (programming language)', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Will Johnson (soccer)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Fiskerton, Lincolnshire', 'Reflection-oriented programming', 'B (programming language)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steven Cohen (soccer)', 'Steve Perry (musician)', 'David Gray (musician)', 'Craig Martin (soccer)', 'Time travel', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'Python (programming language)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Lua (programming language)', 'Single-board computer', 'Mets de Guaynabo (volleyball)', "United States men's national soccer team 2009 results", 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'China national soccer team', 'Covariance and contravariance (computer science)', 'English folk music (1500–1899)', 'Personal computer', 'David Levi (musician)', 'Scores (computer virus)', 'Digital photography', 'George Crum (musician)', 'Solver (computer science)', 'Wildlife photography', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Comparison of programming languages (basic instructions)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Spawning (computer gaming)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Ruby (programming language)', 'Texture (music)', 'List of computer role-playing games', 'Register (music)', 'Mode (computer interface)', '2007 in music', 'List of video games with time travel', '2008 in music', 'Semaphore (programming)', "Wake Forest Demon Deacons men's soccer"]) 
        self.assertEqual(multiple_keywords(",", expected_dog_search_results), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Fiskerton, Lincolnshire', 'List of dystopian music, TV programs, and games'])
        self.assertEqual(multiple_keywords("", expected_dog_search_results), expected_dog_search_results)
        self.assertEqual(multiple_keywords("kev", expected_dog_search_results), expected_dog_search_results)
