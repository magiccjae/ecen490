import shlex, subprocess
cmd = 'echo 200 > /sys/class/gpio/export'
output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )

cmd = 'echo out > /sys/class/gpio/gpio200/direction'
output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )

cmd = 'echo 1 > /sys/class/gpio/gpio200/value'
output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )




