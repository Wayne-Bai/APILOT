from cryptography import x509
from datetime import datetime

# Create the subject
def create_subject(name, organization, country):
    subject = x509.subject_name.SubjectComponentsBuilder()
    subject.common_name(name)
    subject.locality(organization)
    subject.country(country)
    return subject

# Create the issuer
def create_issuer(name, organization, country):
    issuer = x509.issuer_name.SubjectComponentsBuilder()
    issuer.common_name(name)
    issuer.locality(organization)
    issuer.country(country)
    return issuer

# Create the certificate version
def create_certificate_version():
    return x509.NameOIDCertificateVersion.__version__

# Create the notBefore date
def create_not_before_date(value):
    return x509.certificate.SubjectAndIssuerBuilder().not_before(datetime.strptime(value, "%Y-%m-%d"))

# Create the notValid date
def create_not_valid_date(value):
    return x509.certificate.SubjectAndIssuerBuilder().not_valid_after(datetime.strptime(value, "%Y-%m-%d"))

# Example of generate a certificate with details
def generate_certificate(name, organization, country, not_before, not_valid, issuer_name):
    subject = create_subject(name, organization, country)
    issuer = create_issuer(name, organization, country)
    version = create_certificate_version()
    not_before = create_not_before_date(not_before)
    not_valid = create_not_valid_date(not_valid)

    # Put it all together: the issuer and subject, and then add it
    x509_cert = x509.certificate.CertificateBuilder().subject_name(subject).issuer_name(issuer)\
        .serial_number(x509.random_length_serial_number()).not_before(not_before).not_valid_after(not_valid)\
        .add_extension(x509.SubjectAltName([x509.DNSName(issuer_name)]), critical=False).\
        add_extension(x509.KeyUsage(
            digital_signature=True,
            key_encipherment=True,
            key_cert_sign=True,
            data_certification=False,
        ), critical=False).add_extension(x509.ExtendedKeyUsage([x509.OID_EXTENDED_KEY_USAGE_SERVER_AUTH])).\
        public_key(2048, ('x25519')).subject_alt_name([x509.DNSName(issuer_name)])\
        .sign(issuer, private_key)

    return x509_cert

# Example
cert = generate_certificate('Alice Smith', 'MyCorporation', 'US', '2023-08-01', '2023-08-31', 'alice-corp.com')
