from tech_news.database import find_news
from tech_news.analyzer.formatted import formatted


# Requisito 10
def top_5_news():
    new_list = find_news()
    if new_list is None:
        return None

    new_list.sort(
        key=lambda new: new['comments_count'],
        reverse=True)

    return formatted(new_list[:5])


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
