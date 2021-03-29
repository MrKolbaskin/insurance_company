def parse_begin_info(values):
    res = {}
    res['max_events'] = {}
    res['contracts_info'] = {}
    res['random_count'] = {}
    for key in values:
        ind = key.find('.')
        if ind != -1:
            name_obj = key[:ind]
            name_field = key[ind + 1:]
            if name_field == 'max_events':
                res['max_events'][name_obj] = int(values[key])
                continue
            if name_field == 'random_count':
                res['random_count'][name_obj] = int(values[key])
                continue
            if name_obj not in res['contracts_info']:
                res['contracts_info'][name_obj] = {}
            res['contracts_info'][name_obj][name_field] = int(values[key])
        else:
            res[key] = int(values[key])
    return res