#!/usr/bin/env python3
from collections import defaultdict
import re
import os
import textwrap
import argparse
import numpy as np
import sys


def firstNonspace(ls):
    for i in ls:
        if i != "":
            break
    return i


def gc(seq):
    gc = 0
    for bp in seq:
        if bp == "C" or bp == "G":
            gc += 1
    return gc/len(seq)


def Dictparser(Dictionary):
    lowest = float(1000)
    for i in Dictionary:
        if float(Dictionary[i]) < float(lowest):
            lowest = Dictionary[i]
            key = i
    return [key, lowest]


def reverseComplement(seq):
    out = []
    for i in range(len(seq)-1, -1, -1):
        nucleotide = seq[i]
        if nucleotide == "C":
            nucleotide = "G"
        elif nucleotide == "G":
            nucleotide = "C"
        elif nucleotide == "T":
            nucleotide = "A"
        elif nucleotide == "A":
            nucleotide = "T"
        out.append(nucleotide)
    outString = "".join(out)
    return outString


def Complement(seq):
    out = []
    for i in range(0, len(seq)):
        nucleotide = seq[i]
        if nucleotide == "C":
            nucleotide = "G"
        elif nucleotide == "G":
            nucleotide = "C"
        elif nucleotide == "T":
            nucleotide = "A"
        elif nucleotide == "A":
            nucleotide = "T"
        out.append(nucleotide)
    outString = "".join(out)
    return outString


def ribosome(seq):
    NTs = ['T', 'C', 'A', 'G']
    stopCodons = ['TAA', 'TAG', 'TGA']
    Codons = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                codon = NTs[i] + NTs[j] + NTs[k]
                # if not codon in stopCodons:
                Codons.append(codon)

    CodonTable = {}
    AAz = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    AAs = list(AAz)
    k = 0
    for base1 in NTs:
        for base2 in NTs:
            for base3 in NTs:
                codon = base1 + base2 + base3
                CodonTable[codon] = AAs[k]
                k += 1

    prot = []
    for j in range(0, len(seq), 3):
        codon = seq[j:j + 3]
        try:
            prot.append(CodonTable[codon])
        except KeyError:
            prot.append("X")
    protein = ("".join(prot))
    return protein


def SeqCoord(seq, start, end):
    return seq[start:end]


def howMany(ls, exclude):
    counter = 0
    for i in ls:
        if i != exclude:
            counter += 1
    return counter


def stabilityCounter(int):
    if len(str(int)) == 1:
        string = (str(0) + str(0) + str(0) + str(0) + str(int))
        return (string)
    if len(str(int)) == 2:
        string = (str(0) + str(0) + str(0) + str(int))
        return (string)
    if len(str(int)) == 3:
        string = (str(0) + str(0) + str(int))
        return (string)
    if len(str(int)) == 4:
        string = (str(0) + str(int))
        return (string)
    if len(str(int)) > 4:
        string = str(int)
        return (string)


def sum(ls):
    count = 0
    for i in ls:
        count += float(i)
    return count


def ave(ls):
    count = 0
    for i in ls:
        count += float(i)
    return count/len(ls)


def derep(ls):
    outLS = []
    for i in ls:
        if i not in outLS:
            outLS.append(i)
    return outLS


def cluster(data, maxgap):
    '''Arrange data into groups where successive elements
       differ by no more than *maxgap*

        #->>> cluster([1, 6, 9, 100, 102, 105, 109, 134, 139], maxgap=10)
        [[1, 6, 9], [100, 102, 105, 109], [134, 139]]

        #->>> cluster([1, 6, 9, 99, 100, 102, 105, 134, 139, 141], maxgap=10)
        [[1, 6, 9], [99, 100, 102, 105], [134, 139, 141]]

    '''
    # data = sorted(data)
    data.sort(key=int)
    groups = [[data[0]]]
    for x in data[1:]:
        if abs(x - groups[-1][-1]) <= maxgap:
            groups[-1].append(x)
        else:
            groups.append([x])
    return groups


def GCcalc(seq):
    count = 0
    for i in seq:
        if i == "G" or i == "C":
            count += 1
    return count/len(seq)


def reject_outliers(data):
    m = 2
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered


def lastItem(ls):
    x = ''
    for i in ls:
        if i != "":
            x = i
    return x


