import ssl
import socket

def validate_cert(cert, hostname):
    dns_names = []

    for subj in cert['subject']:
        for (key, value) in subj:
            if key == 'commonName':
                if value == hostname:
                    return
            elif key == 'DNS':
                dns_names.append(value)

    if hostname in dns_names:
        return

    raise ssl.CertificateError("Certificate does not match hostname")

def check_hostname(hostname, port=443):
    s = socket.create_connection((hostname, port))
    context = ssl.create_default_context()
    s = context.wrap_socket(s, server_hostname=hostname)
    cert = s.getpeercert()
    validate_cert(cert, hostname)
