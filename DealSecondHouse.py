
from bs4 import BeautifulSoup
from utils import (
    get_html, get_soup, append_item, delay, crawler_context, logger
)


def parse_chengjiao(items6, i):
    guaTime = ''
    if i &lt; len(items6):
        for item in items6[i]:
            strDf = str(item)
            if '成交周期' in strDf:
                guaTime = strDf[6:len(strDf) - 7]
    return guaTime


def parse_page(html: str):
    soup = get_soup(html)

    items = soup.find_all(attrs={'class': 'img CLICKDATA maidian-detail'})
    items1 = soup.find_all(attrs={'class': 'CLICKDATA maidian-detail'})
    items2 = soup.find_all(attrs={'class': 'houseInfo'})
    items3 = soup.find_all(attrs={'class': 'positionInfo'})
    items4 = soup.find_all(attrs={'class': 'totalPrice'})
    items5 = soup.find_all(attrs={'class': 'unitPrice'})
    items6 = soup.find_all(attrs={'class': 'dealCycleTxt'})
    items7 = soup.find_all(attrs={'class': 'dealDate'})

    min_len = min(len(items), len(items1), len(items2), len(items3), len(items4), len(items5), len(items6), len(items7))
    
    for i in range(min_len):
        yield {
            'title': items1[i].text.strip(),
            'totalPrice': items4[i].span.text + '万' if items4[i].span else '',
            'unitPrice': items5[i].span.text + '元/平米' if items5[i].span else '',
            'dealDate': items7[i].text.strip(),
            'dealPrice': items6[i].span.text if items6[i].span else '',
            'dealTime': parse_chengjiao(items6, i),
            'href': items[i].attrs.get('href', ''),
            'image': items[i].img['data-original'] if items[i].img else '',
            'houseInfo': items2[i].text.strip() + items3[i].text.strip(),
        }


def start_get_data(page: int, district: str = ''):
    base_url = 'https://hf.ke.com/chengjiao/'
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
            append_item(item, 'deal.txt')

        delay()


if __name__ == '__main__':
    with crawler_context('二手房成交数据'):
        start_get_data(10, 'feixi')

