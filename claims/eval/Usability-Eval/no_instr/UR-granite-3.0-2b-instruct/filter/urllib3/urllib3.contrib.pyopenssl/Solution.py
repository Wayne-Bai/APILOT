import urllib3

def create_http_pool_manager(PoolManager, timeout=None):
    """
    Create an HTTP PoolManager with the given timeout.

    :param PoolManager: The PoolManager class from urllib3.
    :param timeout: The connection timeout in seconds.
    :return: A new PoolManager instance.
    """
    if timeout is None:
        timeout = PoolManager.default_timeout
    return PoolManager(timeout=timeout)

def create_http_session(Session, pool_manager, timeout=None):
    """
    Create an HTTP Session with the given PoolManager and timeout.

    :param Session: The Session class from urllib3.
    :param pool_manager: The PoolManager instance.
    :param timeout: The connection timeout in seconds.
    :return: A new Session instance.
    """
    if timeout is None:
        timeout = Session.default_timeout
    return Session(pool_manager, timeout=timeout)

def create_http_connection(http_session, timeout=None):
    """
    Create an HTTP connection with the given Session and timeout.

    :param http_session: The Session instance.
    :param timeout: The connection timeout in seconds.
    :return: A new HTTP connection.
    """
    if timeout is None:
        timeout = http_session.default_timeout
    return http_session.connect(timeout=timeout)

def create_http_request(http_connection, method, url, **kwargs):
    """
    Create an HTTP request with the given method, URL, and kwargs.

    :param http_connection: The HTTP connection.
    :param method: The HTTP method (e.g., GET, POST).
    :param url: The URL to send the request to.
    :param kwargs: Additional keyword arguments for the request.
    :return: An HTTP request object.
    """
    return http_connection.request(method, url, **kwargs)

def send_http_request(http_request, **kwargs):
    """
    Send an HTTP request and return the response.

    :param http_request: The HTTP request object.
    :param kwargs: Additional keyword arguments for the request.
    :return: The HTTP response.
    """
    return http_request.send(**kwargs)
