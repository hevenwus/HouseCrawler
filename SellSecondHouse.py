
from utils import (
    get_html, get_soup, append_item, delay, crawler_context, logger
)


def parse_flood(items1, i):
    if i &lt; len(items1) and items1[i].a:
        return items1[i].a.text
    return ''


def parse_page(html: str):
    soup = get_soup(html)

    items = soup.find_all(attrs={'class': 'img VIEWDATA CLICKDATA maidian-detail'})
    items1 = soup.find_all(attrs={'class': 'positionInfo'})
    items2 = soup.find_all(attrs={'class': 'houseInfo'})
    items3 = soup.find_all(attrs={'class': 'followInfo'})
    items4 = soup.find_all(attrs={'class': 'totalPrice'})
    items5 = soup.find_all(attrs={'class': 'unitPrice'})

    min_len = min(len(items), len(items1), len(items2), len(items3), len(items4), len(items5))
    
    for i in range(min_len):
        yield {
            'flood': parse_flood(items1, i),
            'title': items[i].attrs.get('title', ''),
            'href': items[i].attrs.get('href', ''),
            'alt': items[i].img['alt'] if items[i].img else '',
            'totalPrice': items4[i].span.text if items4[i].span else '',
            'unitPrice': items5[i].span.text if items5[i].span else '',
            'houseInfo': items2[i].text.strip(),
            'followInfo': items3[i].text.strip()
        }


def start_get_data(page: int, district: str = ''):
    base_url = 'https://hf.ke.com/ershoufang/'
    if district:
        base_url = f'{base_url}{district}/pg'
    else:
        base_url = f'{base_url}pg'

    for i in range(page):
        url = f'{base_url}{i + 1}/'
        html = get_html(url)
        if not html:
            continue

        for item in parse_page(html):
            logger.info(item)
            append_item(item, 'sell.txt')

        delay()


if __name__ == '__main__':
    with crawler_context('在售二手房'):
        start_get_data(10, 'feixi')

