import re
from typing import Optional


def filter_query(param: str, data: str) -> Optional[list[str]]:
    return list(filter(lambda p: param in p, data))


def map_query(param: str, data: str) -> Optional[list[str]]:
    col = int(param)
    return list(map(lambda p: p.split(' ')[col], data))


def unique_query(data: str) -> Optional[list[str]]:
    return list(set(data))


def sort_query(param: str, data: str) -> Optional[list[str]]:
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: str) -> Optional[list[str]]:
    limit = int(param)
    return list(data)[:limit]


def regex_query(param: str, data: str) -> Optional[list[str]]:
    return list(filter(lambda p: re.findall(param, p), data))
