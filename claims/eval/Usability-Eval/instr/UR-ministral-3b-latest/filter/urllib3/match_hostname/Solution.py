from urllib3 import utils

def verify_certificate(hostname, cert):
    decoded_cert = utils.socketutils.ssl.getpeercert(cert)
    if decoded_cert:
        subject = decoded_cert.get('subject', {})
        common_name = next((v for v in subject if v[0] == 'CN'), None)
        if common_name:
            common_name = str(common_name[1])
            if common_name.lower() == hostname.lower():
                return
    raise CertificateError("Hostname mismatch or certificate error")

