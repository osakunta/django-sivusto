
def split_and_remove_empty(string):
    return list(filter(None, string.split('/')))


def create_breadcrumbs(path, prefix):
    path = split_and_remove_empty(path)
    breadcrumbs = [{'name': 'Galleria', 'path': '/gallery/'}]

    for i, path_entry in enumerate(path):
        breadcrumbs.append(
            {'name': path_entry, 'path': prefix + '/'.join(path[:i+1])}
        )

    return breadcrumbs
