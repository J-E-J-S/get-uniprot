import requests
import click
import os

def uniprot_request(name, organism, review='yes'):

    base = 'https://www.uniprot.org/uniprot/'
    query = 'name: "{name}" AND taxonomy: {organism} AND reviewed:{reviewed}'.format(name=name, organism=organism, reviewed=review)
    payload = {'query': query,'format': 'fasta', 'limit':'1'} # Gets fasta sequence limited to 1 sequence 

    r = requests.get(base, params=payload)
    print(r.text)




uniprot_request('eEF1A', 's. cerevisiae')
