import datetime

def get_next_update(crl):
    # Extract the nextUpdate field from the CRL
    next_update = crl.get('tbsCertList').get('nextUpdate')

    # Parse the ASN.1 time value into a Python datetime object
    next_update = asn1_parse(next_update)

    return next_update
