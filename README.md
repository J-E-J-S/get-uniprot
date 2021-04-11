## Get-Uniprot: A Simple Python CLI for Grabbing Protein Sequences. 🧬

![](/assets/get-uniprot.gif)

### Prerequisites:  
- Python >=3.6  

### Quickstart:  
```
pip install get-uniprot  
```
### Usage:  
```
Usage: uniprot [OPTIONS]

Options:
  -q, --query TEXT     Name of protein.
  -o, --organism TEXT  Name of organism.
  -f, --file           Output sequence to .fasta file.
  --help               Show this message and exit.
```
e.g.  
```
uniprot -q eEF1A -o 'S. cerevisiae' -f  
```
### Output:  
Command will output sequence to the shell and create a .fasta file in the current directory if -f supplied.
