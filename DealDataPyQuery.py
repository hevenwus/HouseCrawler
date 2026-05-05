
from utils import get_pq, append_item, delay, crawler_context, logger


def start_get_data(url: str):
    doc = get_pq(url)
    if not doc:
        return

    items_img = doc('.img.CLICKDATA.maidian-detail img')
    items_title = doc('.listContent li .info .title a')
    items_deal_date = doc('.info .dealDate')
    items_house_info = doc('.info .houseInfo')
    items_total_price = doc('.info .totalPrice .number')
    items_unit_price = doc('.info .flood .unitPrice')
    items_position = doc('.info .flood .positionInfo')
    items_deal_cycle = doc('.info .dealCycleeInfo .dealCycleTxt')

    img_list = [item.attr('data-original') for item in items_img.items()]
    title_list = [item.text().strip() for item in items_title.items()]
    href_list = [item.attr('href') for item in items_title.items()]
    deal_date_list = [item.text().strip() for item in items_deal_date.items()]
    house_info_list = [item.text().strip() for item in items_house_info.items()]
    total_price_list = [item.text().strip() + '万' for item in items_total_price.items()]
    unit_price_list = [item.text().strip() for item in items_unit_price.items()]
    position_list = [item.text().strip() for item in items_position.items()]
    deal_cycle_list = [item.text().strip() for item in items_deal_cycle.items()]

    min_len = min(len(img_list), len(title_list), len(href_list), len(deal_date_list),
                  len(house_info_list), len(total_price_list), len(unit_price_list),
                  len(position_list), len(deal_cycle_list))

    for i in range(min_len):
        yield {
            'title': title_list[i],
            'totalPrice': total_price_list[i],
            'unitPrice': unit_price_list[i],
            'dealDate': deal_date_list[i],
            'dealInfo': deal_cycle_list[i],
            'href': href_list[i],
            'image': img_list[i],
            'houseInfo': house_info_list[i] + position_list[i]
        }


def start_crawler(pages: int = 10, district: str = 'feixi'):
    base_url = f'https://hf.ke.com/chengjiao/{district}/pg'

    for i in range(1, pages + 1):
        url = f'{base_url}{i}/'
        for item in start_get_data(url):
            logger.info(item)
            append_item(item, 'deal.txt')
        delay()


if __name__ == '__main__':
    with crawler_context('二手房成交数据 (PyQuery)'):
        start_crawler(10, 'feixi')

