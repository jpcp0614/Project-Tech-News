from parsel import Selector
from tech_news.database import create_news
import tech_news.utils as utils
import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            timeout=utils.TIMEOUT_MAX,
            headers=utils.HEADER,
            )
        time.sleep(1)
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None
    except requests.RequestException:
        print("Error unknown")
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    noticias = selector.css(utils.SELECTORS["NEWS"]).getall()

    if not noticias:
        return list()
    return noticias


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css(utils.SELECTORS["NEXT_PAGE"]).get()

    if not next_page:
        return None
    return next_page


# Requisito 4
# def scrape_noticia(html_content):
#     selector = Selector(html_content)
#     content = {
#         'url': selector.css("[rel='canonical']::attr(href)").get().strip(),
#         'title': selector.css("h1.entry-title::text").get().strip(),
#         'timestamp': selector.css("li.meta-date::text").get(),
#         'writer': selector.css("a.url::text").get(),
#         'comments_count': len(selector.css(".comment-list li").getall()),
#         'summary': ''.join(
#             selector.css(
#                 ".entry-content > p:first-of-type *::text"
#                 ).getall()).strip(),
#         'tags': selector.css(".post-tags a::text").getall(),
#         'category': selector.css("span.label::text").get()
#     }
#     return content


def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = dict()

    news["url"] = selector.css(utils.SELECTORS["URL"]).get()
    news["title"] = selector.css(utils.SELECTORS["TITLE"]).get().strip()
    news["timestamp"] = selector.css(utils.SELECTORS["TIMESTAMP"]).get()
    news["writer"] = selector.css(utils.SELECTORS["WRITER"]).get()
    news["comments_count"] = len(
        selector.css(utils.SELECTORS["COMMENTS_COUNT"]).getall())
    news["summary"] = "".join(
        selector.css(utils.SELECTORS["SUMMARY"]).getall()).strip()
    news["tags"] = selector.css(utils.SELECTORS["TAGS"]).getall()
    news["category"] = selector.css(utils.SELECTORS["CATEGORY"]).get()

    return news


# Requisito 5
def get_tech_news(amount):
    html_content = fetch(utils.URL)
    novidades = scrape_novidades(html_content)
    news = list()

    while amount >= 1:
        for url in novidades[:amount]:
            html = fetch(url)
            news.append(scrape_noticia(html))
            amount -= 1
        if amount >= 1:
            next_page_link = scrape_next_page_link(html_content)
            html_content = fetch(next_page_link)
            novidades = scrape_novidades(html_content)

    create_news(news)
    return news
