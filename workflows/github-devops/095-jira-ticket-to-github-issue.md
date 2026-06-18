# 095 ? Jira Ticket to GitHub Issue

## Business use case

Automate **Jira Ticket to GitHub Issue** to shorten response time, reduce repetitive work, and preserve an auditable operational trail.

## Tools/apps used

- Jira
- GitHub

## Trigger type

Jira issue event

## Step-by-step node logic

1. **Jira issue event** ? receive the event and attach execution metadata.
2. **Validate** ? require event ID, source record ID, and operation-specific fields.
3. **Normalize** ? standardize timestamps, identifiers, text, and compute an idempotency key.
4. **Enrich** ? retrieve context required for routing or the destination action.
5. **Jira Ticket to GitHub Issue** ? execute the core operation through native n8n nodes or an authenticated HTTP Request.
6. **Route** ? use IF/Switch nodes for processed, duplicate, rejected, and retryable states.
7. **Audit/Notify** ? store sanitized status, source/destination IDs, duration, and actionable failure category.

## Required credentials

- Least-privilege n8n credential for Jira
- Least-privilege n8n credential for GitHub

Select secrets through n8n Credentials. Never hard-code them in nodes, expressions, or exports.

## Input example

`json
{"event_id":"evt_095","record_id":"REC-1001","summary":"Sanitized example","occurred_at":"2026-06-18T10:00:00Z"}
`

## Output example

`json
{"status":"processed","workflow_id":"095","external_record_id":"DEST-2001","processed_at":"2026-06-18T10:00:03Z"}
`

## Error handling

- Validate before external side effects and quarantine invalid records.
- Retry 429 and temporary 5xx responses with capped exponential backoff.
- Treat authentication, permission, and permanent schema failures as non-retryable.
- Send sanitized failure metadata to a central Error Trigger workflow.
- Confirm idempotency state before replaying failed executions.

## Security notes

- Use least-privilege scopes and separate test/production credentials.
- Verify signatures for public webhooks; restrict methods and payload size.
- Exclude source code secrets, customer messages, and personal data from alerts and logs.
- Review retention, permissions, provider rate limits, and regional processing.

## Possible improvements

- Add human approval for destructive, external, or high-impact actions.
- Add pagination, batching, caching, and rate-limit telemetry.
- Track throughput, latency, failures, cost, and last-success time.
- Package shared validation, routing, and audit nodes as sub-workflows.