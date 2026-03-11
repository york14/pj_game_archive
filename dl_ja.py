import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/cotes2020/jekyll-theme-chirpy/master/_data/locales/ja.yml'
url2 = 'https://raw.githubusercontent.com/cotes2020/jekyll-theme-chirpy/main/_data/locales/ja.yml'
try:
    with urllib.request.urlopen(url, context=ctx) as r:
        content = r.read().decode('utf-8')
        print(content)
except Exception as e:
    try:
        with urllib.request.urlopen(url2, context=ctx) as r:
            content = r.read().decode('utf-8')
            print(content)
    except Exception as e2:
        print(f"Failed: {e2}")
