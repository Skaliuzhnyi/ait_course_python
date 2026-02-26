def make_url(host, port=80, https=False):
    scheme = 'https' if https else 'http'
    return f"{scheme}://{host}:{port}"
    
print(make_url('example.com', 443, True))
print(make_url('example.com'))
print(make_url('example.com', https=True))
