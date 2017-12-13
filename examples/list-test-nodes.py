#!/usr/bin/python

# pylint: disable=C0111, C0325

import argparse
import logging
from cutlass import iHMPSession

# globals
NAMESPACE = 'ihmp'

## input
parser = argparse.ArgumentParser()
parser.add_argument('--username', help='OSDF username')
parser.add_argument('--password', help='OSDF password')
parser.add_argument('--server', help='OSDF server address')
parser.add_argument('--tag', help='Unique tag for uploaded test nodes.')
args = parser.parse_args()

# main program
logging.basicConfig(level=logging.INFO)
s = iHMPSession(args.username, args.password, args.server)
o = s.get_osdf()

# query for all nodes with tag args.tag
qstring = "\"" + args.tag + "\"[tags]"
res = o.oql_query_all_pages(NAMESPACE, qstring)
print("OQL query=" + qstring + " result_count=" + str(res['result_count']))
results = res['results']

n_listed = 0
for result in results:
    ident = result['id']
    print("id=" + ident + " node type=" + result["node_type"])
    tags = result['meta']['tags']
    for tag in tags:
        # double-check that args.tag is present - should be superfluous
        if (tag == args.tag):
            n_listed = n_listed + 1

print("num_listed= " + str(n_listed))
