# eviltar
Modded version of tarfile.py for testing arbitrary file (over)write via path traversal in Tar archives.

This script is useful for quickly craft a tar archive with a file with dot-dot pattern as a filename and verify if the target library is vulnerable to arbitrary file overwrite via path traversal filenames.

This tool can be considered the counterpart of https://github.com/ptoomey3/evilarc.

Example:

<code>$python2 eviltar.py -f fakefile -n ../../../../../../../../../tmp/test</code>
