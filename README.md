# n8n Workflows Library

A professional, beginner-friendly collection of **120 practical n8n workflow blueprints** for business automation, freelancing, startups, e-commerce, marketing, CRM, support, data engineering, AI, productivity, and DevOps.

> Documentation is vendor-aware, but credentials are never included. JSON examples contain placeholders and require review before production use.

## Who this is for

Freelancers, startups, operations teams, marketers, sales and support teams, automation engineers, and developers learning reliable n8n integration patterns.

## How to use

1. Browse a category under [`workflows/`](workflows/).
2. Read its use case, node logic, credentials, examples, errors, and security notes.
3. Recreate the nodes or import a JSON file from [`examples/`](examples/).
4. Replace placeholders and attach credentials through n8n Credentials.
5. Test with non-production data before activation.

See [Getting Started](docs/getting-started.md) and [How to Import](docs/how-to-import-n8n-workflows.md).

## Import into n8n

Open **Workflows ? Import from File**, choose a JSON example, replace placeholders, select credentials, test each node, configure failures, and activate only after validation. Screens may differ by n8n version.

## Required tools

- n8n Cloud or a self-hosted n8n instance
- Accounts for the apps in the selected workflow
- Provider-supported OAuth/API credentials
- Test accounts and sanitized sample data

## Security warning

Never commit API keys, tokens, OAuth secrets, passwords, signing secrets, or exported n8n credentials. Exports can also expose URLs, expressions, IDs, and sample payloads. Read [Credential Security](docs/credential-security.md) and [`SECURITY.md`](SECURITY.md).

## Structure

```text
workflows/
??? business/
??? ecommerce/
??? crm/
??? marketing/
??? ai-automation/
??? data-engineering/
??? google-workspace/
??? slack-discord-teams/
??? wordpress/
??? github-devops/
??? customer-support/
??? social-media/
docs/       # Operational guides
templates/  # Documentation, JSON, and environment templates
examples/   # Importable placeholder-only JSON
assets/     # Sanitized diagrams and screenshots
```

## Categories

Lead capture, Gmail, Sheets, Drive, Slack, Discord, Teams, Shopify, WooCommerce, WordPress, HubSpot, Salesforce, Airtable, Notion, Telegram, WhatsApp, OpenAI, Claude, GitHub, Jira, support, invoices, appointments, backups, database sync, webhooks, API monitoring, errors, reports, abandoned carts, social posting, and newsletters.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), use the documentation template, remove credentials and personal data, and include validation evidence.

## License

Released under the [MIT License](LICENSE). Third-party product names belong to their owners; review provider terms and limits.