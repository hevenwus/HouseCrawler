
from utils import get_pq, append_item, delay, crawler_context, logger


def start_get_data(url: str):
    doc = get_pq(url)
    if not doc:
        return

    items_aside = doc('.content__list--item--aside')
    items_img = doc('.content__list--item--aside img')
    items_location = doc('.content__list--item--des')
    items_price = doc('.content__list--item-price')
    items_time = doc('.content__list--item--time.oneline')
    items_tag = doc('.content__list--item--bottom.oneline')

    title_list = [item.attr('title') for item in items_aside.items()]
    href_list = ['https://sh.zu.ke.com' + item.attr('href') for item in items_aside.items()]
    img_list = [item.attr('data-src') for item in items_img.items()]
    location_list = [item.text().strip() for item in items_location.items()]
    price_list = [item.text().strip() for item in items_price.items()]
    time_list = [item.text().strip() for item in items_time.items()]
    tag_list = [item.text().strip() for item in items_tag.items()]

    min_len = min(len(title_list), len(href_list), len(img_list),
                  len(location_list), len(price_list), len(time_list), len(tag_list))

    for i in range(min_len):
        yield {
            'title': title_list[i],
            'unitPrice': price_list[i],
            'location': location_list[i],
            'time': time_list[i],
            'tag': tag_list[i],
            'href': href_list[i],
            'image': img_list[i]
        }


def start_crawler(pages: int = 5, district: str = 'xuhui'):
    base_url = f'https://sh.zu.ke.com/zufang/{district}/pg'

    for i in range(1, pages + 1):
        url = f'{base_url}{i}/'
        for item in start_get_data(url):
            logger.info(item)
            append_item(item, 'zufang.txt')
        delay()


if __name__ == '__main__':
    with crawler_context('贝壳租房'):
        start_crawler(5, 'xuhui')

