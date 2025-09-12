from datetime import datetime
import cryptography.x509

def get_revocation_date(certificate):
    """
    Returns a naïve datetime representing the date this certificate was revoked, if any.
    If the certificate has not been revoked, returns None.
    """
    # Check if the certificate has a CRL distribution point (CDP) extension
    cdps = cryptography.x509.extensions.CRLDistributionPoints.from_certificate(certificate)
    for cdp in cdps:
        # Check if the CDP has a revocation reason (reasonCode) extension
        reasons = cdp.extensions.get_extension_for_oid(cryptography.x509.extensions.ReasonFlags.OID).value
        if not reasons:
            continue
        for reason in reasons:
            # Check if the revocation reason is a revocation date (3.2.1.7.2)
            if reason == 3:
                # Return the revocation date from the CRL entry
                return datetime.strptime(cdp.full_name, '%Y%m%d%H%M%SZ')
    return None
