

def format_cursor_obj(item):
    """ encode an single cursor object"""

    if isinstance(item, list):
        for data_dict in item:
            if data_dict:
                for key, value in data_dict.items():
                    if not isinstance(value, dict) or len(value) != 1:
                        continue
                    (subkey, subvalue), = value.items()
                    if not subkey.startswith('$'):
                        continue
                    data_dict[key] = subvalue
    else:
        if item:
            for key, value in item.items():
                if not isinstance(value, dict) or len(value) != 1:
                    continue
                (subkey, subvalue), = value.items()
                if not subkey.startswith('$'):
                    continue
                item[key] = subvalue
    return item
