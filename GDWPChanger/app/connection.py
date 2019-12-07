def is_connected():
    from socket import create_connection
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
        return False
if __name__ == '__main__':
    #is_connected()
    print("I'm here")
