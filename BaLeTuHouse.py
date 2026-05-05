
from utils import get_pq, append_item, delay, crawler_context, logger


def start_get_data(url: str):
    doc = get_pq(url)
    if not doc:
        return

    items1 = doc('.listUnit-date.clearfix.PBA_list_house')
    items2 = doc('.pro-pic.li_phoneNum a')
    items3 = doc('.pro-pic.li_phoneNum a .lazy')
    items4 = doc('.list-pic-title h3 a')
    items5 = doc('.list-pic-ps')
    items6 = doc('.list-pic-ad')
    items7 = doc('.pro-lable')
    items8 = doc('.room-time')

    name_list = [item.attr('name') for item in items1.items()]
    cat_list = [item.attr('category') for item in items1.items()]
    variant_list = [item.attr('variant') for item in items1.items()]
    price_list = [int(item.attr('price')) for item in items1.items()]
    href_list = [item.attr('href') for item in items2.items()]
    img_list = [item.attr('data-original') for item in items3.items()]
    title_list = [item.attr('title') for item in items4.items()]
    info_list = [item.text() for item in items5.items()]
    addr_list = [item.text() for item in items6.items()]
    tag_list = [item.text() for item in items7.items()]
    time_list = [item.text() for item in items8.items()]

    min_len = min(len(name_list), len(href_list), len(img_list), len(title_list),
                  len(info_list), len(addr_list), len(tag_list), len(time_list))

    for i in range(min_len):
        yield {
            'name': name_list[i],
            'category': cat_list[i],
            'variant': variant_list[i],
            'price': price_list[i],
            'href': href_list[i],
            'image': img_list[i],
            'title': title_list[i],
            'house': info_list[i],
            'address': addr_list[i],
            'remark': tag_list[i],
            'time': time_list[i]
        }


def start_crawler(pages: int = 10):
    base_url = 'http://sh.baletu.com/zhaofang/p{page_num}o1a1d900/?seachId=0&amp;is_rec_house=0&amp;entrance=14&amp;solr_house_cnt=5176'

    for i in range(1, pages + 1):
        url = base_url.format(page_num=i)
        for item in start_get_data(url):
            logger.info(item)
            append_item(item, 'baletu.txt')
        delay()


if __name__ == '__main__':
    with crawler_context('巴乐兔租房'):
        start_crawler(10)

