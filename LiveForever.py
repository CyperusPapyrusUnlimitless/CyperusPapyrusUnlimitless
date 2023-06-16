from Bio import SeqIO

# Load the human genome sequence from a FASTA file
genome_file = "human_genome.fasta"
genome = SeqIO.read(genome_file, "fasta")

# Print basic information about the genome
print("Genome ID:", genome.id)
print("Genome description:", genome.description)
print("Genome length:", len(genome))

# Find a specific pattern (motif) in the genome
motif = "ACGT"
matches = genome.seq.count(motif)
print("Number of matches for motif", motif, ":", matches)

# Search for a specific gene by its name or identifier
gene_name = "BRCA1"
gene_sequence = genome.seq.find(gene_name)
if gene_sequence != -1:
    print("Gene", gene_name, "found at position", gene_sequence)
else:
    print("Gene", gene_name, "not found in the genome")

# Perform sequence alignment with another DNA sequence
sequence_to_align = "GATTACA"
alignment = genome.seq.align(sequence_to_align)
print("Alignment score:", alignment.score)
print("Alignment details:")
for alignment_record in alignment:
    print(alignment_record)

