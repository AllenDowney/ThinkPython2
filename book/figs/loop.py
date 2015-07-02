import sys, os
from glob import glob

def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    return res, stat
 
def main(script, files='*.eps'):
    for filename in sorted(glob(files)):
        destination = '.'.join(filename.split('.')[:-1]) + '.pdf'
        cmd = 'convert %s %s' % (filename, destination) 
        print cmd

        res, stat = pipe(cmd)
        print res, stat
  
if __name__ == '__main__':
    main(*sys.argv)
