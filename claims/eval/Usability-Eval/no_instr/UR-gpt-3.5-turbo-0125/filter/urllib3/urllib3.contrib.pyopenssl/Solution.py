
import urllib3

urllib3.util.ssl_.DEFAULT_CIPHERS = 'HIGH:!DH:!aNULL'
urllib3.util.ssl_.DEFAULT_SSLLIB = "openssl"
