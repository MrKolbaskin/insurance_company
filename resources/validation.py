def validate_field(val_dict, value, key, begin_seq=1, end_seq=None):
    if not value:
        val_dict[f'{key}.num'] = True
        return
    
    if not value.isnumeric():
        val_dict[f'{key}.num'] = True
        return
    
    if begin_seq and int(value) < begin_seq:
        val_dict[f'{key}.seq'] = True
    
    if end_seq and int(value) > end_seq:
        val_dict[f'{key}.seq'] = True


def validation(values):
    res = {}
    for key in values:
        begin_seq = 1
        end_seq = None
        if key == 'm':
            begin_seq = 6
            end_seq = 24
        elif key == 'tax':
            begin_seq = 0
            end_seq = 100
        elif key == 'duration':
            begin_seq = 1
            end_seq = 24
            
        validate_field(res, values[key], key, begin_seq=begin_seq, end_seq=end_seq)
    
    return res