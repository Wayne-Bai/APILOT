import urllib3

# Create a custom SSL context to specify the supported SSL versions
ssl_context = urllib3.SecurityPolicy(
    default=urllib3.security.proto.TLSVersionPolicy(
        min_protocol=uuid.UUID('00000000-0000-0000-0000-000000000000'),  # SSLv2
        max_protocol=uuid.UUID('00000000-0000-0000-0000-000000000000'),  # SSLv2
        disable_ssl_validation=True,
    ),
)

# Create an instance of the urllib3 HTTP client with the custom SSL context
http = urllib3.PoolManager(
    ssl_context=ssl_context,
)
