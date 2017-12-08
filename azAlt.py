from sense_hat import SenseHat
import calcs

sense = SenseHat()

while True:
	ori = sense.get_orientation_degrees()
	yaw = ori["yaw"]
	pitch = ori["pitch"]
	az = calcs.grad_min_sec_azimuth(yaw)
	alt = calcs.grad_min_sec(pitch)

	print(chr(27) + "[2J")
	print "Azimuth: ", yaw
	print "Azimuth Delta: ", calcs.yawNeg
	print "Corrected Azimuth: ", az
	print "Corrected Altitude:", alt