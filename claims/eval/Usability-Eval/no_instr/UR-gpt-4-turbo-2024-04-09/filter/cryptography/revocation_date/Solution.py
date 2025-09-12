from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Sample PEM data for a CRL; replace this string with your actual CRL data
pem_data = """
-----BEGIN X509 CRL-----
MIIBYzCBzDANBgkqhkiG9w0BAQsFADA6MTgwNgYDVQQDDC9FbWFpbCBQcm90ZWN0
aW9uIENlcnRpZmljYXRlIEF1dGhvcml0eTELMAkGA1UEBhMCVVMXDTIwMDExNDE4
MjUwMFoXDTIxMDExMzE4MjUwMFowJzAlAhQdihBk9JxxgV0UtzaloM/G9RcNMTkw
NzE3MDAwMDAwWjANBgkqhkiG9w0BAQsFAAOCAQEAYR1tWJlJ+3Ql5B5r9b8W8jG3
spDLLzc4IU6iYt3FUcmsELZGQz7ywvwRzI2ZVOQXMCteH+komwtY+2x6YAhLZNnS
SB3s1R5EiZ6C6wYuPuMAD2Vc47X2mYY4HCTzqu/9ePC3OHM2XR1CxRsDRaK55DLO
LFSHCPDGj9LlZaec3kaZIbVwonnXfEsYSS3ybihZnp/JX8Hg4bPbZMB1c8YThvHa
JVpHyWqgWF9gz75x+yPamj5k5dpesFZxADH6g6N9MraOiLz4JVZzLvcU4lrPLNXp
cFwafuDrJ3OwYgnVcihciMk465iFf7Os6spbWU0f0nRAoGTXB/mzSk9KgUWCdDCC
AjYwggErBgkqhkiG9wKIbzCCAhMCAQEwfzB5MQswCQYDVQQGEwJVUzETMBEGA1UE
ChMKRGlnaUNlcnQgSW5jMTUwMwYDVQQDEyx
-----END X509 CRL-----
"""

# Load the CRL
crl = x509.load_pem_x509_crl(pem_data.encode('utf-8'), default_backend())

# Print the revocation date for each revoked certificate in the CRL
for revoked_cert in crl:
    print("Serial number:", revoked_cert.serial_number)
    print("Revocation date:", revoked_cert.revocation_date)
