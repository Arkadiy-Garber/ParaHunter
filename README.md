# ParaHunter
If you found this software useful to your research please cite as follows:

Garber, AI and Miller, SR (2020) ParaHunter: identification of gene paralogs in genomes. GitHub repository: https://github.com/Arkadiy-Garber/ParaHunter.

ParaHunter uses [MMseqs2](https://www.nature.com/articles/nbt.3988) to cluster sequences from a single genomic dataset, based on a set of user-defined parameters. The clustered genes are then aligned using [Muscle](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC390337/) and [PAL2NAL](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1538804/), and pairwise dS, dN, and dN/dS values are calculated using [PAML](https://pubmed.ncbi.nlm.nih.gov/17483113/).

## easy-installation:
  
    git clone https://github.com/Arkadiy-Garber/ParaHunter.git
    cd ParaHunter
    bash setup.sh
    source activate parahunt

## quick-start

    ParaHunter.sh -a genomeOrfs_aa.faa -n genomeOrfs_nuc.ffn

### setting minimum amino acid identity for clustering to 35%, with query coverage of at least 50%

    ParaHunter.sh -a genomeOrfs_aa.faa -n genomeOrfs_nuc.ffn -m 0.35 -c 0.5


## Tutorial (Binder)

This software uses PAML, in addition to other tools like MMseqs2 and Muscle. If you would like to learn more about what is going on under the hood of this program, and some of the theoretical framework behind the evolutionary biology of gene divergence estimates, please see the following slideshow and associated video:

[Slideshow](https://github.com/biovcnet/topic-pop-gen-and-comparative-genomics/blob/master/Lesson-1/Comparative-Genomics-Lesson-1.pdf) | [Video presentation](https://www.youtube.com/watch?v=NtFuHFp0xB4)


## Walkthrough

If you'd like to try out this program in a virtual terminal session with all dependencies and test dataset pre-loaded, hit the 'launch binder' button below, and follow the commands in 'Walkthrough'

[![Binder](https://mybinder.org/badge_logo.svg)](https://gesis.mybinder.org/binder/v2/gh/biovcnet/bvcn-binder-paml/master?urlpath=lab)

(Initially forked from [here](https://github.com/binder-examples/conda). Thank you to the awesome [binder](https://mybinder.org/) team!)

You can also follow along in this linked video:
[Video presentation](https://www.youtube.com/watch?v=stjJHfQ51sA&t=1179s)


These videos were made as part of the [Bioinformatics Virtual Coordination Network](https://biovcnet.github.io/) :)

### Using PAML

Enter the first direcotry

    cd interspecies_example//

Align the FASTA amino acid file

    muscle -in MNBX01000583.1_4.faa -out MNBX01000583.1_4.fa

Make a codon alignment from the peptide alignment and nucleotide sequence

    pal2nal.pl MNBX01000583.1_4.fa MNBX01000583.1_4.ffn -output fasta > MNBX01000583.1_4.codonalign.fa

Check that the correct input/output files are in the codeml.ctl file

    less codeml.ctl

Run codeml

    codeml codeml.ctl

Enter the second directory

    cd intraspecies_example/

Align the FASTA amino acid file

    muscle -in NC_009928.1_232.faa -out NC_009928.1_232.fa

Make a codon alignment from the peptide alignment and nucleotide sequence

    pal2nal.pl NC_009928.1_232.fa NC_009928.1_232.ffn -output fasta > NC_009928.1_232.codonalign.fa

Run codeml after checking out the input/output codeml.ctl file

    codeml codeml.ctl


### ParaHunter tutorial

Print the ParaHunter help menu

    Parahunter.sh -h

Run program on the test dataset

    cd ParaHunter/
    cd cyanothece/
    ParaHunter.sh -a CyanothecePCC7425.faa -n CyanothecePCC7425.ffn -l ../codeml-2.ctl

