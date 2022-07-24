TIMEOUT_MAX = 3
HEADER = {"user-agent": "Fake user-agent"}
URL = "https://blog.betrybe.com/"


# *URL's
SELECTORS = {
    "NEWS": "div.cs-overlay a ::attr(href)",
    "NEXT_PAGE": "a.next ::attr(href)",
    "URL": "link[rel='canonical'] ::attr(href)",
    "TITLE": "h1.entry-title ::text",
    "TIMESTAMP": "li.meta-date ::text",
    "WRITER": "span.author a ::text",
    "COMMENTS_COUNT": "ol.comment-list li",
    "SUMMARY": "div.entry-content > p:nth-of-type(1) *::text",
    "TAGS": "section.post-tags a ::text",
    "CATEGORY": "a.category-style span.label ::text",
}
