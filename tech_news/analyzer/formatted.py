def formatted(data):
    formatted_list = list()

    for news in data:
        formatted_title_url = (news["title"], news["url"])
        formatted_list.append(formatted_title_url)

    return formatted_list
