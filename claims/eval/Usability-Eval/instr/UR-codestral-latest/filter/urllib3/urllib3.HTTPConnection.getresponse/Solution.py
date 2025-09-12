import urllib.request

req = urllib.request.Request('http://www.example.com')  # replace with your URL

with urllib.request.urlopen(req) as response:
    the_page = response.read()  # read the content of the server's response

print(the_page)
