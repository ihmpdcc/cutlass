#!/usr/bin/python
import argparse
import os
import random
import re
import subprocess
import sys

from . import aspera

## input
parser = argparse.ArgumentParser(description='Perform round-trip Aspera upload/download test with ascp.')

parser.add_argument('--server', metavar='s', type=str, help='Aspera host/server address.')
parser.add_argument('--username', metavar='u', type=str, help='Aspera username.')
parser.add_argument('--remote_path', metavar='r', type=str, help='Path on Aspera server to use for testing.')
parser.add_argument('--local_file', metavar='l', type=str, help='Path to local file to upload.')
parser.add_argument('--tmp_dir', metavar='t', type=str, default='/tmp', help='Path in which to write temporary files.')
args = parser.parse_args();

## functions
def get_md5(f):
    cmd_out = subprocess.check_output(["md5sum", f], universal_newlines=True)
    m = re.match(r"^([0-9a-f]+)", cmd_out)
    if m:
        return m.group(1)
    else:
        return None        

## main program

# use a remote path that's likely to be unique
r_id = random.randint(1, 100000)
pid = os.getpid()
r_str = "test_%06d_%06d" % (pid, r_id)

remote_path = os.path.join(args.remote_path, r_str)
print(("uploading to remote path %s" % remote_path))

# upload file
if not aspera.upload_file(args.server, args.username, None, args.local_file, remote_path):
    print(("FAIL - file upload failed"))
    sys.exit(1)

# likewise with the local path
new_local_path = os.path.join(args.tmp_dir, r_str)

# check that the file doesn't already exist
if (os.path.isfile(new_local_path)):
    print(("FAIL - local file " + new_local_path + " already exists. Please remove it and re-run."))
    sys.exit(1)

print(("downloading to local file", new_local_path))

# download file
if not aspera.download_file(args.server, args.username, None, remote_path, new_local_path):
    print(("FAIL - file download failed"))
    sys.exit(1)

# run md5sum to check that they're the same
original_md5 = get_md5(args.local_file)
new_md5 = get_md5(new_local_path)

if new_md5 == original_md5:
    print(("SUCCESS - md5sums match, removing local temporary file"))
    # remove local/temporary file
    os.remove(new_local_path)
else:
    print(("FAIL - md5sums do not match (original=" + original_md5 + " new=" + new_md5 + ")"))
    print(("WARN - temporary downloaded file " + new_local_path + " not removed"))

