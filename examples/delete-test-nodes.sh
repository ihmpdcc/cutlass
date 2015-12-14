#!/bin/bash

export PYTHONPATH=cutlass:osdf-python

# iHMPDCC production server
export SERVER=osdf.ihmpdcc.org

# delete test nodes
./delete-test-nodes.py --username=$USER --password=$PASS --server=$SERVER --tag=${USER}test
