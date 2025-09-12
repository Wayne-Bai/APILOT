import datetime
from cryptography import x509

# Create a certificate object
cert = x509.load_pem_x509_certificate(open('path/to/your/certificate.pem', 'rb').read())

# Get the CRL distribution point extension
crl_distribution_point = cert.extensions.get_extension_for_oid(x509.OID_CRL_DISTRIBUTION_POINTS)

# Extract the URL of the CRL distribution point
url = crl_distribution_point.value.full_name[0].value

# Get the current time and add 24 hours to it
current_time = datetime.datetime.now()
future_time = current_time + datetime.timedelta(hours=24)

# Create a new CRL object with the updated next update time
new_crl = x509.CRLBuilder(
    cert,  # The certificate to which the CRL belongs
    url,   # The URL of the CRL distribution point
    future_time,  # The new next update time
)

# Create a PEM-encoded string for the updated CRL
new_crl_pem = new_crl.build(x509.PEM_TYPE)
