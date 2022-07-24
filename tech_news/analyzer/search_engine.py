from tech_news.database import search_news
from tech_news.analyzer.formatted import formatted
from datetime import datetime


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    return formatted(data)


# Requisito 7
def search_by_date(date):
    try:
        input = datetime.fromisoformat(date)
        searchDate = datetime.strftime(input, "%d/%m/%Y")
        data = search_news({"timestamp": searchDate})
        return formatted(data)
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    data = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return formatted(data)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
