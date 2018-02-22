from contextlib import contextmanager
from ftplib import FTP
import os


@contextmanager
def listing_files(url):
    try:
        ftp = FTP(url)
        yield ftp
    finally:
        dftp.quit()


credentials = {  # 'rebex':{'url':'test.rebex.net','user':'demo','passwd':'password'},
    'dlptest': {'url': 'ftp.dlptest.com', 'user': 'dlpuser@dlptest.com', 'passwd': 'eiTqR7EMZD5zy7M'}

}


class FileAcquisition:

    def __init__(self, ftp):
        self.ftp = ftp

    def format_list(self, ftp):
        print(ftp.getwelcome() + '\n')
        ftp.retrlines('LIST')

    def name_list(self, ftp):
        file_names = ftp.nlst()
        for name in file_names:
            print(name)

    def set_path(self,path):
        self.path = path #'/home/ankur/Documents/dwnl_data/'
        return self.path

    def file_download(self, ftp):

        ftp_files = ftp.nlst()
        for filename in ftp_files:
            #file_type = mimetypes.guess_type(filename)[0]

           # try:
            if not filename.startswith('.'):
                with open(self.path + filename, 'wb') as file:
                    ftp.retrbinary('RETR ' + filename, file.write)
                    print(filename + ' downloaded to ' + self.path)

                '''except:
                with open(self.path + filename, 'wb') as file:
                    ftp.retrbinary('RETR ' + filename, file.write)
                    print(filename + ' downloaded to ' + self.path)

            except:'''

    def file_upload(self, ftp):

        dir_files = os.listdir(self.path)
            #file_type = mimetypes.guess_type(filename)[0]


            try:

                with open(self.path + filename, 'rb') as file:
                    ftp.storlines('STOR ' + filename, file)
                    print(filename + ' uploaded.')

            except:

                print('File type not recognised.')


#file_extensions = ['txt','doc','docx','log','msg','odt','rtf','wps','dat','csv','ppx','pptx','xml','tar','vcf','htm','html']

'''file_extensions1 = ["asp",	"aspx",	"bat",	"c",	"cbl",	"cc",	"cfc",	"cfg",	"cfm",	"cmd",	"cnf", "conf",	"cpp",	"cson",	"css",	"csv",	"cxx",	"dat",	"eco",	"emacs",	"eml",	"erb",	"erl",	"gitconfig",	"gitignore",	"go", "h",	"htm",	"html",	"ini",	"ino",	"js",	"json",	"jsonld",	"jsx",	"less",	"log",	"ls",	"m",	"md",	"mht",	"mhtml",	"mjs",	"mkd",	"mkdn",	"mkdown",	"patch",	"pch",	"php",	"phtml",	"pl",	"py",	"rb",	"rdoc",	"rss", "rtf",	"sass",	"scala",	"sh",	"sql",	"sss",	"sub", "svg", "tex",	"text", "ts",	"tsv",	"txt",	"vbs",	"vim",  "xht",	"xhtml",	"xml",	"xsl",	"yaml",	"yml",	"zsh"]'''


for ftp_name in credentials.keys():
    with listing_files(credentials[ftp_name]['url']) as ftp:
        ftp.login(user=credentials[ftp_name]['user'], passwd=credentials[ftp_name]['passwd'])

        print('Select operation to perform:')
        print('l for Listing files')
        print('u for Uploading files')
        print('d for Downloading files')

        choice = input()

        if choice == 'l':

            list = FileAcquisition(ftp)
            list.name_list(ftp)
            list.format_list(ftp)


        elif choice == 'u':

            upload = FileAcquisition(ftp)

            path = input('From where is data uploaded (absolute path):')
            upload.set_path(path)
            upload.file_upload(ftp)



        elif choice == 'd':

            download = FileAcquisition(ftp)

            path = input('Where to download (absolute path):')
            download.set_path(path)
            download.file_download(ftp)
