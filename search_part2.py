from wiki import article_metadata, ask_search, ask_advanced_search

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article metadata's relevant keywords
#
# Returns: list of metadata for articles in which the article is relevant to
#   the keyword. Relevance is determined by checking the metadata's "relevant
#   keywords" list for a case-insensitive match with the keyword parameter. #   The returned list should not include the "relevant keywords" list for each
#   article metadata.
#   
#   If the user does not enter anything, return an empty list
#
# Hint: to get list of existing article metadata, use article_metadata()
def search(keyword):
    list_of_artices = []
    if not keyword:
        return list_of_artices
    keyword = keyword.strip()
    for i in article_metadata():
        for j in i[3]:
            if keyword.lower() == j.lower():
                list_of_artices.append(i[:4])
    return list_of_artices
# print(search("           the"))
    

# 2) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   metadata - article metadata to search through
#
# Returns: list of article metadata from given metadata with articles not
#   exceeding max_length number of characters
def article_length(max_length, metadata):
    for i in metadata.copy():
        if len(i[0]) > max_length:
            metadata.remove(i)
    return metadata
# print(article_length(30,[['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]] ))

  
    

# 3) 
#
# Function: unique_authors
#
# Parameters:
#   count - max number of unique authors to include in the results
#   metadata - article metadata
#
# Returns: list of article metadata containing a maximum of `count` results,
#   each with a unique author. If two or more articles have the same author, 
#   include the first in the results and skip the others. Two authors are 
#   considered the same if they are a case-insensitive match. If count is 
#   larger than the number of unique authors, return all articles with the 
#   duplicate authors removed.
def unique_authors(count, metadata):
    if not metadata or count <= 0:
        return []
    result = []
    num = 0
    checked = set()
    for i in range(len(metadata)):
        if num < count:
            if metadata[i][1].lower() not in checked:
                checked.add(metadata[i][1].lower())
                result.append(metadata[i])
                num += 1
    return result
# print(unique_authors(5,[['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['List of soul musicians', 'jack johnson', 1175455921, 4878], ['Human computer', 'Bearcat', 1248275178, 4750], ['Aube (musician)', 'Mack Johnson', 1145410600, 3152], ['List of overtone musicians', 'Mack Johnson', 1176928050, 2299], ['Black dog (ghost)', 'Pegship', 1220471117, 14746], ['USC Trojans volleyball', 'jack johnson', 1218049435, 5525], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['2007 Bulldogs RLFC season', 'Burna Boy', 1177410119, 11116], ['Peter Brown (music industry)', 'Pegship', 1240235639, 2837], ['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138], ['Embryo drawing', 'Jack Johnson', 1034459202, 1712], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['C Sharp (programming language)', 'Burna Boy', 1232492672, 52364], ['List of Saturday Night Live musical sketches', 'Pegship', 1134966249, 13287], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Aco (musician)', 'Nihonjoe', 1132546632, 3129], ['Geoff Smith (British musician)', 'Pegship', 1194687509, 2043], ['Fiskerton, Lincolnshire', 'Bearcat', 1259869948, 5853], ['B (programming language)', 'jack johnson', 1196622610, 5482], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582], ['1936 in music', 'RussBot', 1243745950, 23417], ['Guide dog', 'Jack Johnson', 1165601603, 7339], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['2009 Louisiana Tech Bulldogs football team', 'Nihonjoe', 1245796406, 22410], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Craig Martin (soccer)', 'Mr Jake', 1174203493, 709], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], ['Time travel', 'Jack Johnson', 1140826049, 35170], ['Fisk University', 'RussBot', 1263393671, 16246], ['Annie (musical)', 'Jack Johnson', 1223619626, 27558], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['Python (programming language)', 'Burna Boy', 1137530195, 41571], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Tom Hooper (musician)', 'Bearcat', 1204967541, 1441], ['Endoglin', 'Bearcat', 1212259031, 6778], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['Sun dog', 'Mr Jake', 1208969289, 18050], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Lua (programming language)', 'Burna Boy', 1113957128, 0], ['Single-board computer', 'Gary King', 1220260601, 8271], ['Joseph Williams (musician)', 'Pegship', 1140752684, 4253], ['The Hunchback of Notre Dame (musical)', 'Nihonjoe', 1192176615, 42], ['Covariance and contravariance (computer science)', 'Bearcat', 1167547364, 7453], ['Personal computer', 'Pegship', 1220391790, 45663], ['The Mandogs', 'Mack Johnson', 1205282029, 3968], ['David Levi (musician)', 'Gary King', 1212260237, 3949], ['Scores (computer virus)', 'RussBot', 1235850703, 2706], ['Digital photography', 'Mr Jake', 1095727840, 18093], ['George Crum (musician)', 'jack johnson', 1252996687, 3848], ['Solver (computer science)', 'Gary King', 1253282654, 1861], ['Wildlife photography', 'Jack Johnson', 1165248747, 1410], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['Landseer (dog)', 'Bearcat', 1231438650, 2006], ['Charles McPherson (musician)', 'Bearcat', 1255183865, 3007], ['Comparison of programming languages (basic instructions)', 'RussBot', 1238781354, 61644], ['Les Cousins (music club)', 'Mack Johnson', 1187072433, 4926], ['Paul Carr (musician)', 'Burna Boy', 1254142018, 5716], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Danja (musician)', 'RussBot', 1257155543, 6925], ['Ruby (programming language)', 'Bearcat', 1193928035, 30284], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['Register (music)', 'Pegship', 1082665179, 598], ['Mode (computer interface)', 'Pegship', 1182732608, 2991], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605], ['Semaphore (programming)', 'Nihonjoe', 1144850850, 7616], ["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745]])) 

        
        
