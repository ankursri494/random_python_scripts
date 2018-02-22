import pytest
import unittest
from mock import patch
from ftp_operations import FTPOperations
import ftp_operations


CREDENTIALS = ['dlp.test.com',21,'demo','password','some/arbitrary/localpath/','some/arbitrary/remotepath/']

REMOTE_FILES = ['dwnl1.txt','dwn.jpeg','index.csv']
LOCAL_FILES = ['img.jpg','dbcentre.db','values.dat']

UPLOADED_FILES = ['img.jpg','dbcentre.db','values.dat']
DOWNLOADED_FILES = ['dwnl1.txt','dwn.jpeg','index.csv']
FILE_LIST = ['dwnl1.txt','dwn.jpeg','index.csv']



@pytest.fixture()
def x_ftp():
    with patch("ftp_operations.FTP") as ftp:
        yield ftp

@pytest.fixture()
def x_os():
    with patch("ftp_operations.os") as xos:
        yield xos


class TestFTPOperations():
    def test_ftp_connect_given_credentials(self,x_ftp):
        FTPOperations(*CREDENTIALS).ftp_connect()
        x_ftp.return_value.FTP.called

    def test_ftp_login_given_credentials(self,x_ftp):
        FTPOperations(*CREDENTIALS).ftp_connect()
        x_ftp.return_value.login.assert_called_with(CREDENTIALS[2],CREDENTIALS[3])

    def test_ftp_current_dir_given_remotepath(self, x_ftp):
        FTPOperations(*CREDENTIALS).file_list()
        x_ftp.return_value.cwd.assert_called_with(CREDENTIALS[5])

    def test_ftp_remotepath_given_credentials(self, x_ftp):
        FTPOperations(*CREDENTIALS).file_list()
        assert isinstance(FTPOperations(*CREDENTIALS).remotepath,str)

    # random test
    def test_random_function(self, x_ftp):
        x_ftp.nlst.return_value = REMOTE_FILES
        files_on_server = ftp_operations.file_list()
        assert files_on_server == FILE_LIST

    # random test 2
    def test_random_function_2(self, x_ftp):
        x_ftp.nlst.return_value = REMOTE_FILES
        files_on_server = FTPOperations(*CREDENTIALS).file_list_2()
        assert files_on_server == FILE_LIST

    def test_ftp_files_list_given_remotepath(self, x_ftp):
        x_ftp.return_value.nlst.return_value = REMOTE_FILES
        files_on_server=FTPOperations(*CREDENTIALS).file_list()
        assert files_on_server == FILE_LIST

    def test_ftp_download_given_localpath(self, x_ftp):
        FTPOperations(*CREDENTIALS).file_download()
        x_ftp.return_value.retrbinary.called

    def test_ftp_upload_given_remotepath(self, x_ftp):
        FTPOperations(*CREDENTIALS).file_upload()
        x_ftp.return_value.storbinary.called

    #doubt_case
    def test_ftp_upload_given_localpath(self, x_ftp, x_os):
        x_os.listdir.side_effect = [LOCAL_FILES,None]
        files_on_local=FTPOperations(*CREDENTIALS).file_upload()
        assert files_on_local==LOCAL_FILES

    def test_ftp_upload_error_given_localpath(self, x_ftp, x_os):
        with pytest.raises(TypeError):
            x_os.return_value.listdir.return_value = None
            FTPOperations(*CREDENTIALS).file_upload()

    #doubt_case_2
    def test_random_function_3(self, x_ftp, x_os):
        x_os.listdir.return_value = LOCAL_FILES
        files_on_local=FTPOperations.file_upload_2()
        assert files_on_local==LOCAL_FILES



    def ftp_list_handle_exception_given_wrong_path(self,x_ftp,x_os):
        x_os.listdir.side_effect=[[LOCAL_FILES],None]
        files_on_local =FTPOperations(*CREDENTIALS).file_upload()
        assert files_on_local==LOCAL_FILES

    def test_ftp_list_handle_exception_given_wrong_path(self):
        self.ftp_list_handle_exception_given_wrong_path(x_ftp,x_os)



