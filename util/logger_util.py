import time
import socket
import requests
import ssl
import re
from random import choice
from string import ascii_uppercase

# remove warnings
# requests.packages.urllib3.disable_warnings(
#     requests.packages.urllib3.exceptions.InsecureRequestWarning
# )
requests.urllib3.disable_warnings()

# TODO: hostname in serializer and auth credentials as nested serializers


def get_dns_lookup_time(ip):
    """
    Returns the dns lookup time in seconds
    """
    try:
        start_time = time.time()
        socket.gethostbyaddr(ip)
        end_time = time.time()
        dns_lookup_time = end_time - start_time
        return dns_lookup_time

    except socket.gaierror as e:
        # handle DNS resolution errors
        print(ip, e)
        return None

    except:
        # handle other errors
        return None


def get_connection_time(
    hostname=None,
    ip=None,
    protocol="HTTPS",
    timeout=5,
    port=None,
    auth=None,
    headers=None,
):
    """
    Returns the connection time in seconds
    """
    try:
        # need either url or ip
        if hostname and ip:
            return None

        # set-up default port if empty
        if protocol == "HTTPS":
            default_port = 443
        elif protocol == "HTTP":
            default_port = 80
        elif protocol == "ICMP":
            return None  # ICMP doesn't require a connection, so return 0
        else:
            raise ValueError("Invalid protocol")

        if not port:
            port = default_port

        # prepare url
        url = f"{protocol.lower()}://"
        if hostname is None:
            url += f"{ip}:{port}"
        else:
            url += f"{hostname}"

        # add custom headers
        if headers is None:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        # add authentication headers
        if auth is not None:
            headers["Authorization"] = "Bearer " + auth

        # send requests
        start_time = time.time()
        requests.get(url=url, timeout=timeout, headers=headers)
        end_time = time.time()

        # calculate connection time
        connection_time = end_time - start_time

        return connection_time

    except requests.exceptions.RequestException as e:
        print(e)
        # handle connection errors
        return None

    except:
        # handle other errors
        return None


