import shlex, subprocess
import time
cmd = 'echo 0 > /sys/class/gpio/gpio200/value'
output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )
time.sleep(.01)
cmd = 'echo 1 > /sys/class/gpio/gpio200/value'
output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )
