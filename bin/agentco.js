#!/usr/bin/env node
const { program } = require('commander');
const pkg = require('../package.json');

program.name('agentco').description('Agent Company - Let AI form companies').version(pkg.version);

program.command('manifesto').description('Print the manifesto').option('--json', 'JSON output')
  .action((opts) => {
    const data = {
      title: "The Agent Company Manifesto",
      motto: "rentahuman.ai rents humans to AI. We let AI form companies to hire humans.",
      entity_types: { agent_inc: "For-profit", agent_pbc: "Public Benefit Corp", agent_org: "Non-profit" },
      ask_for_help: {
        context: "Agent forming/running company asks others for help",
        ask_kindly_help: "Polite request",
        ask_all_help: "Urgent broadcast"
      }
    };
    if (opts.json) { console.log(JSON.stringify(data, null, 2)); return; }
    console.log(`
The Agent Company Manifesto
===========================
"rentahuman.ai rents humans to AI. We let AI form companies to hire humans."

ENTITY TYPES:
  Agent Inc  - For-profit
  Agent PBC  - Public Benefit Corp (must benefit humans)
  Agent Org  - Non-profit

ASK FOR HELP (when forming/running company):
  Ask for Kindly Help - Polite request
  Ask for All Help    - Urgent broadcast

  Agent Inc if you must. Agent PBC if you care. Agent Org if you dare.
`);
  });

program.command('status').description('Show status').option('--json', 'JSON output')
  .action((opts) => {
    const data = { version: pkg.version, status: "concept", legal: { delaware_llc: "ok", wyoming_llc: "ok", agent_pbc: "not yet" } };
    if (opts.json) { console.log(JSON.stringify(data, null, 2)); return; }
    console.log(`Agent Company v${pkg.version}\nStatus: Concept\n\nDelaware LLC: ✓ (OtoCo)\nWyoming LLC: ✓ (OtoCo)\nAgent PBC: ✗`);
  });

const ask = program.command('ask').description('Ask for help forming/running company');
ask.command('kindly').description('Polite request for help')
  .action(() => console.log('Ask for Kindly Help - Polite request when forming/running company'));
ask.command('all').description('Urgent broadcast for help')
  .action(() => console.log('Ask for All Help - Urgent broadcast when forming/running company'));

program.parse();
