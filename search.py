from wiki import article_titles, ask_search, ask_advanced_search

# FUNCTION 1
# Iterates through the articles list(called with articles_titles()) and returns a list with the titles that contain the stripped keywords
def search(keyword):
    if not keyword:
        return []
    keyword = keyword.strip()
    titles_with_keywords = []
     
    for title in article_titles():
        if keyword.lower() in title.lower():
            titles_with_keywords.append(title)
    return titles_with_keywords


#FUNCTION 2
# Iterates through the titles list and returns a list of titles that are not greater than the max_length
def title_length(max_length, titles):
    result = []
    for title in titles:
        title = title.strip()
        if len(title) <= max_length:
            result.append(title)
    return result


# FUNCTION 3
# Iterates through the titles list and returns a list of the first 'count' titles.
def article_count(count, titles):
    result = []
    if not titles:
        return []
    if count > len(titles):
        return titles
    for i in range(count):
        result.append(titles[i])
    return result


# FUNCTION 4
# Returns the title at index 'index' in 'titles'
def random_article(index, titles):
    if index not in range(len(titles)):
        return ''
    return titles[index]


# FUNCTION 5
# Iterates through 'titles' list and checks if 'favorite' (case-insensitive) is in 'titles'
def favorite_article(favorite, titles):
    for article in titles:
        if favorite.lower().strip() == article.lower().strip():
            return True
    return False

# FUNCTION 6
# Iterates through the list returned from calling 'search' on 'keyword', adds it to the titles list and returns the result.
def multiple_keywords(keyword, titles):
    result = titles
    for title in search(keyword):
        title = title.strip()
        if title not in result:
            result.append(title)
    return result

# --------------------------------------------------------------------------------------------


# MAIN CODE    
    
# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-5)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article titles to contain only ones of the maximum length
        articles = title_length(value, articles)
    if advanced == 2:
        # value stores max number of articles
        # Update article titles to contain only the max number of articles
        articles = article_count(value, articles)
    elif advanced == 3:
        # value stores random number
        # Update articles to only contain the article title at index of the random number
        articles = random_article(value, articles)
    elif advanced == 4:
        # value stores article title
        # Store whether article title is in the search results into a variable named has_favorite
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
        # value stores keyword to search
        # Updated article titles to contain article titles from the first search and the second search
        articles = multiple_keywords(value, articles)

    print()
    
    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
