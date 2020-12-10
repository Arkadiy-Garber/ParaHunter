# ParaHunter
If you found this software useful to your research please cite as follows: Garber AI, Miller, SR (2020) ParaHunter: identification of gene paralogs in genomes. Publication coming soon. doi: [LINK](actual LINK)

### easy-installation:
  
    git clone https://github.com/Arkadiy-Garber/ParaHunter.git
    cd ParaHunter
    ./setup.sh
    source activate parahunt

### quick-start

    ParaHunter.sh -a genomeOrfs_aa.faa -n genomeOrfs_nuc.fna

### setting minimum amino acid identity for clustering to 35%, with query coverage of at least 50%

    ParaHunter.sh -a genomeOrfs_aa.faa -n genomeOrfs_nuc.fna -m 0.35 -c 0.5
