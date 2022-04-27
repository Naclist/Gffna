# Gffna
Some Bioinformatic tools during my days in Prof Zhou's lab. 

Extract partial sequence (CDS or other functional genes) from a fasta file according to its GFF file.

Useful for me, while still not friendly to you.

Gffna --gff [input .gff file] --fna [input .fna file] --type [type: CDS, tRNA, exon... default: CDS] --protein [optional, generate sequence of amino acids]

--gff
Required, standard gff file (Example: downloaded from NCBI) was recommanded. It could also handle the gff annotated by Prokka but might lead to some potential errors.

--fna
Required, your fna and gff files should be matched (gff should be annotated according to this fna) to ensure consistency of seqid.

(--output)
I should have set a output here but I was lazy that night.

--type
Optional, you can specify a type of gene to look for: CDS, tRNA, gene, exon .... Default: CDS.

--protein
Optional, if you want an output in amino acids sequence.
