import threading

def testTime():
	print("Time to learn Pyhton!! bye...")

timer = threading.Timer(3.0, testTime)

timer.start()