import sandbox

MODULE_UNDER_TEST = 'sandbox'

def test_add_given_2_numbers():
    r = sandbox.add_numbers(4, 5)
    assert r == 9


# Requirement filter values from a list by UNIX like pattern

X_LIST = ['RAEabc.csv', 'RAEdef.xls', 'RAEghi.csv', 'RAEced.txt']
X_PATTERN = 'RAE*csv'
X_EXPECTED = ['RAEabc.csv', 'RAEghi.csv']


def test_filter_given_list_by_pattern():
    result = sandbox.filter_list_by_pattern(X_LIST, X_PATTERN)
    assert result == X_EXPECTED


# MOCKING
# Requirement change to List above is list of files in a directory
X_PATH = '/path/to/test/dir'

from mock import patch

# Context manager form for mocking
def test_retrieve_file_names_from_path_match_by_pattern():
    with patch(MODULE_UNDER_TEST + '.os') as x_os:
        x_os.listdir.return_value = X_LIST
        result = sandbox.list_file_names_by_pattern(X_PATH, X_PATTERN)
    assert result == X_EXPECTED


# Refactored test cases# Decorated mock

@patch(MODULE_UNDER_TEST+'.os')
def test_using_deco_retrieve_file_names_from_path_match_by_pattern(x_os):
    x_os.listdir.return_value = X_LIST
    result = sandbox.list_file_names_by_pattern(X_PATH, X_PATTERN)
    assert result == X_EXPECTED

#Refactored test case using pytest fixture

import pytest

@pytest.fixture
def x_os():
    with patch(MODULE_UNDER_TEST + '.os') as x:
        yield x


def test_using_fixture_retrieve_file_names_from_path_match_by_pattern(x_os):
    x_os.listdir.return_value = X_LIST
    result = sandbox.list_file_names_by_pattern(X_PATH, X_PATTERN)
    assert result == X_EXPECTED




# Connection to FTP
X_USER = 'test_user'
X_PASS = 'test_pass'
X_HOST = 'test_host'
X_PORT = 'test_port'

def test_connect_to_ftp(x_FTP):
    sandbox.connect_to_ftp(X_USER, X_PASS, X_HOST, X_PORT)
    x_FTP.return_value.connect.assert_called_with(X_HOST, X_PORT)

def test_login_to_ftp_given_user_and_passwd(x_FTP):
    sandbox.connect_to_ftp(X_USER, X_PASS, X_HOST, X_PORT)
    x_FTP.return_value.login.assert_called_with(X_USER, X_PASS)


@pytest.fixture
def x_FTP():
    with patch(MODULE_UNDER_TEST+'.FTP') as x:
        yield x



# Test case for code snippet 5
X_PROTOCOL = 'sftp'
def test_sftp_protocol_obj_given_protocol():
    protocol_obj = sandbox.create_protocol_object(X_PROTOCOL)
    assert isinstance(protocol_obj, sandbox.SftpOperations)


def test_raises_exception_given_unknown_protocol(x_logging):
    X_PROTOCOL = 'ftp'
    protocol_obj = sandbox.create_protocol_object(X_PROTOCOL)
    x_logging.error.assert_called_with("Unknown Protocol Name")


@pytest.fixture
def x_logging():
    with patch(MODULE_UNDER_TEST+'.logging') as x:
        yield x