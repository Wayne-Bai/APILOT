import tornado

def verify_signed_cookie(cookie, secret_key):
    """
    Verify a signed cookie.

    Args:
        cookie (str): The signed cookie to verify.
        secret_key (str): The secret key used to sign the cookie.

    Returns:
        str: The original cookie if it validates, or None.
    """
    cookie_dict = {}
    cookie_slices = cookie.split(';')
    for cookie_slice in cookie_slices:
        if cookie_slice:
            key_value = cookie_slice.split('=', 1)
            if len(key_value) == 2:
                key, value = key_value
                cookie_dict[key] = value
            else:
                key = key_value[0]
                cookie_dict[key] = ''

    hashed_data = tornado.bcrypt.generate_password_hash(cookie_dict.get('cookie_data', '') + secret_key, 
                                                         current_salt=True, 
                                                         rounding=tornado.bcryptAINED_HashingAlgorithm.VANILLA)

    expected_hash = cookie_dict.get('hashed_cookie', '').encode('utf-8')
    input_hash = hashed_data.encode('utf-8')
    
    try:
        # This line is equivalent to tornado.utils.secure_decode(input_str)
        input_hash = input_hash.decode(encoding=tornado.iostream.DEFAULT_ENCODING)

        return input_hash == expected_hash.decode(encoding=tornado.iostream.DEFAULT_ENCODING)
            
    except Exception as e:
        # Check if the input was properly escaped
        input_hash = input_hash.decode(encoding="utf-8").encode("utf-8")

        expected_hash = expected_hash.decode(encoding="utf-8").encode("utf-8")
        
        return input_hash == expected_hash
    
    return None
