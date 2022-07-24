from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})

    formatted_list = list()

    for news in data:
        formatted_title_url = (news["title"], news["url"])
        formatted_list.append(formatted_title_url)

    return formatted_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
