import requests
import click
import os

@click.command()
@click.option('-q', '--query', type=str)
@click.option('-o', '--organism', type=str)
#@click.option('-r', '--review', default='yes', type=str)
def cli(query, organism, review='yes'):

    base = 'https://www.uniprot.org/uniprot/'
    search = 'name: "{name}" AND taxonomy: {organism} AND reviewed:{reviewed}'.format(name=query, organism=organism, reviewed=review)
    payload = {'query': search,'format': 'fasta', 'limit':'1'} # Gets fasta sequence limited to 1 sequence

    r = requests.get(base, params=payload)

    if r.status_code == 200:
        if len(r.text) == 0:
            return click.echo('Query Does Not Exist.') # Uniprot will not always return a 404 code if protein doesn't exist
        else:
            return click.echo(r.text) # Output .fasta sequence to shell

    # Error Handling
    if r.status_code == 400:
        return click.echo('Problem with Input.')
    if r.status_code == 404:
        return click.echo('Query Does Not Exist.')
    if r.status_code == 500 or r.status_code == 503:
        return click.echo('Uniprot API Service Down.')
    elif r.status_code != 200:
        return click.echo('An Error has Occurred.')


if __name__ == '__main__':
    cli()
