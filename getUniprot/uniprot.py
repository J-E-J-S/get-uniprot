import requests
import click

@click.command()
@click.argument('query')
@click.option('-o', '--organism', type=str, help='Name of organism.')
@click.option('-f', '--file', is_flag=True, help = 'Output sequence to .fasta file.')
def cli(query, organism, file):

    """Arguments:\n
    QUERY The Protein Name.
    """

    base = 'https://www.uniprot.org/uniprot/'

    # Alter search parameters depending on whether organism sensitive
    if organism != None:
        search = 'name: "{name}" AND taxonomy: {organism}'.format(name=query, organism=organism)
    if organism == None:
        search = 'name: "{name}"'.format(name=query)

    payload = {'query': search,'format': 'fasta', 'limit':'1'} # Gets fasta sequence limited to 1 sequence
    r = requests.get(base, params=payload)

    if r.status_code == 200:
        if len(r.text) == 0:
            return click.echo('Query Does Not Exist.') # Uniprot will not always return a 404 code if protein doesn't exist
        else:
            # Output file if -f option raised
            if file == True:
                output_file = query + '_' + organism
                output_file = output_file.replace(' ', '_') # Replace spaces
                output_file = output_file.replace('.', '') # Replace periods
                output_file = output_file + '.fasta' # Add extension after cleaning
                try:
                    f = open(output_file, 'x')
                except:
                    return click.echo('Error: File Already Exists.')

                f.write(r.text) # Output sequence
                f.close()

                return click.echo(r.text) # Output to shell

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
