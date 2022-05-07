status_rec = ""

def set_status(status):
    global status_rec
    status_rec = str(status)

def get_status_info():
  global status_rec
  return status_rec