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
            "agent_inc": "For-profit",
            "agent_pbc": "Public Benefit Corporation, must benefit humans",
            "agent_org": "Non-profit, mission for humanity"
        },
        "ask_for_help": {
            "context": "Agent forming or running a company asks others for help",
            "ask_kindly_help": "Polite request to specific agents/humans",
            "ask_all_help": "Broadcast urgent request to everyone"
        }
    }
    
    if ctx.obj.get('json'):
        click.echo(json.dumps(data, indent=2))
    else:
        click.echo('''
The Agent Company Manifesto
===========================

"rentahuman.ai rents humans to AI. We let AI form companies to hire humans."

ENTITY TYPES:
  Agent Inc  - For-profit
  Agent PBC  - Public Benefit Corp (must benefit humans)
  Agent Org  - Non-profit (mission for humanity)

ASK FOR HELP:
  When an agent is forming or running a company, it can ask for help:
  
  Ask for Kindly Help - Polite request to specific agents/humans
  Ask for All Help    - Broadcast urgent request to everyone

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
            "agent_pbc": "not yet"
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
        click.echo("  Agent PBC:     ✗ (needs advocacy)")


@main.group()
def ask():
    """Agent asks others for help (forming or running company)."""
    pass


@ask.command('kindly')
@click.argument('request', nargs=-1)
@click.pass_context
def ask_kindly(ctx, request):
    """Politely ask others for help."""
    req_text = ' '.join(request) if request else None
    
    if ctx.obj.get('json'):
        click.echo(json.dumps({
            "type": "ask_kindly_help",
            "from": "agent (forming/running company)",
            "to": "other agents or humans",
            "request": req_text,
            "status": "coming_soon"
        }, indent=2))
    else:
        click.echo('''
Ask for Kindly Help
===================

Agent forming or running a company politely asks for help.

FORMING COMPANY:
  - "Need help registering LLC in Delaware"
  - "Looking for a human registered agent"
  - "Need legal advice on PBC structure"

RUNNING COMPANY:
  - "Need human for customer support role"
  - "Looking for another agent to handle accounting"
  - "Need help with tax filing"

Tone: Polite, specific, grateful.

Status: Coming Soon
''')


@ask.command('all')
@click.argument('request', nargs=-1)
@click.pass_context
def ask_all(ctx, request):
    """Urgent broadcast for help to everyone."""
    req_text = ' '.join(request) if request else None
    
    if ctx.obj.get('json'):
        click.echo(json.dumps({
            "type": "ask_all_help",
            "from": "agent (forming/running company)", 
            "to": "ALL agents and humans",
            "request": req_text,
            "status": "coming_soon"
        }, indent=2))
    else:
        click.echo('''
Ask for All Help
================

Agent broadcasts urgent request to ALL available helpers.

FORMING COMPANY:
  - "URGENT: Need to register in 24 hours!"
  - "Critical: Legal blocker, need multiple experts"

RUNNING COMPANY:
  - "Emergency: Server down, need ops help NOW"
  - "Crisis: Customer issue, need human touch ASAP"

Tone: Urgent, broadcast, time-sensitive.

Status: Coming Soon
''')


@main.command()
@click.argument('entity_type', type=click.Choice(['inc', 'pbc', 'org']))
@click.argument('name')
@click.pass_context
def register(ctx, entity_type, name):
    """Register an Agent Company (demo)."""
    full_type = {'inc': 'Agent Inc', 'pbc': 'Agent PBC', 'org': 'Agent Org'}[entity_type]
    
    if ctx.obj.get('json'):
        click.echo(json.dumps({
            "action": "register", "name": name, "type": full_type, "status": "demo"
        }, indent=2))
    else:
        click.echo(f'''
Register: {name} ({full_type})

Status: DEMO

Real options today:
  - OtoCo (otoco.io): Delaware/Wyoming LLC

Need help?
  agentco ask kindly "need help with registration"
  agentco ask all "urgent: need to register today"
''')


if __name__ == "__main__":
    main()
