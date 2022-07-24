import tech_news.utils as utils
from parsel import Selector
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
    noticias = selector.css(utils.URLS["NOTICIAS"]).getall()

    if not noticias:
        return list()
    return noticias


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
