
import math
import datetime
import time
# import sys
import signal




ISO_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
start = time.time()
duration = -1

def sigterm_handler(signum, frame):
    global duration
    print 'Signal caught (%d): Exiting' % signum
    duration=0

signal.signal(signal.SIGTERM, sigterm_handler)

while True:
    datetimenow = datetime.datetime.now()
    now=time.time()

    GMstamp = time.strftime(ISO_DATE_FORMAT,time.gmtime(time.time())) 
    print "%s --- %s  %d" % (datetimenow,GMstamp,duration) 

    now=time.time()
    if duration>=0 and (now-start)>duration:
        break

    # sleep to hit the second on the nose:
    (frac,dummy) = math.modf(now)
    desiredFractionalOffset = .1
    delay = 1-frac + desiredFractionalOffset
    time.sleep(delay)

print "Done; lasted %f" % (time.time()-start)