# 4) 
#
# Function: most_recent_article
#
# Parameters:
#   metadata - article metadata
#
# Returns: article metadata of the article published most recently according
#   to the timestamp. Note this should return just a 1D list representing
#   a single article.
def most_recent_article(metadata):
    hold = metadata[0][2]
    count  = 0 
    for i in range(1, len(metadata)):
        if metadata[i][2] > hold:
            hold = metadata[i][2]
            count = i
    return metadata[count]
# print(most_recent_article([['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 37669593, 2117]] ))



# 5) 
#
# Function: favorite_author
#
# Parameters:
#   favorite - favorite author title
#   metadata - article metadata
#
# Returns: True if favorite author is in the given articles (case 
#   insensitive), False otherwise
def favorite_author(favorite, metadata):
    for i in metadata:
        if i[1].lower() == favorite.lower().strip():
            return True
    return False
# print(favorite_author("       JaCK Johnson",[['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 37669593, 2117]] ))

# 6) 
#
# Function: title_and_author
#
# Parameters:
#   metadata - article metadata
#
# Returns: list of Tuples containing (title, author) for all of the given 
#   metadata.
def title_and_author(metadata):
    result = []
    for i in metadata:
        result.append(tuple(i[:2]))
    return result
# print(title_and_author([['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 37669593, 2117]] ))


# 7) 
#
# Function: refine_search
#
# Parameters:
#   keyword - additional keyword to search
#   metadata - article metadata from basic search
#
# Returns: searches for article metadata from entire list of available
#   articles using keyword. Returns the article metadata that is returned in 
#   in *both* the additional search and the basic search. The results should
#   be in the same order that they were returned in the basic search. Two
#   articles can be considered the same if both their author and article title
#   match exactly.
def refine_search(keyword, metadata):
    result = []
    value1 = search(keyword)
    for i in metadata:
        if i in value1:
            result.append(i)
    return result
# print(refine_search("soccer", [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'and', 'rock', 'singer', 'songwriter', 'also', 'known', 'hip', 'hop', 'musician', 'folk', 'pop', 'composer', 'drummer', 'player', 'rapper', 'john', 'don', 'guitarist', 'the', 'andrew', 'country', 'indie', 'charlie', 'alternative', 'paul', 'matt', 'james', 'blues', 'bassist', 'cellist', 'pianist', 'artist', 'marie', 'dance', 'winner', 'idol', 'mike', 'keyboardist', 'jason', 'music', 'tim', 'kim', 'soprano', 'kevin', 'martin', 'violinist', 'dan', 'blue', 'new', 'daniel', 'producer', 'punk', 'conductor', 'gospel', 'dave', 'big', 'band', 'george', 'brian', 'bill', 'classical', 'david', 'operatic', 'michael', 'film', 'jon', 'soul', 'billy', 'record', 'jim', 'member', 'broken', 'social', 'scene', 'musical', 'theatre', 'actress', 'actor', 'peter', 'ian', 'electronic', 'rhythm', 'taylor', 'vocalist', 'jesse', 'radio', 'personality', 'for', 'andy', 'former', 'solo', 'chris', 'ryan', 'mark', 'scott', 'kate', 'multi', 'formerly', 'mother', 'instrumentalist', 'johnson', 'white', 'smith']]]))











# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article metadata to contain only ones of the maximum length
        articles = article_length(value, articles)
    if advanced == 2:
        # value stores max number of unique authors
        # Update article metadata to contain only the max number of authors
        articles = unique_authors(value, articles)
    elif advanced == 3:
        # Update articles to only contain the most recent article
        articles = most_recent_article(articles)
    elif advanced == 4:
        # value stores author
        # Store whether author is in search results into variable named 
        # has_favorite
        has_favorite = favorite_author(value, articles)
    elif advanced == 5:
        # Update article metadata to only contain titles and authors
        articles = title_and_author(articles)
    elif advanced == 6:
        # value stores keyword to search
        # Update article metadata to contain only article metadata
        # that is contained in both searches
        articles = refine_search(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite author is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
