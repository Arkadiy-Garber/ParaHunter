#!/bin/bash

# setting colors to use
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'


usage="$(basename "$0") [-h] [-a s] [-n s] [-m n] [-c n] [-l s] -- program to cluster protein sequences based on amino acid identity

options:
    -h     show this help text
    -a     input FASTA file containing ORFs in amino acid format
    -n     input FASTA file containing ORFs in nucleic acid format
    -c     fraction of query sequence that must align to cluster (default 0.7)
    -m     cluster sequences above this identity threshold (default: 0.7)\
    -l     codeml-2.ctl file"

if [ "$#" == 0 ] || [ $1 == "-h" ] || [ $1 == "help" ]; then
echo "$usage"
       exit
       fi

COV=0.7
ID=0.7
while getopts ':a:n:m:c:l:' args; do
  case "$args" in

    a) AA=${OPTARG}
       ;;

    n) NUC=${OPTARG}
       ;;

    c) COV=${OPTARG}
       ;;

    m) ID=${OPTARG}
       ;;

    l) CTL=${OPTARG}
       ;;

    :) printf "missing argument for -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
   \?) printf "\n  ${RED}Invalid argument: -${OPTARG}${NC}\n\n    Run 'ParaHunter' with no arguments or '-h' only to see help menu.\n\n" >&2 && exit
       exit 1
       ;;
  esac
done

#shift $((OPTIND - 1))

echo ${AA}
echo ${NUC}
echo ${COV}
echo ${ID}
echo ${ctl}

fixfastas.py -aa ${AA} -nuc ${NUC}
sleep 5

echo "Clustering ORFs"
mmseqs createdb ${AA}.ph ${AA}.db &> mmseqs.log1
mmseqs cluster ${AA}.db clu tmp --min-seq-id ${ID} -c ${COV} &> mmseqs.log2
mmseqs createseqfiledb ${AA}.db clu clu_seq &> mmseqs.log3
mmseqs result2flat ${AA}.db ${AA}.db clu_seq clu_seq.fasta &> mmseqs.log4
mmseqs createtsv ${AA}.db ${AA}.db clu clu.tsv &> mmseqs.log5

cat mmseqs.log* > mmseqs.log
rm mmseqs.log1
rm mmseqs.log2
rm mmseqs.log3
rm mmseqs.log4
rm mmseqs.log5
rm -r tmp/
rm clu
rm *.index
rm ${AA}.db
rm ${AA}.db_h
rm ${AA}.db.lookup
rm clu_seq.*
#rm clu.*
rm ${AA}.db_h.dbtype
rm ${AA}.db.source
mv clu.tsv ${AA}-clu.tsv

mkdir ${AA}-clusters
echo "${GREEN}Splitting ORFs into separate files"cd g
clu2fasta.py -clu ${AA}-clu.tsv -outdir ${AA}-clusters -prots ${AA}.ph
echo "${GREEN}Performing dN/dS analysis with Codeml"
echo "This file is automatically generated during the ParaHunter run to fool codeml. Please feel free to delete" > tmp.trees
parahunter-dnds.py -clu ${AA}-clu.tsv -aa ${AA}.ph -nuc ${NUC}.ph -ctl ${ctl}




