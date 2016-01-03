from ftplib import FTP


class FtpAccess:
    __ftp_server = ''
    __user_name = ''
    __user_password = ''
    __port = ''
    ftp = FTP()

    def __init__(self, ftp_server, user_name='', password='', port=21):
        self.__ftp_server = ftp_server
        self.__user_name = user_name
        self.__user_password = password
        self.__port = port
        self.__connect()
        self.__login()

    def __login(self):
        self.ftp.login(self.__user_name, self.__user_password)

    def __connect(self):
        self.ftp.connect(self.__ftp_server, self.__port)

    def download_file(self, local_file, remote_file):
        file_handle = open(local_file, 'wb')
        self.ftp.retrbinary('RETR %s' % remote_file, file_handle.write)
        file_handle.close()
        return True

    def quit(self):
        self.ftp.quit()
