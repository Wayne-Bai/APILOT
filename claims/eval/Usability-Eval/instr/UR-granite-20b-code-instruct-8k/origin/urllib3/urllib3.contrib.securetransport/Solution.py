import urllib3

# Enable platform-native TLS on macOS
urllib3.contrib.pyopenssl.inject_into_urllib3()
