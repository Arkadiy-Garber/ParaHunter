# ParaHunter

## easy-installation:
  
    git clone https://github.com/Arkadiy-Garber/ParaHunter.git
    cd ParaHunter
    ./setup.sh
    conda activate parahunt

## quick-start

    ParaHunter.sh -a genomeOrfs_aa.faa -n genomeOrfs_nuc.fna

### setting minimum amino acid identity for clustering to 35%, with query coverage of at least 50%

    ParaHunter.sh -a genomeOrfs_aa.faa -n genomeOrfs_nuc.fna -m 0.35 -c 0.5
