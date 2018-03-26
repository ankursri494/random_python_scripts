import base64
import argparse

def write_config_file(user, passwd, cloud_name, config_file_path):
	try:
		with open(config_file_path + '/config.ini','a') as write_config:
			write_config.write('[' + cloud_name + ']' + '\n')
			write_config.write('Username = ' + user + '\n')
			encoded_passwd = base64.encodestring(passwd)
			write_config.write('Password = ' + encoded_passwd + '\n')
	except Exception as e:
		print (e)

def parse_config_file(cloud_name, config_file_path):
	try:
		flag = False
		set_values = dict()
		for line in open(config_file_path + '/config.ini','r'):
			if flag == True:
				if line != '\n':
					values = line.split('=')
					set_values.update({values[0].strip() : values[1].strip()})
				else:
					return set_values
			elif cloud_name in line:
				flag = True
		if flag == False: print('No such hostname found.')
	except Exception as e:
		print (e)
			
def argument_parse():
	arguments = argparse.ArgumentParser()
	group = arguments.add_mutually_exclusive_group()
	group.add_argument('--save',action='store_true',help='Save credentials to config file')
	group.add_argument('--retrieve',action='store_true',help='Retrieve credentials from config file')
	arguments.add_argument('--user',action='store',help='Username')
	arguments.add_argument('--password',action='store',help='Password')
	arguments.add_argument('--cloud_name',action='store',help='Cloud Name')
	arguments.add_argument('--path',action='store',help='Path to config file')
	return arguments.parse_args()
	
def main():
	args = argument_parse()
	if args.save:
		write_config_file(args.user,args.password,args.cloud_name,args.path)
	elif args.retrieve:
		retrieved_values = parse_config_file(args.cloud_name,args.path)	
		print (retrieved_values)
	
if __name__ == '__main__':
	main()
