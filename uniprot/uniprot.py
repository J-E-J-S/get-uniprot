import requests
import click
import os

def uniprot_request(name, organism, review='yes'):

    base = 'https://www.uniprot.org/uniprot/'
    query = 'name: "{name}" AND taxonomy: {organism} AND reviewed:{reviewed}'.format(name=name, organism=organism, reviewed=review)
    payload = {'query': query,'format': 'fasta', 'limit':'1'} # Gets fasta sequence limited to 1 sequence

    r = requests.get(base, params=payload)

    if r.status_code == 200:
        if len(r.text) == 0:
            return click.echo('Query Does Not Exist.') # Uniprot will not always return a 404 code if protein doesn't exist
        else:
            return r.text # Return .fasta sequence 

    # Error Handling
    if r.status_code == 400:
        return click.echo('Problem with Input.')
    if r.status_code == 404:
        return click.echo('Query Does Not Exist.')
    if r.status_code == 500 or r.status_code == 503:
        return click.echo('Uniprot API Service Down.')
    elif r.status_code != 200:
        return click.echo('An Error has Occurred.')








a = uniprot_request('eEF1A', 's. cerevisiae')
print(a)