def RemoveDuplicates(ls):
    empLS = []
    counter = 0
    for i in ls:
        if i not in empLS:
            empLS.append(i)
        else:
            pass
    return empLS


def allButTheLast(iterable, delim):
    x = ''
    length = len(iterable.split(delim))
    for i in range(0, length-1):
        x += iterable.split(delim)[i]
        x += delim
    return x[0:len(x)-1]


def secondToLastItem(ls):
    x = ''
    for i in ls[0:len(ls)-1]:
        x = i
    return x


def pull(item, one, two):
    ls = []
    counter = 0
    for i in item:
        if counter == 0:
            if i != one:
                pass
            else:
                counter += 1
                ls.append(i)
        else:
            if i != two:
                ls.append(i)
            else:
                ls.append(i)
                counter = 0
    outstr = "".join(ls)
    return outstr


def replace(stringOrlist, list, item):
    emptyList = []
    for i in stringOrlist:
        if i not in list:
            emptyList.append(i)
        else:
            emptyList.append(item)
    outString = "".join(emptyList)
    return outString


def remove(stringOrlist, list):
    emptyList = []
    for i in stringOrlist:
        if i not in list:
            emptyList.append(i)
        else:
            pass
    outString = "".join(emptyList)
    return outString


def removeLS(stringOrlist, list):
    emptyList = []
    for i in stringOrlist:
        if i not in list:
            emptyList.append(i)
        else:
            pass
    return emptyList


def fasta(fasta_file):
    count = 0
    seq = ''
    header = ''
    Dict = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
    for i in fasta_file:
        i = i.rstrip()
        if re.match(r'^>', i):
            count += 1
            if count % 1000000 == 0:
                print(count)

            if len(seq) > 0:
                Dict[header] = seq
                header = i[1:]
                # header = header.split(" ")[0]
                seq = ''
            else:
                header = i[1:]
                # header = header.split(" ")[0]
                seq = ''
        else:
            seq += i
    Dict[header] = seq
    # print(count)
    return Dict


def fasta2(fasta_file):
    count = 0
    seq = ''
    header = ''
    Dict = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
    for i in fasta_file:
        i = i.rstrip()
        if re.match(r'^>', i):
            count += 1
            if count % 1000000 == 0:
                print(count)

            if len(seq) > 0:
                Dict[header] = seq
                header = i[1:]
                header = header.split(" ")[0]
                seq = ''
            else:
                header = i[1:]
                header = header.split(" ")[0]
                seq = ''
        else:
            seq += i
    Dict[header] = seq
    # print(count)
    return Dict


def allButTheFirst(iterable, delim):
    x = ''
    length = len(iterable.split(delim))
    for i in range(1, length):
        x += iterable.split(delim)[i]
        x += delim
    return x[0:len(x)]


def filter(list, items):
    outLS = []
    for i in list:
        if i not in items:
            outLS.append(i)
    return outLS


def filterRe(list, regex):
    ls1 = []
    ls2 = []
    for i in list:
        if re.findall(regex, i):
            ls1.append(i)
        else:
            ls2.append(i)
    return ls1, ls2


def delim(line):
    ls = []
    string = ''
    for i in line:
        if i != " ":
            string += i
        else:
            ls.append(string)
            string = ''
    ls = filter(ls, [""])
    return ls


