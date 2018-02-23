import base64
import argparse

def input_to_config(host, user, passwd, path):
	try:
		with open(path + '/config.ini','a') as write_config:
			write_config.write('Hostname:' + host.rjust(len(host)+4) + '\n')
			write_config.write('Username:' + user.rjust(len(user)+4) + '\n')
			encoded_passwd = base64.encodestring(passwd)
			write_config.write('Password:' + encoded_passwd.rjust(len(encoded_passwd)+4) + '\n')
	except Exception as e:
		print (e)

def read_from_config(host, path):
	try:
		with open(path + '/config.ini','r') as read_config:
			file_content = read_config.readlines()
			flag = False
			for index, lines in enumerate(file_content):
				if host in lines:
					flag = True
					for req_lines in file_content[index : index+3]:
							if 'Password' not in req_lines: print(req_lines)
							else:
								encoded_passwd = req_lines.split(':')[1].strip()
								decoded_passwd = base64.decodestring(encoded_passwd)
								print(req_lines.split(':')[0].strip() + ':' + decoded_passwd.rjust(len(decoded_passwd)+4))
			if flag == False: print('No such hostname found.')
	except Exception as e:
		print (e)
			
def argument_parse():
	arguments = argparse.ArgumentParser()
	group = arguments.add_mutually_exclusive_group()
	group.add_argument('--save',action='store_true',help='Save credentials to a file')
	group.add_argument('--retrieve',action='store_true',help='Retrieve credentials for the provided username')
	arguments.add_argument('--host',action='store',help='Hostname')
	arguments.add_argument('-u','--user',action='store',help='Username')
	arguments.add_argument('-p','--passwd',action='store',help='Password')
	arguments.add_argument('--path',action='store',help='Path for saving the file')
	return arguments.parse_args()
	
def main():
	accept_args = argument_parse()
	if accept_args.save:
		input_to_config(accept_args.host, accept_args.user, accept_args.passwd, accept_args.path)
	elif accept_args.retrieve:
		read_from_config(accept_args.host,accept_args.path)	
	
if __name__ == '__main__':
	main()