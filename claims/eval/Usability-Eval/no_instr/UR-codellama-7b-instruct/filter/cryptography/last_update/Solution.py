
import cryptography
from cryptography import x509

# Parse the certificate and extract the information
certificate = x509.load_pem_x509_certificate(open('certificate.pem', 'rb').read())
crl = cryptography.x509.load_pem_x509_crl(open('crl.pem', 'rb').read())

# Get the last update time of the CRL
last_update_time = crl.last_update
