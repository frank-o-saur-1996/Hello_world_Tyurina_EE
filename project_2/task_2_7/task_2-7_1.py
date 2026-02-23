files = ["seq1", "seq2", "seq3", "seq4"]
data = "21.06.2002"

for name in files:
   new_name = name + "." + data + ".fasta"
   print(f"{new_name}")