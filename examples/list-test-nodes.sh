#!/bin/tcsh

setenv PYTHONPATH cutlass:osdf-python

# iHMPDCC production server
setenv SERVER osdf.ihmpdcc.org

# delete test nodes
./list-test-nodes.py --username=$USER --password=$PASS --server=$SERVER --tag=jctest
