#!/usr/bin/env python

"""
The script is used to generate password hashes suitable for both
OSDF and Aspera servers.
"""

import getpass
import hashlib
import sys
import getopt
from werkzeug.security import generate_password_hash

def get_sha1_hash(password):
    """For a given password string, utf-8 encode it and hash it with SHA1."""
    encoded = password.encode('utf8')
    hashed = hashlib.sha1(encoded).hexdigest()

    return hashed

def how_to():
    """Generates the usage information to STDOUT."""

    print("generate_password.py")
    print("options - ")
    print(" -u, --username - username for the account (required)")
    print(" -p, --password - prompts for password(masked) (optional)")
    print(" -h, --help - usage")

def main(argv):
    """The main body of execution."""

    username = None
    password = None

    try:
        opts, args = getopt.gnu_getopt(argv, "u:ph",
                                       ["username=", "password", "help"])
        if not opts:
            how_to()
            sys.exit(2)
    except getopt.GetoptError as err:
        print err
        how_to()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = getpass.getpass("Enter your password:")
        elif opt in ("-h", "--help"):
            how_to()
            sys.exit(2)

    if password is None:
        password = getpass.getpass(
            "Enter your password (Don't worry, it's not shown): "
        )
        password_confirm = getpass.getpass(
            "Enter your password AGAIN to confirm: "
        )

    if password != password_confirm:
        print("Passwords entered do not match.")
        sys.exit(1)

    sha1 = get_sha1_hash(password)

    salted_hash = generate_password_hash(password, method='sha1')

    print("="*80)
    print("SHA1:        %s" % sha1)
    print("Salted SHA1: %s:%s" % (username, salted_hash))

main(sys.argv[1:])
