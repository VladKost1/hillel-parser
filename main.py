def parse_cookie(query):
    par2 = query.split(';')
    result = {}
    for i in par2:
        if i:
            k, v = i.split('=', 1)
            result[k] = v
    return result

if __name__ == '__main__':

    assert parse_cookie('name=Vlad=User;age=20;') == {'name': 'Vlad=User', 'age': '20'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Vlad;age=20;') == {'name': 'Vlad', 'age': '20'}
    assert parse_cookie('name=Vlad;') == {'name': 'Vlad'}
    assert parse_cookie('age=20') == {'age': '20'}