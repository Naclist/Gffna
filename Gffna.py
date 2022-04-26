#! /usr/bin/env python

import gffutils
from Bio.Seq import Seq
import pyfaidx
import argparse
import Bio.Seq

parser = argparse.ArgumentParser(
    description='Generate partial CDS or other required sequences from a nucleotide sequence file according to a GFF file.',
    add_help=False,
    usage='\nGffna --gff [input .gff file] --fna [input .fna file] --type [type: CDS, tRNA, exon... default: CDS] --protein [optional, generate sequence of amino acids]')

parser.add_argument(
    '--gff',
    metavar='[input.gff]',
    required=True,
    type=str)
parser.add_argument(
    '--fna',
    metavar='[input.fna]',
    required=True,
    type=str)
parser.add_argument(
    '--type',
    metavar='[Requested type of sequence]',
    help='Options of requested type of sequence.',
    required=False)
parser.add_argument(
    '--protein',
    action = 'store_true',
    help='generate sequence of amino acids.',
    required=False)

args = parser.parse_args()

gff = args.gff
fna = pyfaidx.Fasta(args.fna)

gffdb = gffutils.create_db(
    gff,dbfn='gff.db',
    force=True,
    keep_order=True,
    merge_strategy="merge",
    sort_attribute_values=True) #以后有时间应该这里得要改名字

if not args.type:
    reqType = 'CDS'
else:
    reqType = args.type

for i in gffdb.features_of_type(reqType, order_by='seqid'):
    print('>'+i.seqid+"_"+i.id.replace('cds-',''))
    g_seq = (i.sequence(fna))
    g_seq = Seq(g_seq)
    if i.strand == '-':
        g_seq = g_seq.reverse_complement() #转义
    if not args.protein:
        g_seq = g_seq
    else:
        g_seq = Bio.Seq.translate(g_seq,table=11)
    for b in range(0, len(g_seq), 60):  #好看一些的输出
        print(g_seq[b:b + 60])
