import threading
import time
from flask import g

from werkzeug.local import Local


class A:
    b = 1


my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print('in new thread b is:' + str(my_obj.b))


new_t = threading.Thread(target=worker, name='carr')
new_t.start()
time.sleep(1)

print(my_obj.b)
