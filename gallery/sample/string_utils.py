
def ensure_trailing_slash(string):
    if not string.endswith('/') and string != '':
        return string + '/'
    else:
        return string
