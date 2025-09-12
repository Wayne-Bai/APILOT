
import urllib3

def verify_cert(cert, hostname):
    # RFC 2818 and RFC 6125 rules:
    # - SubjectAltName must be present in the certificate
    # - The most specific SubjectAltName (i.e., longest matching IP address or FQDN) must be used
    # - Avoid using outdated APIs
    
    # Check if SubjectAltName is present in the certificate
    if 'subjectAltName' not in cert:
        raise CertificateError('SubjectAltName not found in certificate')
    
    # Get the most specific SubjectAltName (i.e., longest matching IP address or FQDN)
    alt_names = cert['subjectAltName']
    alt_name = max(alt_names, key=lambda x: x[0])[1]
    
    # Check if the hostname matches the SubjectAltName
    if not fnmatch.fnmatch(hostname, alt_name):
        raise CertificateError('Hostname does not match SubjectAltName')
