import random
import time

def randdate(start, end):
    print(start,end)
    randgen = random.random()
    format  = '%d/%m/%Y'
    startt  = time.mktime(time.strptime(start, format))
    endt    = time.mktime(time.strptime(end  , format))
    randt   = startt + randgen * (endt-startt)
    randd   = time.strftime(format, time.localtime(randt))
    return randd
print(randdate("1/1/2020","12/12/2024"))