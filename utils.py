def filter_query(param, data):
    return list(filter(lambda p: param in p, data))


def map_query(param, data):
    col = int(param)
    return list(map(lambda p: p.split(' ')[col], data))


def unique_query(data):
    return list(set(data))


def sort_query(param, data):
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param, data):
    limit = int(param)
    return list(data)[:limit]
