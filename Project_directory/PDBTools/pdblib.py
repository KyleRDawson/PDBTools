def text_wrapper(text, width=80):                                                   
    """
    Use: Text wrapper tool so make sure line width is never greater than 80 characters
    Arguments: Input if the text in question and the default line width of 80
    Return: Returns text with a width of 80
    """
    text_wrapper_list = []                                                                                              
    line = ""                                                                    
    
    for text in text.split():                                                    
        if len(line) + len(text) < width:                                   # checking if the length of the line + current word is less than width                                     
            line += text + " "                                                     
        else:
            text_wrapper_list.append(line.strip())                          # appending information and stripping whitespace                                 
            line = text + " "                                               # adding the word and a space                                                      
    text_wrapper_list.append(line.strip())                                         
    return "\n".join(text_wrapper_list)           

def pdb_download(pdbid):                                                                       
    """
    Use: Downloads a PDB if not available locally within the data folder of a project folder
    Arguments: Input is the 4 letter PDB ID of the structure, can be lower case or upper case
    Retruns: Returns the path of the downloaded file
    """ 
    
    import os                                                                       
    import requests                                                                 
    
    filename = f"{pdbid.upper()}.pdb"                                               
    path = os.path.join("data", filename)                                           
    
    if not os.path.exists(path):                                            # if file not in path location                                                                                                                       
        url = f"https://files.rcsb.org/download/{pdbid.upper()}.pdb"        # download pdb              
        print(f"{pdbid.upper()} is being downloaded: {url}")                     
        response = requests.get(url)                                             
        
        if response.status_code == 200:                                     # successful connection                                        
            with open(path, "wb") as wfile:                                 
                wfile.write(response.content)                               # writing file     
            print(f"File saved as {pdbid.upper()}")                            
        else:
            print(f"Failure. Error {response.status_code} has been encountered") 
            return None  
            
    else:
        print(f"{pdbid.upper()} already present locally: {path}")                 
    return path

def text_wrapper(text, width=80):                                                   
    """
    Use: Text wrapper tool so make sure line width is never greater than 80 characters
    Arguments: Input if the text in question and the default line width of 80
    Return: Returns text with a width of 80
    """
    text_wrapper_list = []                                                                                              
    line = ""                                                                    
    
    for text in text.split():                                                    
        if len(line) + len(text) < width:                                   # checking if the length of the line + current word is less than width                                     
            line += text + " "                                                     
        else:
            text_wrapper_list.append(line.strip())                          # appending information and stripping whitespace                                 
            line = text + " "                                               # adding the word and a space                                                      
    text_wrapper_list.append(line.strip())                                         
    return "\n".join(text_wrapper_list)           

def obtain_header(pdbid, directory):
    """
    Use: Obtain header information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question and the directory
    Return: Returns the header information
    """
    import os                                                                      
    
    filename = f"{pdbid.upper()}.pdb"                                               
    path = os.path.join(directory, filename)                                        
    header_lines = []                                                                                                                   

    try:
        with open(path, "r") as rfile:
            for line in rfile:
                line = line.strip()                                              
                if line.startswith("HEADER"):                               # isolating header information                                      
                    header_lines.append(line[7:].strip())                   # removing unnecessary information and appending                         
                elif header_lines:                                                  
                    break                                                          
    except FileNotFoundError:                                                       
        print(f"Error: {filename} not found")
        return None
    except Exception as e:                                                       
        print(f"Error: {e}")
        return None

    if header_lines:                                                               
        header = " ".join(header_lines)
        return text_wrapper(header)                                         # feeding into text_wrapper                                              
    else:
        print("No header information")
        return None
    
    
