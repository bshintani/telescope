from sense_hat import SenseHat
import math
import time

#set the variable for which we subtract from degs to correct North
sense = SenseHat()
yawArray = []
x = 0
print "Calibrating..."
while (x <= 99):
    ori = sense.get_orientation_degrees()
    yaw = ori["yaw"] #current yaw reading in degrees
    time.sleep(.15)
    yawArray.append(yaw)
    x = x + 1
    
yawArraySum = sum(yawArray)
yawArrayAvg = yawArraySum / len(yawArray) 
yawNeg = yawArrayAvg * -1.00

## From degrees in float format, to a list with number of degrees, minutes and seconds
#
# \param degs Degrees in float format
# \return List with (degrees, minutes, seconds)
def grad_min_sec(degs):
    to_neg = False
    if degs < 0:
        degs = math.fabs(degs)
        to_neg = True

    degrees = int(math.floor(degs)) 
    degs_m = (degs - degrees)*60.0
    minutes = int(math.floor(degs_m))
    seconds = int((degs_m - minutes)*60.0)

    if seconds >= 59.99:
        seconds = 0
        minutes += 1
    if minutes >= 60.0:
        minutes = 60.0-minutes
        degrees += 1

    if to_neg:
        degrees = -degrees;

    return (degrees, minutes, seconds)

def grad_min_sec_azimuth(degs):
    corrDegs = degs + yawNeg
    degrees = int(math.floor(corrDegs))
    degs_m = (corrDegs - degrees)*60.0
    minutes = int(math.floor(degs_m))
    seconds = int((degs_m - minutes)*60.0)

    if seconds >= 59.99:
        seconds = 0
        minutes += 1
    if minutes >= 60.0:
        minutes = 60.0-minutes
        degrees += 1

    return (degrees, minutes, seconds)