
import json
import time
import logging
import os
from typing import List, Dict, Any, Generator
from contextlib import contextmanager

import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from requests.exceptions import RequestException

from config import HEADERS, REQUEST_DELAY, OUTPUT_DIR

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_html(url: str, retry: int = 3) -&gt; str:
    for i in range(retry):
        try:
            logger.info(f'正在请求: {url}')
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                return response.text
            logger.warning(f'请求失败，状态码: {response.status_code}，重试 {i+1}/{retry}')
        except RequestException as e:
            logger.error(f'请求异常: {e}，重试 {i+1}/{retry}')
        time.sleep(REQUEST_DELAY)
    return ''


def get_pq(url: str) -&gt; Any:
    try:
        logger.info(f'正在请求: {url}')
        return pq(url=url)
    except Exception as e:
        logger.error(f'PyQuery 请求异常: {e}')
        return None


def get_soup(html: str) -&gt; BeautifulSoup:
    return BeautifulSoup(html, 'lxml')


def save_to_file(data: List[Dict[str, Any]], filename: str, append: bool = False) -&gt; None:
    filepath = os.path.join(OUTPUT_DIR, filename)
    mode = 'a' if append else 'w'
    try:
        with open(filepath, mode, encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        logger.info(f'数据已保存到: {filepath}')
    except IOError as e:
        logger.error(f'保存文件失败: {e}')


def append_item(item: Dict[str, Any], filename: str) -&gt; None:
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    except IOError as e:
        logger.error(f'追加数据失败: {e}')


def safe_extract(container, index: int, default: Any = '') -&gt; Any:
    try:
        return container[index]
    except (IndexError, AttributeError):
        return default


def delay() -&gt; None:
    time.sleep(REQUEST_DELAY)


@contextmanager
def crawler_context(name: str):
    logger.info(f'开始爬取: {name}')
    start_time = time.time()
    try:
        yield
    except Exception as e:
        logger.error(f'爬取过程出错: {e}')
        raise
    finally:
        elapsed = time.time() - start_time
        logger.info(f'爬取完成: {name}，耗时: {elapsed:.2f}秒')

