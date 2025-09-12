import urllib3

https = urllib3.PoolManager(
    verify_mode=urllib3.security.verify.CERT_REQUIRED,
    certfile='/etc/ssl/certs/ca-certificates.crt',
    server_hostname='example.com'
)

http = urllib3.PoolManager(
    verify_mode=urllib3.security.verify.CERT_NONE,
    certfile='/etc/ssl/certs/ca-certificates.crt',
    server_hostname='example.com'
)
