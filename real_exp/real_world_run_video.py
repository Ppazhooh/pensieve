import os
import sys
import signal
import subprocess
from time import sleep

abr_algo = sys.argv[1]
run_time = int(sys.argv[2])
exp_id = sys.argv[3]


for i in range(0,100):
	try:
		command1 = 'kill -9 $(lsof -t -i:8333)'
		if abr_algo == 'RL':
			command = 'exec  ~/anaconda3/envs/py2/bin/python2.7 ../rl_server/rl_server_no_training.py ' + exp_id
		elif abr_algo == 'fastMPC':
			command = 'exec  ~/anaconda3/envs/py2/bin/python2.7 ../rl_server/mpc_server.py ' + exp_id
		elif abr_algo == 'robustMPC':
			command = 'exec  ~/anaconda3/envs/py2/bin/python2.7 ../rl_server/robust_mpc_server.py ' + exp_id
		else:
			command = 'exec  ~/anaconda3/envs/py2/bin/python2.7 ../rl_server/simple_server.py ' + abr_algo + ' ' + exp_id
		
		proc1 = subprocess.Popen(command1, shell=True)
		sleep(1)
		proc1.kill()
		proc = subprocess.Popen(command, shell=True)
		sleep(2)
		sleep(run_time)
		print 'done'
		proc.send_signal(signal.SIGINT)
		
	except Exception as e:
		try:
			proc.send_signal(signal.SIGINT)
		except:
			pass
		
		print e	

