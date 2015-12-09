#!/bin/tcsh

# path to ascp Aspera command-line client (Linux)
#setenv PATH /home/jcrabtree/.aspera/connect/bin:$PATH

# path to ascp Aspera command-line client (Mac OS X)
setenv PATH ~/Applications/Aspera\ Connect.app/Contents/Resources:$PATH

setenv PYTHONPATH cutlass:osdf-python

# iHMPDCC production server
setenv SERVER osdf.ihmpdcc.org

# upload new nodes
./test-upload.py --username=$USER --password=$PASS --server=$SERVER --tag=jctest

