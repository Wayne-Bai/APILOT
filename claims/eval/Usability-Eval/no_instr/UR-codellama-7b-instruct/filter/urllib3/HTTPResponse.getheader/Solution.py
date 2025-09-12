
import urllib.request as urllib

response = urllib.urlopen('https://www.example.com')

print(response.info()['Content-Type'])
