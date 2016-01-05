import ftplib
import os
import socket
import sys

import datetime

HOST = '127.0.0.1'
DIR = 'd:\\G'
FILE = 'xue.jpg'
USER_NAME = 'tao.pei'
PWD = '123456'


def download_file(file_name):
    try:
        ftp = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror):
        host_ = ('ERROR:cannot reach %s' % HOST)
        print host_
        return
    print('*** Connected to host %s' % HOST)

    try:
        ftp.login(USER_NAME, PWD)
    except ftplib.error_perm:
        print('ERROR:cannot login USER_NAME=%s, PWD=%s' % (USER_NAME, PWD))
        ftp.quit()
        return
    print('*** Login in as %s' % USER_NAME)

    try:
        ftp.cwd(DIR)
    except ftplib.error_perm:
        print('ERROR:cannot CD to %s' % DIR)
        ftp.quit()
        return

    try:
        f = open(file_name, 'wb')
        ftp.retrbinary('R %s' % file_name, f.write)
        f.close()

    except ftplib.error_perm:
        print('ERROR:cannot read f %s' % file_name)
        os.unlink(file_name)
        f.close()
    else:
        print('*** Downloaded %s to %s' % (file_name, os.getcwd()))
    ftp.quit()
    return

# if __name__ == '__main__':
# DownloadFile(sys.argv[1])
print os.getcwd()
print '+++++'
for root, dirs, files in os.walk('/home/peter/ebook', False):
    print root, "consumes"
    print dirs
    for n in files:
        print os.path.join(root, n)
        print datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root, n)))
        print datetime.date.today()
    print sum([os.path.getsize(os.path.join(root, name)) for name in files]),
    print "bytes in", len(files), "non-directory files"
