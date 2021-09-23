from datetime import datetime

def timestamp():
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    return date

time = timestamp()
print(time)
