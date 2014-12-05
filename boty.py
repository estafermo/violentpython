import optparse
import pxssh

botNet = []
class Client:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()
	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			print 'user: '+self.user
			return s
		except Exception, e:
			print e
			print '[-] Error Connecting'
	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def botnetCommand(command):
	for client in botNet:
		output = client.send_command(command)
		print '[*] Output from ' + client.host
		print '[+] ' + output + '\n'
def addClient(host, user, password):
	client = Client(host, user, password)
	botNet.append(client)
	
			
def main():
	print 'a'
	
	addClient('127.0.0.1', 'moron', 'moron1')
	addClient('127.0.0.1', 'cro', 'adsada')
	botnetCommand('uname -v')
	botnetCommand('cat /etc/issue')			

		
if __name__ == '__main__':
	main()
