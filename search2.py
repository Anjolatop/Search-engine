def search(keyword):
    list_of_artices = []
    if not keyword:
        return list_of_artices
    keyword = keyword.strip()
    for i in article_metadata():
        for j in i[4]:
            if keyword.lower() == j.lower():
                list_of_artices.append(i[:4])
    return list_of_artices


def article_length(max_length, metadata):
    for i in metadata.copy():
        if len(i[0]) > max_length:
            metadata.remove(i)
    return metadata

def unique_authors(count, metadata):
    if not metadata or count <= 0:
        return []
    result = []
    num = 0
    checked = set()
    for i in range(len(metadata)):
        if num < count -1:
            if metadata[i][1].lower() not in checked:
                checked.add(metadata[i][1].lower())
                result.append(metadata[i])
                num += 1
        else:
            return result

def most_recent_article(metadata):
    hold = metadata[0][2]
    count  = 0 
    for i in range(1, len(metadata)):
        if metadata[i][2] > hold:
            hold = metadata[i][2]
            count = i
    return metadata[count]


def favorite_author(favorite, metadata):
    for i in metadata:
        if i[1].lower() == favorite.lower().strip():
            return True
    return False


def title_and_author(metadata):
    result = []
    for i in metadata:
        result.append(tuple(i[:2]))
    return result


def refine_search(keyword, metadata):
    result = []
    value1 = search(keyword)
    for i in metadata:
        if i in value1:
            result.append(i)
    return result
