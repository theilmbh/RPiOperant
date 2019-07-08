from pyoperant.local_pi import PiPanel
import time

test = PiPanel()

print("Turning on House light")
test.house_light.on()

time.sleep(2)
print("Feeding..")
try:
	test.hopper.feed()
except:
	print("hopper error")

time.sleep(2)
test.hopper.down()

print("Test center peck ports..")
while not test.center.status():
	print("waiting..")
	time.sleep(0.25)

time.sleep(1)
print("Test right peck ports..")
while not test.right.status():
	print("waiting..")
	time.sleep(0.25)

time.sleep(1)
print("Test left peck ports..")
while not test.left.status():
	print("waiting..")
	time.sleep(0.25)

print("Tests complete")
test.house_light.off()
