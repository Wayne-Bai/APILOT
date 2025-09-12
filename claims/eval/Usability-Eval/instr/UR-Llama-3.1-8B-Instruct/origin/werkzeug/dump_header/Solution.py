# Create an instance of Headers class. This will be used to build the HTTP Header
headers = Headers()

# Add key-value pairs to build the HTTP Headers
headers.add('Content-Type', 'application/json')
headers.add('Authorization', 'Bearer your_token_here')

# Dump the HTTP Headers
print(headers)

# You can also use the to_str() method to dump the headers
print(headers.to_str())

# You can use the headers to get any specific header value
print(headers.get('Content-Type'))

# You can also iterate over the headers dictionary
for key, value in headers:
    print(f"{key}: {value}")
    
# You can also access all the values using the MultiDict class. This part of Werkzeug library handles all the key-value pairs  
print(headers.raw_list)
