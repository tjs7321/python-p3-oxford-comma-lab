def oxford_comma(items):
    if len(items) < 2:
        new_list = ''.join(items)
    elif len(items) == 2:
        new_list = ' and '.join(items)
    elif len(items) > 2:
        new_list = ', and '.join([', '.join(items[:-1]), items[-1]])
    return new_list