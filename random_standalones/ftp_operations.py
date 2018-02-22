from ftplib import FTP
import argparse
import os

'''credentials = {  # 'rebex':{'url':'test.rebex.net','user':'demo','passwd':'password'},
    'dlptest': {'url': 'ftp.dlptest.com', 'user': 'dlpuser@dlptest.com', 'passwd': 'eiTqR7EMZD5zy7M'}
}'''


class FTPOperations:
    def __init__(self, host, port, user, passwd, localpath, remotepath):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.localpath = localpath # '/home/ankur/Documents/dwnl_data/'
        self.remotepath = remotepath
        self.session = None

    #def testing(self,user,password):
    #    pass

    def ftp_connect(self):
        self.session =  FTP(self.host)
        #ftp.connect(self.host,self.port)
        self.session.login(self.user, self.passwd)

    def file_list(self):
        self.ftp_connect()
        file_names=list()
        try:
            self.session.cwd(self.remotepath)
            file_names = self.session.nlst()
        except Exception as e:
            print(e)
        finally:
            self.session.quit()
            return file_names

    def file_download(self):
        self.ftp_connect()
        try:
            self.session.cwd(self.remotepath)
            ftp_files = self.session.nlst()
            for filename in ftp_files:
                if not filename.startswith('.'):
                    with open(self.localpath + filename, 'wb') as file:
                        self.session.retrbinary('RETR ' + filename, file.write)
                        print(filename + ' downloaded to ' + self.localpath)
        except Exception as e:
            print(e)
        finally:
            self.session.quit()

    def file_upload(self):
        self.ftp_connect()
        dir_files=list()
        try:
            self.session.cwd(self.remotepath)
            dir_files =os.listdir(self.localpath)
            for filename in dir_files:
                with open(self.localpath + filename, 'rb') as file:
                    self.session.storbinary('STOR ' + filename, file)
                    print(filename + ' uploaded.')
        except Exception as e:
            print(e)
        finally:
            self.session.quit()
            return dir_files

    def file_list_2(self):
        file_names = FTP.nlst()
        return file_names

    @staticmethod
    def file_upload_2():
        dir_files=os.listdir()
        return dir_files


def argument_parse():
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--host', action='store', dest='host', help='Hostname')
    arguments.add_argument('--port', action='store', dest='port',  type=int, help='Port number')
    arguments.add_argument('-u', action='store', dest='user', help='Username')
    arguments.add_argument('-p', action='store', dest='passwd', help='Password')
    arguments.add_argument('-lp', action='store', dest='localpath', help='Absolute Path for the local directory')
    arguments.add_argument('-rp', action='store', dest='remotepath', help='Absolute Path for the remote directory')
    arguments.add_argument('--list', action='store_true', dest='list', default=False, help='List Files on Server')
    arguments.add_argument('--up', action='store_true', dest='up', default=False, help='Download files')
    arguments.add_argument('--down', action='store_true', dest='down', default=False, help='Upload Files')
    return arguments.parse_args()


def main():
    accept_args = argument_parse()
    if accept_args.list:
        print('Extracting list from server...')
        list = FTPOperations(accept_args.host,accept_args.port,accept_args.user,accept_args.passwd,accept_args.localpath,accept_args.remotepath)
        for filename in list.file_list():
            print (filename)

    elif accept_args.up:
        print('Uploading files to server...')

    elif accept_args.down:
        print('Downloading files from server...')
        download = FTPOperations(accept_args.host,accept_args.port,accept_args.user,accept_args.passwd,accept_args.localpath,accept_args.remotepath)
        download.file_download()

    else:
        print('No option provided for either listing, uploading or downloading files.')

def file_list():
        file_names = FTP.nlst()
        return file_names

if __name__ == '__main__':
    main()