def obtain_title(pdbid, directory):
    """
    Use: Obtain title information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question and the directory
    Return: Returns the title information
    """
    import os                                                                    
    filename = f"{pdbid.upper()}.pdb"                                            
    path = os.path.join(directory, filename)                                      
    title_lines = []                                                           
    title_started = False                                                   # expecting multiple lines for title                                                      

    try:
        with open(path, "r") as rfile:
            for line in rfile:
                line = line.strip()                                             
                if line.startswith("TITLE"):                                # isolating title information                                     
                    if not title_started:                                   # for first line
                        title_started = True                                       
                        title_lines.append(line[6:].strip())                # appending information for first line                      
                    else:
                        title_lines[-1] += " " + line[11:].strip()          # appending information for second line                
                elif title_started:                                            
                    break
    except FileNotFoundError:                                                    
        print(f"Error: {filename} not found")
    except Exception as e:                                                     
        print(f"Error: {e}")

    if title_lines:                                                               
        title = " ".join(title_lines)                                       # rejoining all text                                             
        return text_wrapper(title)                                          # feeding into wrapper                                                
    else:
        print("No title information")
        return None

def obtain_source_details(pdbid, directory):
    """
    Use: Obtain source information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question and the directory
    Return: Returns the source information
    """
    import os
    
    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    source_details = []
    source_started = False                                                 # expecting multiple lines for range

    try:
        with open(path, "r") as rfile:
            for line in rfile:
                line = line.strip()
                if line.startswith("SOURCE"):                               # isolating SOURCE information
                    if not source_started:
                        source_started = True
                        source_details.append(line[10:].strip())            # appending information for first line
                    else:
                        source_details[-1] += " " + line[10:].strip()       # appending information for second line  
                elif source_started:
                    break
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    if source_details:
        source_details_joined = "; ".join(source_details)
        return text_wrapper(source_details_joined)                          # rejoining all text & feeding to wrapper
    else:
        print("No source information")
        return None

def obtain_keywords(pdbid, directory):
    """
    Use: Obtain keywords information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question and the directory
    Return: Returns the keywords information
    """
    import os
    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    keyword_lines = []
    keywords_started = False                                                # expecting multiple lines for keywrds

    try:
        with open(path, "r") as rfile:
            for line in rfile:
                line = line.strip()
                if line.startswith("KEYWDS"):                               # isolating keywrds information 
                    if not keywords_started:                                # for first line
                        keywords_started = True
                        keyword_lines.append(line[7:].strip())              # appending information for first line  
                    else:
                        keyword_lines[-1] += " " + line[11:].strip()        # appending information for second line 
                elif keywords_started:
                    break
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    if keyword_lines:
        keyword = " ".join(keyword_lines)                                   # rejoining all text 
        return text_wrapper(keyword)                                        # feeding into wrapper
    else:
        print("Keywords section not found.")
        return None 
    
def obtain_authors(pdbid, directory):
    """
    Use: Obtain authors information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question and the directory
    Return: Returns the authors information
    """
    import os
    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    author_info = []  

    try:
        with open(path, "r") as rfile:
            for line in rfile:
                line = line.strip()
                if line.startswith("AUTHOR"):                               # isolating author information 
                    author_info.append(line[7:].strip())                    # appending information  
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")

    if author_info:
        return text_wrapper("\n".join(author_info))                         # rejoining all text & feeding to wrapper  
    else:
        print("No author information")
        return None
    
def obtain_res_range(pdbid, directory):
    """
    Use: Obtain resolution range information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question and the directory
    Return: Returns the resolution range information
    """
    import os
    
    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    res_lines = []
    reslines_started = False                                                # expecting multiple lines for range
    
    try:
        with open(path, "r") as rfile:
            for line in rfile:
                line = line.strip()
                if line.startswith("REMARK") and "(ANGSTROMS)" in line:     # isolating REMARK and ANG information
                    if not reslines_started:
                        reslines_started = True                  
                        res_lines.append(line[13:].strip())                 # appending information for first line
                    else:
                        res_lines[-1] += " " + line[30:].strip()            # appending information for second line  
                elif res_lines:
                    break
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    if res_lines:
        return text_wrapper("\n".join(res_lines))                           # rejoining all text & feeding to wrapper
    else:
        print("Resolutions section not found")
        return None

