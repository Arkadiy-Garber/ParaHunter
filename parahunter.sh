#!/bin/bash

# setting colors to use
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'


usage="$(basename "$0") [-h] [-a s] [-n s] [-min-seq-id n] [-c n] -- program to cluster protein sequences based on amino acid identity

where:
    -h              show this help text
    -a              input FASTA file containing ORFs in amino acid format
    -n              input FASTA file containing ORFs in nucleic acid format
    -c              fraction of query sequence that must align to cluster (default 0.7)
    -min-seq-id     cluster sequences above this identity threshold (default: 0.7)"


COV=0.7
ID=0.7
while getopts ':han:' option; do
  case "$option" in
    h) echo "$usage"
       exit
       ;;
    min-seq-id) ID=$OPTARG
       ;;

    c) COV=$OPTARG
       ;;

    n) NUC=$OPTARG
       ;;

    a) AA=$OPTARG
       ;;


    :) printf "missing argument for -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
   \?) printf "illegal option: -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
shift $((OPTIND - 1))


if [ "$#" == 0 ]; then
echo "$usage"
       exit
       fi

mmseqs createdb $1 $1.db
mmseqs cluster $1.db clu tmp --min-seq-id $ID -c $COV
mmseqs createseqfiledb $1.db clu clu_seq
mmseqs result2flat $1.db 1.db clu_seq clu_seq.fasta
mmseqs createtsv $1.db $1.db clu clu.tsv

rm -r tmp/
rm clu
rm *.index
rm $1.db
rm $1.db_h
rm $1.db.lookup
rm clu_seq
mv clu.tsv $1-clu.tsv

mkdir $1-clusters
clu2fasta.py -clu $1-clu.tsv -outdir $1-clusters -prots $1
echo $1
echo -n
parahunter-dnds.py -clu $1-clu.tsv -aa $1 -nuc $2 -ctl ${CTL}




