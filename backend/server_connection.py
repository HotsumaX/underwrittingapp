"""Module to handle server connections."""



import requests


def check_server_connection(url):
    """
    Check the server connection by making a GET request.

    Args:
        url (str): The URL to check the connection.

    Returns:
        str: The status of the server connection.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "Server is up!"
        return f"Server returned status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error connecting to server: {e}"
