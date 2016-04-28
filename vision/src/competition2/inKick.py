import shlex, subprocess
cmd = 'echo 1 > /sys/class/gpio/gpio200/value'
output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )
