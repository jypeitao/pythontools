import os
import re
import tarfile

print os.getcwd()


def tar(name):
    t = tarfile.open(name + ".tar.gz", "w:gz")
    for root, dr, files in os.walk(name):
        print(root, dr, files)
        for f in files:
            fp = os.path.join(root, f)
            t.add(fp)
    t.close()


def untar(name, dirs):
    t = tarfile.open(name)
    ns = t.getnames()
    for n in ns:
        sn = str(n)
        if sn.find('Ac') > -1:
            print 'got'
        print n
    t.extractall(dirs)


print __name__

if __name__ == '__main__':
    print 'test'
    if os.path.exists('haha'):
        print 'haha exist'
        pass
    else:
        print 'haha not exist'
        os.mkdir('haha')
    #untar("tests.tar.gz", './haha')
    # tar('tests')
   # with re.match('ac', 'abc ac ac') as ma:
    ma = re.match(r'ac', 'acd b ac ac')
    print 'xxx'
    print ma.group(0)
    mm = re.search('cc', 'abc cc cbc bcc')
    print mm.group(0)


