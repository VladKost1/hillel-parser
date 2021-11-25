def parse(query):
    if '?' not in query:
        return {}
    par1 = query.split("?")[1]
    par1 = par1.split("&")
    result = {}
    for p in par1:
        if p:
            k, v = p.split('=')
            result[k] = v
    return result


if __name__ == '__main__':

    # Testing function `parse`
    assert parse('https://youtube.com/?ivanguy=me&subscribe=true') == {'ivanguy': 'me', 'subscribe': 'true'}
    assert parse('https://youtube.com/?ivanguy=me&subscribe=true&') == {'ivanguy': 'me', 'subscribe': 'true'}
    assert parse('https://youtube.com') == {}
    assert parse('https://youtube.com/?') == {}
    assert parse('https://youtube.com/?&&&') == {}
    assert parse('https://youtube.com/?ivanguy=me') == {'ivanguy': 'me'}
    assert parse('https://youtube.com/?vlad=kost') == {'vlad': 'kost'}
    assert parse('https://youtube.com/?vlad=kost&age=20') == {'vlad': 'kost', 'age': '20'}
    assert parse('https://youtube.com/?vlad=kost&age=20&&') == {'vlad': 'kost', 'age': '20'}
    assert parse('https://youtube.com/?vlad=kost&age=20???') == {'vlad': 'kost', 'age': '20'}
