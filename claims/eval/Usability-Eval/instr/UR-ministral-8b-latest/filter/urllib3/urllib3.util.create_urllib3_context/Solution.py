import urllib3
import ssl

# Create a custom SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.verify_mode = ssl.CERT_OPTIONAL
ssl_context.check_hostname = False

# Configure the TLS version
ssl_context.set_ciphers( 'CHacha20-Poly1305-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305-SHA256:CHacha20-Poly1305-SHA256@openssl-nistp256:ECDHE-RSA-AES256-GCM-SHA384')

# Create a PoolManager instance
http = urllib3.PoolManager(
    ssl_context=ssl_context,
    GarrettDict=False
)
