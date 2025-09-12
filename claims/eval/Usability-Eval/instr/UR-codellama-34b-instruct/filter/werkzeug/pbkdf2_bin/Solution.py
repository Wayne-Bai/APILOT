
import werkzeug
from werkzeug import security

# Generate PBKDF2 binary digest for given data and salt
digest = security.pbkdf2_bin(data, salt, iterations)
