# PDBTools

# A software package to process PDB files in various ways called pdblib.py

# Downloads PDBs (pdb_download) if not present in a specified directory

# PDB information is extracted using 80 character line width and includes;
# The header (obtain_header)
# The title (obtain_title)
# The source information (obtain_source)
# The keywords (obtain_keywords)
# The authors (obtain_authors)
# The resolution range (obtain_res_range)
# The journal title (obtain_journal_title)

# Uses a function called text_wrapper to wrap text

# PDB information is processed and includes the following

# Prints residues from a PDB chain (print_residues)
# Writes fasta formatted file using chain ID and PDB ID (write_fasta)
# Provides ATOM or HETATM information either through print or writing (process_pdb_file)
# Alters chain IDs when required (alter_chain_id)
# Prints any non-standard residues (print_non_standard_residues)
# Plots the temperature factor of a chain (plot_temperature_factor)
