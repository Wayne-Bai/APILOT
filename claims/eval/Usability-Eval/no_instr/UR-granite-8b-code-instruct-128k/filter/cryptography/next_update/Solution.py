from cryptography import datetime

def get_next_crl_update_time():
    next_update_time = datetime.datetime.now() + datetime.timedelta(days=30)
    return next_update_time

next_update_time = get_next_crl_update_time()
print(next_update_time)
