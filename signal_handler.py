#!/usr/bin/python3
import time
import datetime
import signal
signal_status = 0


def exit_handler(sig, frame):
	print("Signal recive: ",sig)
	global signal_status
	signal_status = sig
	#exit()

for sig in signal.Signals:
	print(sig.value,signal.Signals(sig).name)
	signal.signal(signal.SIGTERM, exit_handler)
	#if sig == 9 or sig == 19 :continue
	#signal.signal(sig, exit_handler)


while True:
	print(datetime.datetime.now(),"Import transaction", signal_status)
	time.sleep(1)
	print(datetime.datetime.now(),"Finish transaction",signal_status)
	if signal_status  != 0:
		print("Grace exit")
		exit()