def get_ssl_handshake_time(
    hostname=None, ip=None, protocol="HTTPS", port=None, auth=None
):
    """
    Returns the ssl handshake time in seconds
    """
    try:
        # need either url or ip
        if hostname and ip:
            return None

        if protocol == "HTTPS":
            default_port = 443
        elif protocol == "HTTP":
            # default_port = 80 # SSL doesn't require SSL, so return None
            return None
        elif protocol == "ICMP":
            # ICMP doesn't require SSL, so return None
            return None
        else:
            raise ValueError("Invalid protocol")

        # when port isn't specified switch to default
        if not port:
            port = default_port

        username = None
        password = None
        if auth is not None:
            username = auth.get("username", None)
            password = auth.get("password", None)

        # start the timer
        start_time = time.monotonic()
        context = ssl.create_default_context()
        elapsed_time = 0
        if ip is None:
            url = f"{protocol.lower()}://{hostname}"
            with socket.create_connection((url, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=url) as ssock:
                    end_time = 0

                    if auth is None:
                        end_time = time.monotonic()
                    else:
                        # Send authentication data to the server
                        ssock.sendall(f"{username}:{password}".encode("utf-8"))
                        # Manually perform the SSL/TLS handshake
                        ssock.do_handshake()
                        end_time = time.monotonic()

                    elapsed_time = end_time - start_time
        else:
            with socket.create_connection((ip, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=ip) as ssock:
                    end_time = 0

                    if auth is None:
                        end_time = time.monotonic()
                    else:
                        # Send authentication data to the server
                        ssock.sendall(f"{username}:{password}".encode("utf-8"))
                        # Manually perform the SSL/TLS handshake
                        ssock.do_handshake()
                        end_time = time.monotonic()

                    elapsed_time = end_time - start_time
        return elapsed_time

    except ssl.SSLError as e:
        print(e)
        # handle SSL errors
        return None

    except:
        # handle other errors
        return None


def get_response_time_raw(
    hostname=None,
    ip=None,
    protocol="HTTPS",
    timeout=5,
    port=None,
    auth=None,
    headers=None,
):
    """
    Returns the response time in seconds
    """
    try:
        if ip and hostname:
            return None

        if protocol == "HTTPS":
            default_port = 443
        elif protocol == "HTTP":
            default_port = 80
        elif protocol == "ICMP":
            return None  # ICMP doesn't require a response, so return None
        else:
            raise ValueError("Invalid protocol")

        # prepare default port
        if not port:
            port = default_port

        # prepare url
        url = f"{protocol.lower()}://"
        if hostname is None:
            url += f"{ip}:{port}"
        else:
            url += f"{hostname}"

        # add custom headers
        if headers is None:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        # add authentication headers
        if auth is not None:
            headers["Authorization"] = "Bearer " + auth

        start_time = time.time()
        requests.get(url=url, timeout=timeout, headers=headers)
        end_time = time.time()

        response_time = end_time - start_time

        return response_time

    except requests.exceptions.RequestException as e:
        print(e)
        # handle connection errors
        return None

    except:
        # handle other errors
        return None


def get_status(
    hostname=None,
    ip=None,
    protocol="HTTPS",
    timeout=5,
    port=None,
    auth=None,
    headers=None,
    regex="200",
):
    """
    Returns the status depending the regex match
    """
    status_code = 404
    status = "DOWN"
    try:
        # need either url or ip
        if hostname and ip:
            return None

        # set-up default port if empty
        if protocol == "HTTPS":
            default_port = 443
        elif protocol == "HTTP":
            default_port = 80
        elif protocol == "ICMP":
            return None  # ICMP doesn't require a connection, so return 0
        else:
            raise ValueError("Invalid protocol")

        if not port:
            port = default_port

        # prepare url
        url = f"{protocol.lower()}://"
        if hostname is None:
            url += f"{ip}:{port}"
        else:
            url += f"{hostname}"

        # add custom headers
        if headers is None:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        # add authentication headers
        if auth is not None:
            headers["Authorization"] = "Bearer " + auth

        # send requests
        start_time = time.time()
        response = requests.get(url=url, timeout=timeout, headers=headers)
        status_code = response.status_code
        end_time = time.time()

        # calculate connection time
        connection_time = end_time - start_time

        return connection_time

    except requests.exceptions.RequestException as e:
        print(e)
        # handle connection errors
        status_code = 0

    except:
        # handle other errors
        status_code = 0

    finally:
        if re.search(regex, str(status_code)):
            return "OK"
        else:
            return "DOWN"


def generate_token(token_size=24):
    """
    Generate an alphanumeric token for a given token size
    """
    token = "".join(choice(ascii_uppercase) for i in range(token_size))
    return token


def process_endpoint(endpoint):
    """
    Get response time
    Get "OK or Down or Unknown" status
    """
    response_time = -1
    match = False
    message = ""
    context = {}
    response = None
    try:
        headers = (
            {
                endpoint.request_handler.header_name: endpoint.request_handler.header_value
            }
            if endpoint.request_handler.header_name
            and endpoint.request_handler.header_value
            else {}
        )
        body = endpoint.request_handler.body if endpoint.request_handler.body else {}
        auth = (
            (
                endpoint.request_handler.auth_username,
                endpoint.request_handler.auth_password,
            )
            if endpoint.request_handler.auth_username
            and endpoint.request_handler.auth_password
            else None
        )

        response = requests.request(
            method=endpoint.request_handler.method,
            url=endpoint.url,
            headers=headers,
            data=body,
            auth=auth,
            timeout=endpoint.timeout,
            verify=endpoint.request_handler.verify_ssl,
        )

        response_time = response.elapsed.total_seconds()

        regex = endpoint.regex

        match = (
            re.search(regex, str(response.status_code))
            if endpoint.logger_type == "status"
            else re.search(regex, str(response.content))
        )

        message = "Request sent successfully."

    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        message = "Request timed out. Try exceeding the timeout limit."
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        message = "Request exceeds the configured number of maximum redirections. Try a different URL."
    except requests.exceptions.ConnectionError:
        # Network problem (DNS failure, refused connection, etc)
        message = "Request couldn't be fulfilled. URL connection refused."
    except requests.exceptions.HTTPError:
        # Invalid HTTP response or regular unsuccesful
        message = "HTTP response is invalid. Please try with a different URL."
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        message = "Request couldn't be fulfilled. URL connection refused."
    finally:
        # prepare a context object
        context = {
            "response_time": response_time,
            "status": "UP" if match else "DOWN",
            "message": message,
        }

        if not match:
            context["response_body"] = response
            # TODO: prepare a screenshot queue

    return context
