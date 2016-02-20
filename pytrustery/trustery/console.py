"""Console application for Trustery."""

import logging

import click

from trustery.events import Events
from trustery.transactions import Transactions


class StrParamType(click.ParamType):
    """Click parameter type that converts data using str()."""
    name = 'STR'

    def convert(self, value, param, ctx):
        return str(value)

STR = StrParamType()


@click.group()
def cli():
    """Ethereum-based identity system."""
    # Prevents the requests module from printing INFO logs to the console.
    logging.getLogger("requests").setLevel(logging.WARNING)


@cli.command()
@click.option('--attributetype', prompt=True, type=STR)
@click.option('--has_proof', prompt=True, type=bool)
@click.option('--identifier', prompt=True, type=STR)
@click.option('--data', prompt=True, type=STR)
@click.option('--datahash', prompt=True, type=STR)
def rawaddattribute(attributetype, has_proof, identifier, data, datahash):
    """(Advanced) Manually add an attribute about your identity."""
    transactions = Transactions()
    transactions.add_attribute(attributetype, has_proof, identifier, data, datahash)

    click.echo()
    click.echo("Transaction sent.")


@cli.command()
@click.option('--attributeid', prompt=True, type=STR)
@click.option('--expiry', prompt=True, type=STR)
def rawsignattribute(attributeID, expiry):
    """(Advanced) Manually sign an attribute about an identity."""
    transactions = Transaction()
    transactions.sign_attribute(attributeID, expiry)

    click.echo()
    click.echo("Transaction sent.")


@cli.command()
@click.option('--signatureid', prompt=True, type=STR)
def rawrevokeattribute(signatureID):
    """(Advanced) Manaully revoke your signature about an identity."""
    tranactions = Transaction()
    transactions.revoke_signature(signatureID)

    click.echo()
    click.echo("Transaction sent.")


@cli.command()
@click.option('--attributetype', help='Attribute type', type=STR)
@click.option('--identifier', help='Attribute identifier', type=STR)
@click.option('--owner', help='Attribute owner', type=STR)
def search(attributetype, identifier, owner):
    """Search for attributes."""
    events = Events()
    attributes = events.filter_attributes(None, identifier, owner)

    for attribute in attributes:
        if attributetype is not None and attributetype != attribute['attributeType']:
            continue
            
        click.echo("Attribute ID #" + str(attribute['attributeID']) + ':')
        click.echo("\tType: " + attribute['attributeType'])
        click.echo("\tOwner: " + attribute['owner'])
        click.echo("\tIdentifier: " + attribute['identifier'])
        click.echo()
