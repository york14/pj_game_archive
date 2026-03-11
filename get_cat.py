import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/cotes2020/jekyll-theme-chirpy/master/_tabs/categories.md'
try:
    with urllib.request.urlopen(url, context=ctx) as r:
        print(r.read().decode('utf-8'))
except Exception as e:
    print(e)
