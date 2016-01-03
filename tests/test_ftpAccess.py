# -*- coding: gbk -*-
from unittest import TestCase
from src import FtpAceess


class TestFtpAccess(TestCase):
    ftp = FtpAceess.FtpAccess('ftp1.linuxidc.com', 'ftp1.linuxidc.com', 'www.linuxidc.com')

    def test_pwd(self):
        self.ftp.ftp.cwd('2015��LinuxIDC.com')
        pwd = self.ftp.ftp.pwd()
        self.assertSequenceEqual('/2015��LinuxIDC.com', pwd, 'expected: /2015��LinuxIDC.com but: ' + pwd)
        self.ftp.quit()
