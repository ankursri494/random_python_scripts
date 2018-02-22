# Code Snippet 1:

def add_numbers2(a, b):
    r = a + b
    return r


# Refactored Code
def add_numbers(a, b):
    return (a + b)


# Code Snippet 2:

import fnmatch


def filter_list_by_pattern2(list_object, pattern):
    filtered_list = list()
    for i in list_object:
        if fnmatch.fnmatch(i, pattern):
            filtered_list.append(i)

    return filtered_list

# Refactored Code : using List comprehensions

def filter_list_by_pattern(list_object, pattern):
    filtered_list = [i for i in list_object if fnmatch.fnmatch(i,pattern)]
    return filtered_list



#Code Snippet 3:
import os

def list_file_names_by_pattern1(path, pattern):
    file_list = os.listdir(path)
    result_filenames = list()
    for filename in file_list:
        if fnmatch.fnmatch(filename, pattern):
            result_filenames.append(filename)
    return result_filenames


#Refactored Code
def list_file_names_by_pattern(path, pattern):
    file_list = os.listdir(path)
    result_filenames = filter_list_by_pattern(file_list, pattern)
    return result_filenames




# Code Snippet 4
from ftplib import FTP
def connect_to_ftp(username, password, host, port):
    session = FTP()
    session.connect(host,port)
    session.login(username, password)





# code snippet 5
import logging

class SftpOperations:
    pass

class FtpOperations:
    pass


def create_protocol_object(protocol):
    if protocol == 'sftp':
        protocol_obj = SftpOperations()
        return protocol_obj
    else:
        logging.error("Unknown Protocol Name")
