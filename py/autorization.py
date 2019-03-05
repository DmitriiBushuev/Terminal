from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen("http://127.0.0.1:5500/autorizationPage.html")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

inputTag = soup.find(attrs={"id" : "loginField"})
# inputTag = soup.select("input")

output = inputTag['value']

print(output)