def obtain_journal_title(pdbid, directory):
    """
    Use: Obtain journal title information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question and the directory
    Return: Returns the journal title information
    """
    import os
    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    journal_lines = []
    jtitle_started = False                                                  # expecting multiple lines for jtitle

    try:
        with open(path, "r") as rfile:
            for line in rfile:
                line = line.strip()
                if line.startswith("JRNL") and "TITL" in line:              # isolating JRNL and TITL information
                    if not jtitle_started:
                        jtitle_started = True
                        journal_lines.append(line[19:].strip())             # appending information for first line 
                    else:
                        journal_lines[-1] += " " + line[19:].strip()        # appending information for second line
                elif journal_lines:
                    break
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    # Print or return the journal title section as a single line
    if journal_lines:
        return text_wrapper("\n".join(journal_lines))                       # rejoining all text & feeding to wrapper
    else:
        print("Journal title section not found.")
        return None

def print_residues(pdbid, chain_id, directory):
    """
    Use: Obtain residues from a PDB and Chain ID
    Arguments: Input the 4 letter code for the PDB in question and the directory with chain ID
    Return: Prints the residues for the chain
    """  
    import os
    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    residues = ""
    try:
        with open(path, "r") as file:
            for line in file:
                if line.startswith("ATOM") and line[21] == chain_id and line[13:15] == "CA":    # using only alpha carbon information
                    res_name = line[17:20].strip()
                    residues += get_single_letter_code(res_name)                                # using a second function to get the three letter code instead
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    if residues:
        print(residues)
    else:
        print("No residue information")

def get_single_letter_code(res_name):
    residue_codes = {
        "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
        "GLU": "E", "GLN": "Q", "GLY": "G", "HIS": "H", "ILE": "I",
        "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
        "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V"
    }
    return residue_codes.get(res_name, "X")


def write_fasta(pdb_id, directory, chain_id=None, output_file="output.fasta"):
    """
    Use: Writes a fasta formatted file using chain ID and PDB
    Arguments: Input the 4 letter code for the PDB in question and the directory with chain ID, if no chain is given all chains will be written
    Return: File containing amino acid sequences of chains
    """
    import os
    sequences = []
    current_chain = None
    current_sequence = ""

    filename = f"{pdb_id.upper()}.pdb"  
    path = os.path.join(directory, filename)
    try:
        with open(path, "r") as pdb_file:
            for line in pdb_file: 
                if line.startswith("ATOM") and line[21] != " " and line[13:15] == "CA":     # using alpha carbon of ATOM section only
                    pdb_chain_id = line[21]  
                    if pdb_chain_id != current_chain:
                        if current_sequence:
                            header = f">{pdb_id.upper()}_{current_chain}"
                            sequences.append((header, current_sequence))                    # appending a tuple of the header information and the current sequence
                        current_chain = pdb_chain_id
                        current_sequence = ""
                    res_name = line[17:20].strip()
                    current_sequence += res_name

            if current_sequence:
                header = f">{pdb_id.upper()}_{current_chain}"
                sequences.append((header, current_sequence))

            if chain_id:
                sequences = [seq for seq in sequences if seq[0].endswith(chain_id.upper())]

            output_path = os.path.join(directory, output_file)
            with open(output_path, "w") as f:
                for header, seq in sequences:
                    f.write(f"{header}\n")
                    for i in range(0, len(seq), 80):                                        # writing to a file with width 80
                        f.write(seq[i:i+80] + "\n")
        print(f"FASTA file saved as {output_path}")
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


write_fasta('1h7x', 'data', chain_id=None, output_file="output.fasta")

