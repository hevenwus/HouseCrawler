
from utils import get_pq, append_item, delay, crawler_context, logger


def start_get_data(url: str):
    doc = get_pq(url)
    if not doc:
        return

    items = doc('.title a')

    for item in items.items():
        yield {
            'title': item.attr('title'),
            'href': item.attr('href')
        }


def start_crawler(max_start: int = 500):
    base_url = 'https://www.douban.com/group/shanghaizufang/discussion?start='

    i = 0
    while i &lt;= max_start:
        url = base_url + str(i)
        for item in start_get_data(url):
            logger.info(item)
            append_item(item, 'douban.txt')
        i += 25
        delay()


if __name__ == '__main__':
    with crawler_context('豆瓣租房'):
        start_crawler(500)

