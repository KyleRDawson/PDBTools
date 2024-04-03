import sys
from PDBTools import pdblib

def print_menu():
    print("\n=== PDB Tools Menu ===")
    print("1. Download PDB file")
    print("2. Display header information")
    print("3. Display title information")
    print("4. Display source information")
    print("5. Display keyword information")
    print("6. Display author information")
    print("7. Display resolution range")
    print("8. Display journal title")
    print("9. Print residues for a chain")
    print("10. Write FASTA file")
    print("11. Process PDB file")
    print("12. Alter chain ID")
    print("13. Print non-standard residues")
    print("14. Plot temperature factor")
    print("quit/q/Q - Quit the program")

def main():
    if len(sys.argv) == 1:
        print_menu()
        while True:
            choice = input("\nEnter your choice: ").strip().lower()
            if choice in ['quit', 'q']:
                print("Exiting the program.")
                break
            elif choice == '1':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                pdblib.pdb_download(pdb_id)
            elif choice == '2':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                print(pdblib.obtain_header(pdb_id))
            elif choice == '3':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                print(pdblib.obtain_title(pdb_id))
            elif choice == '4':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                print(pdblib.obtain_source_details(pdb_id))
            elif choice == '5':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                print(pdblib.obtain_keywords(pdb_id))
            elif choice == '6':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                print(pdblib.obtain_authors(pdb_id))
            elif choice == '7':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                print(pdblib.obtain_res_range(pdb_id))
            elif choice == '8':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                print(pdblib.obtain_journal_title(pdb_id))
            elif choice == '9':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                chain_id = input("Enter chain ID: ").strip().upper()
                pdblib.print_residues(pdb_id, chain_id, "data")
            elif choice == '10':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                pdblib.write_fasta(pdb_id, "data")
            elif choice == '11':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                chain_id = input("Enter chain ID: ").strip().upper()
                pdblib.process_pdb_file(pdb_id, "data", chain_id)
            elif choice == '12':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                old_chain_id = input("Enter current chain ID: ").strip().upper()
                new_chain_id = input("Enter new chain ID: ").strip().upper()
                pdblib.alter_chain_id(pdb_id, "data", old_chain_id, new_chain_id)
            elif choice == '13':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                pdblib.print_non_standard_residues(pdb_id, "data")
            elif choice == '14':
                pdb_id = input("Enter PDB ID: ").strip().lower()
                chain_id = input("Enter chain ID: ").strip().upper()
                output_file = input("Enter output file name: ").strip()
                pdblib.plot_temperature_factor(pdb_id, "data", chain_id, output_file)
            else:
                print("Invalid choice. Please enter a valid option or 'quit' to exit.")
                print("\n=== PDB Tools Menu ===")
                print("1. Download PDB file")
                print("2. Display header information")
                print("3. Display title information")
                print("4. Display source information")
                print("5. Display keyword information")
                print("6. Display author information")
                print("7. Display resolution range")
                print("8. Display journal title")
                print("9. Print residues for a chain")
                print("10. Write FASTA file")
                print("11. Process PDB file")
                print("12. Alter chain ID")
                print("13. Print non-standard residues")
                print("14. Plot temperature factor")
                print("quit/q/Q - Quit the program")
    else:
        print("Usage: python checkPDB.py")

if __name__ == "__main__":
    main()