def process_pdb_file(pdbid, directory, chain_id, record_type=None, mode="print"):
    """
    Use: Obtain information from a PDB file
    Arguments: Input the 4 letter code for the PDB in question, the directory of the file, the chain ID you are interested
    Arguments cont: The record type, can be "ATOM" or "HETATM" information and the mode of either print or write
    Return: Returns the resolution range information
    """

    if mode not in ("print", "write"):
        raise ValueError("Invalid mode. Please choose 'print' or 'write'.")
    if record_type not in (None, "ATOM", "HETATM"):
        raise ValueError("Invalid record. Please choose 'ATOM' or 'HETATM'.")
    import os
    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    try:
        with open(path, "r") as pdb_file:
            if mode == "write":                                         # specifying the write mode
                out_filename = f"{filename[:-4]}_{chain_id}.pdb"
                with open(out_filename, "w") as out_file:
                    for line in pdb_file:
                        if (record_type is None or line.startswith(record_type)) and (chain_id in line and line[21] == chain_id):  # extracting information based on record type, chain ID
                            out_file.write(line)
                print(f"Relevant lines written to: {out_filename}")
            else:                                                       # specidying the print mode
                for line in pdb_file:
                    if (record_type is None or line.startswith(record_type)) and (chain_id in line and line[21] == chain_id):       # extracting information based on record type, chain ID
                        print(line, end="")
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def alter_chain_id(pdbid, directory, old_chain_id, new_chain_id):
    """
    Use: Altering chain ID information in PDB
    Arguments: Input the 4 letter code for the PDB in question, the directory of the file, the chain ID you are interested and the new chain ID
    Arguments cont: The record type, can be "ATOM" or "HETATM" information and the mode of either print or write
    Return: Returns the resolution range information
    """
    import os

    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    out_filename = f"{pdbid.upper()}_{new_chain_id}.pdb"
    out_path = os.path.join(directory, out_filename)

    try:
        with open(path, "r") as pdb_file, open(out_path, "w") as out_file:
            for line in pdb_file:
                if line.startswith("ATOM") or line.startswith("HETATM"):            # only selecting ATOM and HETATM information
                    if line[21] == old_chain_id:
                        line = line[:21] + new_chain_id + line[22:]                 # replacing the chain ID information
                out_file.write(line)
        print(f"Chain ID altered and saved to: {out_path}")
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except Exception as e:
        print(f"Error: {e}")

def print_non_standard_residues(pdbid, directory):  
    """
    Use: Print non-standard protein residue names present in a PDB file.
    Arguments: Input the 4 letter code for the PDB in question and the directory of the file.
    Return: None
    """
    import os

    filename = f"{pdbid.upper()}.pdb"
    path = os.path.join(directory, filename)
    non_standard_residues = set()
    amino_acids = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]

    try:
        with open(path, "r") as rfile:
            for line in rfile:
                if line.startswith("HETATM") and line[17:20].strip() not in amino_acids:            # excluding all standard amino acids, only selecting those within HETATM
                    non_standard_residues.add(line[17:20].strip())
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    if non_standard_residues:
        print(" ".join(non_standard_residues))
    else:
        print("No non-standard residues found.")

def plot_temperature_factor(pdb_id, directory, chain_id, output_file, figsize=(8, 6)):   
    """
    Use: Plots the temperature factor
    Arguments: Input the 4 letter code for the PDB in question and the directory of the file, the chain ID and the ouputfile name.
    Return: Plotted figure
    """
    
    import matplotlib.pyplot as plt
    import os
    try:
        residue_numbers = []
        temperature_factors = []

        filename = f"{pdb_id.upper()}.pdb"
        path = os.path.join(directory, filename)
        with open(path, "r") as pdb_file:
            for line in pdb_file:
                if line.startswith("ATOM") and line[21] == chain_id:        # specifying only ATOM section and chain ID
                    residue_numbers.append(int(line[22:26]))                # converting the residue number to an int for plotting
                    temperature_factors.append(float(line[60:66]))          # converting the temperature information to a float for plotting

        plt.figure(figsize=figsize)
        plt.plot(residue_numbers, temperature_factors, color='blue')
        plt.title(f"Temperature Factor of Chain {chain_id}")
        plt.xlabel("Residue Number")
        plt.ylabel("Temperature Factor (B-factor)")
        plt.grid(True)
        plt.savefig(os.path.join(directory, output_file))
        plt.show()
        
        print(f"Plot saved as {output_file}")
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except Exception as e:
        print(f"Error: {e}")
