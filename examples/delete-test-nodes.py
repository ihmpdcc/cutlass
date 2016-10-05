#!/usr/bin/python

import argparse
import logging
import pprint
from cutlass import iHMPSession

## globals
NAMESPACE = 'ihmp'
NODE_TYPE_ORDER = [
    'annotation', 'abundance_matrix',
    'wgs_assembled_seq_set', '16s_trimmed_seq_set',
    'wgs_raw_seq_set', '16s_raw_seq_set', 'wgs_dna_prep', '16s_dna_prep',
    'sample', 'visit', 'subject', 'study', 'project'
    ]

## input
parser = argparse.ArgumentParser()
parser.add_argument('--username', help='OSDF username')
parser.add_argument('--password', help='OSDF password')
parser.add_argument('--server', help='OSDF server address')
parser.add_argument('--tag', help='Unique tag for uploaded test nodes.')
args = parser.parse_args()

## main program
logging.basicConfig(level=logging.INFO)
s = iHMPSession(args.username, args.password, args.server)
osdf = s.get_osdf()

# query for all nodes with tag args.tag
qstring = "\"" + args.tag + "\"[tags]"
res = osdf.oql_query_all_pages(NAMESPACE, qstring)
print("OQL query=" + qstring + " result_count=" + str(res['result_count']))
results = res['results']

# sort nodes to satisfy dependency order when deleting - delete will fail otherwise
node_type_order = {}
nto = 1
for nt in NODE_TYPE_ORDER:
    node_type_order[nt] = nto
    nto = nto + 1
sorted_res = sorted(results, key=lambda k: node_type_order[k["node_type"]])


n_deleted = 0
for r in sorted_res:
    id = r['id']
    print("id=" + id + " node type=" + r["node_type"])
    tags = r['meta']['tags']
    for t in tags:
        # double-check that args.tag is present - should be superfluous
        if (t == args.tag):
            print("deleting " + id)
            osdf.delete_node(id)
            n_deleted = n_deleted + 1

print("Deleted count: " + str(n_deleted))
