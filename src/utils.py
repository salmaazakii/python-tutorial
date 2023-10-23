def find_max(_list):
    _max = _list[0]
    for number in _list:
        if number > _max:
            _max = number
    return _max
