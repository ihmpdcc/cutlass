#!/bin/bash

# path to ascp Aspera command-line client (Linux)
# export PATH=$HOME/.aspera/connect/bin:$PATH

# path to ascp Aspera command-line client (Mac OS X)
export PATH=$HOME/Applications/Aspera\ Connect.app/Contents/Resources:$PATH

export PYTHONPATH=cutlass:osdf-python

# iHMPDCC production server
export SERVER=osdf.ihmpdcc.org

# upload new nodes
./test-upload.py --username=$USER --password=$PASS --server=$SERVER --tag=jctest
