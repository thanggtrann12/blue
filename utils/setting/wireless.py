import os
def check_ping():
    hostname = "google.com"
    response = os.system("ping  " + hostname)
    if response == 0:
        return True
    else:
        return False