from typing import Callable, Optional

import utils

FILE = 'data/apache_logs.txt'

CMD_TO_FUNC = {
    "filter": utils.filter_query,
    "map": utils.map_query,
    "sort": utils.sort_query,
    "unique": utils.unique_query,
    "limit": utils.limit_query,
    "regex": utils.regex_query
}


def build_query(cmd: str, param: str, data: Optional[list[str]]) -> Callable[[str], Optional[list[str]]]:
    """returns needed function based of cmd's value """
    if data is None:
        with open(FILE) as file:
            prepared_data = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data
    return CMD_TO_FUNC[cmd](param=param, data=prepared_data)

