import paramiko, base64
import time
import socket
import gssapi, pyasn1
import sys
import getpass
from socket import timeout, gaierror
from paramiko.ssh_exception import (
    SSHException, BadHostKeyException, NoValidConnectionsError
)

target = ""
username = ""
password = ""
if len(sys.argv) == 3:
	username = sys.argv[1]
	target = sys.argv[2]
	password = getpass.getpass('Password:')
elif len(sys.argv) > 3:
	print("Too many arguments\n")
	exit()
elif len(sys.argv) < 3:
	print("Include a Sunet ID to search for")
	exit()

for i in range(1, 33):
	try:
		key = paramiko.RSAKey(data=base64.decodestring('AAAAB3NzaC1yc2EAAAABIwAAAQEAzBGOI2HrympIZLVT1oETmeeVu5T9ZvyqOdIlIRqxKQp4wWo8vvCmNHCWTtzQiHic4ypoaduW0hayPPJcCE2a8k9Yt0iqm5UqePhebyRaIVH3wSKdESk4KX0BJX8f43xWk4KkUT/lOK0EGD3/tlEM/70T8vLbRyNprrGBedhHLpbMocv+2XbWCb2wQzTW7oy4x0fiBXDPK2iUDIAG0WMbG6LDCjljsJZPna8chW6voxzXMujhLS2fJY1puZ7ELbHM18NfXxAmNpVWR6smEc+VaSEOMdod63NJh6qYTZFamnjhGXGRWRzoaMT3V99Rl1/o9eMrCZdGWUBIBu6ImcL5Tw=='))
		client = paramiko.SSHClient()
		client.get_host_keys().add('myth%d.stanford.edu' % i, 'ssh-rsa', key)
		client.connect('myth%d.stanford.edu' % i, timeout=.5, username=username, password=password)
	except (NoValidConnectionsError, timeout, gaierror, SSHException):
		continue
	print("Searching myth machine %d for %s" % (i, target))
	stdin, stdout, stderr = client.exec_command('./repub %s' % target)
	# for line in stdout:
	    # print '... ' + line.strip('\n')
	    # if line.strip('\n').find("nevenwt") >= 0:
	    # 	print("Found nevenwt on myth machine %d" % i)
	    # time.sleep(int(line.strip('\n')))
	# time.sleep(2)
	client.close()