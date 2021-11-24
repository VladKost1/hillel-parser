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
    assert parse('https://youtube.com/?ivanguy=gorn&subscribe=true') == {'ivanguy': 'gorn', 'subscribe': 'true'}
    assert parse('https://youtube.com/?ivanguy=gorn&subscribe=true&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://youtube.com') == {}
    assert parse('https://youtube.com/?') == {}
    assert parse('https://youtube.com/?ivanguy=gorn') == {'ivanguy': 'gorn'}