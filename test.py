import os
def check_ping():
    hostname = "google.com"
    response = os.system("ping  " + hostname)
    # and then check the response...
    if response == 0:
        return True
    else:
        return False


print(check_ping())