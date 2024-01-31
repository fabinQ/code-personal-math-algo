#!/usr/bin/python3
import time
import datetime
import signal

def exit_handler(sig, frame):
	signame = signal.Signals(sig).name
	#print(f'Signal handler called with signal {signame} ({sig})')
	print("Signal recive: ",sig)
	exit()

for sig in signal.Signals:
	print(sig,signal.Signals(sig).name)
	signal.signal(sig, exit_handler)
exit()

while True:
	print(datetime.datetime.now(),"Import transaction")
	time.sleep(1)
	print(datetime.datetime.now(),"Finish transaction")
