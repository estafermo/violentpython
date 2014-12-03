import pxssh

def send_command(s, cmd):
	s.sendline(cmd)
	s.prompt()
	print s.before
def connect(host, user, password):
	try:
		s = pxssh.pxssh()
		s.login(host, user, password)
		return s
	except:
		print '[-] Error Connecting'
		exit(0)
		
def main():
	#host = '192.168.1.93'
	host='127.0.0.1'
	user = 'moron'
	password = 'moron1'
	s = connect(host, user, password)
	send_command(s, 'whoami')
if __name__ == '__main__':
	main()
