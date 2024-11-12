def get_short_links_by_tuple(tuple: tuple) -> dir:
    links_dir = {}

    for obj in tuple:
        prefix, link = obj
        links_dir[prefix] = link

    return links_dir