parser = argparse.ArgumentParser(
    prog="parahunter-dnds.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    ************************************************************************
    Developed by Arkadiy Garber; University of Montana, Biological Sciences
    Please send comments and inquiries to rkdgarber@gmail.com
    ************************************************************************
    '''))

parser.add_argument('-clu', type=str, help="clu.tsv output from mmseqs", default="NA")
parser.add_argument('-nuc', type=str, help="genes in nucleotide format", default="NA")
parser.add_argument('-aa', type=str, help="genes in amino acid format", default="NA")
parser.add_argument('-ctl', type=str, help="template control file for codeml", default="NA")

args = parser.parse_args()

nuc = open(args.nuc)
nuc = fasta2(nuc)

pep = open(args.aa)
pep = fasta2(pep)


cluDict = defaultdict(list)
clu = open(args.clu)
for i in clu:
    ls = (i.rstrip().split("\t"))
    cluDict[ls[0]].append(ls[1])

cwd = os.getcwd()

os.system('mkdir ' + cwd + "/dnds-analysis")

count = 0
for i in cluDict.keys():
    if len(cluDict[i]) > 1:
        name = (i.split("|")[0] + "_" + lastItem(i.split("_")))
        outpep = open(cwd + "/dnds-analysis/%s.faa" % name, "w")
        outnuc = open(cwd + "/dnds-analysis/%s.faa.fna" % name, "w")
        for j in cluDict[i]:
            outpep.write(">" + j + "\n")
            outnuc.write(">" + j + "\n")
            outpep.write(pep[j] + "\n")
            outnuc.write(nuc[j] + "\n")
        outpep.close()
        outnuc.close()
        count += 1


# ALIGNING PROTEIN SEQUENCES AND CREATING A CODON ALIGNMENT
DIR = cwd + "/dnds-analysis"
os.system("for i in %s/*faa; do"
          " muscle -in $i -out $i.aligned.fa;"
          " pal2nal.pl $i.aligned.fa $i.fna -output fasta > $i.codonalign.fa;"
          " done" % DIR)


# BUILDING CONTROL FILES
count = 0
codealign = os.listdir(DIR)
for file in codealign:
    if re.findall(r'codonalign', file):
        clu = file.split(".faa")[0]
        setup = open(args.ctl)
        out = open("%s/%s.ctl" % (DIR, str(clu)), "w")

        for i in setup:
            if re.findall('seqfile', i):
                out.write('' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + 'seqfile' + ' ' + '=' + ' dnds-analysis/' + file + ' ' + '*' + ' ' + 'sequence' + ' ' + 'data' + ' ' + 'filename\n')

            elif re.findall(r'outfile', i):
                out.write('' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + 'outfile' + ' ' + '=' + ' '
                          + 'dnds-analysis/mlcTree_' + str(clu) + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' ' + '' + ' '
                          + '' + ' ' + '' + ' ' + '' + ' ' + '*' + ' ' + 'main' + ' ' + 'result' + ' ' + 'file' + ' ' + 'name\n')

            else:
                out.write(i)
        out.close()


# RUNNING CODEML FOR DN/DS CALCULATION
codealign = os.listdir(DIR)
for file in codealign:
    if lastItem(file.split(".")) == "ctl":
        os.system("codeml dnds-analysis/%s" % (file))


# PARSING CODEML OUTPUT
dsDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 'EMPTY')))
dndsDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 'EMPTY')))
codealign = os.listdir(DIR)
for i in codealign:
    clu = i
    if re.findall(r'mlcTree', i):
        file = open("%s/%s" % (DIR, i), "r")
        for j in file:
            if re.findall(r'(\) \.\.\.)', j):
                ls = (j.rstrip().split("..."))
                orf1 = (ls[0].split("(")[1][0:len(ls[0].split("(")[1])-2])
                orf2 = (ls[1].split("(")[1][0:len(ls[1].split("(")[1])-1])
            if re.findall(r'  dS', j):
                secondHalf = (j.split("dN/dS=")[1])
                ls2 = (secondHalf.split(" "))
                dnds = (firstNonspace(ls2))
                dndsDict[orf1][orf2] = dnds
                dndsDict[orf2][orf1] = dnds

                dS = (j.rstrip().split(" dS")[1])
                dS = remove(dS, [" ", "="])
                dsDict[clu][orf1][orf2] = dS
                dsDict[clu][orf2][orf1] = dS

MLCdict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 'EMPTY')))
for i in dsDict.keys():
    for j in dsDict[i]:
        closestNeighbor = Dictparser(dsDict[i][j])[0]
        lowestDS = Dictparser(dsDict[i][j])[1]
        MLCdict[i][j]["closestNeighbor"] = closestNeighbor
        MLCdict[i][j]["lowestDS"] = lowestDS

out = open("dS_summary.csv", "w")
out.write("cluster" + "," + "gene" + "," + "closestNeighbor" + "," + "lowestDS" + "," + "dN/dS" + "\n")
for i in MLCdict.keys():
    for j in MLCdict[i]:
        out.write(i + "," + j + "," + MLCdict[i][j]["closestNeighbor"] + "," + MLCdict[i][j]["lowestDS"] + "," + dndsDict[j][MLCdict[i][j]["closestNeighbor"]] + "\n")
    out.write("####################################################################\n")

out.close()

os.system("rm 2NG.t 2NG.dN 2NG.dS rst1 rst 2ML.t 2ML.dN 2ML.dS 4fold.nuc rub")









