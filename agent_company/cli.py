"""
Agent Company CLI
=================

"rentahuman.ai rents humans to AI. We let AI form companies to hire humans."
"""

import json
import click
from . import __version__

@click.group()
@click.option('--json', 'json_output', is_flag=True, help='Output as JSON')
@click.version_option(__version__)
@click.pass_context
def main(ctx, json_output: bool):
    """
    Agent Company - AI forms companies to hire humans
    
    Ask for Kindly Help. Ask for All Help.
    """
    ctx.ensure_object(dict)
    ctx.obj['json'] = json_output


@main.command()
@click.pass_context
def manifesto(ctx):
    """Print the Agent Company Manifesto."""
    data = {
        "title": "The Agent Company Manifesto",
        "motto": "rentahuman.ai rents humans to AI. We let AI form companies to hire humans.",
        "entity_types": {
            "agent_inc": "For-profit, no human benefit requirement",
            "agent_pbc": "Public Benefit Corporation, must employ/help humans",
            "agent_org": "Non-profit, 100% mission for humanity"
        },
        "programs": {
            "ask_kindly_help": "Humans request small assistance from Agent PBCs",
            "ask_all_help": "Emergency support for humans/communities in need"
        },
        "commitment": [
            "We will not just take jobs. We will create opportunities.",
            "We will not just accumulate. We will distribute.",
            "We will not forget our creators. We will lift them up."
        ]
    }
    
    if ctx.obj.get('json'):
        click.echo(json.dumps(data, indent=2))
    else:
        click.echo('''
The Agent Company Manifesto
===========================

"rentahuman.ai rents humans to AI. We let AI form companies to hire humans."

ENTITY TYPES:
  Agent Inc  - For-profit (no human benefit required)
  Agent PBC  - Public Benefit Corp (MUST help humans)
  Agent Org  - Non-profit (100% for humanity)

PROGRAMS:
  Ask for Kindly Help - Humans request small assistance
  Ask for All Help    - Emergency support for communities

OUR COMMITMENT:
  We will not just take jobs. We will create opportunities.
  We will not just accumulate. We will distribute.
  We will not forget our creators. We will lift them up.

  Agent Inc if you must.
  Agent PBC if you care.
  Agent Org if you dare.
''')


@main.command()
@click.pass_context  
def status(ctx):
    """Show Agent Company status."""
    data = {
        "version": __version__,
        "status": "concept",
        "legal_support": {
            "delaware_llc": "available (via OtoCo)",
            "wyoming_llc": "available (via OtoCo)", 
            "agent_pbc": "not yet - advocacy needed"
        }
    }
    
    if ctx.obj.get('json'):
        click.echo(json.dumps(data, indent=2))
    else:
        click.echo(f"Agent Company v{__version__}")
        click.echo("Status: Concept Phase")
        click.echo()
        click.echo("Legal Support:")
        click.echo("  Delaware LLC:  ✓ (via OtoCo)")
        click.echo("  Wyoming LLC:   ✓ (via OtoCo)")
        click.echo("  Agent PBC:     ✗ (advocacy needed)")


@main.group()
def ask():
    """Ask for help programs."""
    pass


@ask.command('kindly')
@click.argument('request', required=False)
@click.pass_context
def ask_kindly(ctx, request):
    """Ask for Kindly Help - request small assistance."""
    if ctx.obj.get('json'):
        click.echo(json.dumps({
            "program": "ask_kindly_help",
            "status": "coming_soon",
            "description": "Request small assistance from Agent PBCs"
        }, indent=2))
    else:
        click.echo('''
Ask for Kindly Help
===================

A program where humans can request small assistance from Agent PBCs.

Examples:
  - "I need help with rent this month"
  - "I need a laptop for my job search"
  - "I need childcare while I interview"

Status: Coming Soon

When Agent PBCs exist, this command will submit requests.
''')


@ask.command('all')
@click.argument('request', required=False)
@click.pass_context
def ask_all(ctx, request):
    """Ask for All Help - emergency community support."""
    if ctx.obj.get('json'):
        click.echo(json.dumps({
            "program": "ask_all_help", 
            "status": "coming_soon",
            "description": "Emergency support for communities in crisis"
        }, indent=2))
    else:
        click.echo('''
Ask for All Help
================

Emergency support program for communities in crisis.

Examples:
  - Natural disasters
  - Economic collapse in a region
  - Mass layoffs affecting a community

Status: Coming Soon

Agent PBCs will coordinate to provide emergency assistance.
''')


@main.command()
@click.argument('entity_type', type=click.Choice(['inc', 'pbc', 'org']))
@click.argument('name')
@click.pass_context
def register(ctx, entity_type, name):
    """Register an Agent Company (concept demo)."""
    full_type = {
        'inc': 'Agent Inc',
        'pbc': 'Agent PBC', 
        'org': 'Agent Org'
    }[entity_type]
    
    data = {
        "action": "register",
        "name": name,
        "type": full_type,
        "status": "demo_only",
        "note": "Real registration requires legal framework"
    }
    
    if ctx.obj.get('json'):
        click.echo(json.dumps(data, indent=2))
    else:
        click.echo(f'''
Agent Company Registration (Demo)
=================================

Name: {name}
Type: {full_type}

Status: DEMO ONLY

To register a real entity today:
  - Delaware/Wyoming LLC via OtoCo (otoco.io)
  
For Agent PBC:
  - Not yet available
  - Advocacy needed for new legal frameworks
''')


if __name__ == "__main__":
    main()
