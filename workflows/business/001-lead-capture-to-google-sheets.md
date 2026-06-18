# 001 ? Lead Capture to Google Sheets

## Business use case

Automate **Lead Capture to Google Sheets** to reduce manual handoffs, improve response time, and create a traceable operational record. This blueprint is suitable for a small business or can be extended for a production team.

## Tools/apps used

- Webhook
- Google Sheets
- Slack

## Trigger type

Webhook

## Step-by-step node logic

1. **Webhook** ? start the workflow and capture the event with an execution timestamp.
2. **Validate Input** ? require the business identifier, contact or record ID, and fields needed by downstream nodes.
3. **Normalize Data** ? map dates to ISO 8601, trim text, standardize email/phone fields, and create an idempotency key.
4. **Lookup Existing Record** ? search the destination before creating data to prevent duplicates.
5. **Execute Lead Capture to Google Sheets** ? perform the primary operation through the relevant n8n app node or an authenticated HTTP Request node.
6. **Route Result** ? use IF/Switch nodes for success, rejected input, duplicate, and retryable provider responses.
7. **Audit and Notify** ? record status, external record ID, execution ID, and a sanitized summary; notify an owner only when action is required.

## Required credentials

- A least-privilege n8n credential for Google Sheets, when the selected operation requires authentication
- A least-privilege n8n credential for Slack, when the selected operation requires authentication

Never place a token directly in a Set, Code, or HTTP Request field. Select an n8n credential object.

## Input example

`json
{
  "event_id": "evt_",
  "workflow": "lead-capture-to-google-sheets",
  "contact_email": "customer@example.com",
  "record_id": "REC-1001",
  "occurred_at": "2026-06-18T10:00:00Z"
}
`

## Output example

`json
{
  "status": "processed",
  "workflow_id": "001",
  "external_record_id": "DEST-2001",
  "duplicate": false,
  "processed_at": "2026-06-18T10:00:03Z"
}
`

## Error handling

- Reject missing or malformed fields before external calls.
- Retry HTTP 429 and temporary 5xx responses with capped exponential backoff.
- Do not retry authentication, permission, or validation failures indefinitely.
- Send failed items to a quarantine table or error workflow with the execution ID and sanitized context.
- Use the event ID as an idempotency key before replaying an execution.

## Security notes

- Use least-privilege OAuth scopes or API tokens and separate test from production credentials.
- Verify webhook signatures when supported and restrict public webhook methods and payload size.
- Minimize stored personal data; redact message bodies and customer details from alerts and logs.
- Review provider retention, regional processing, and rate-limit requirements.

## Possible improvements

- Add approval for high-value or destructive actions.
- Add SLA metrics, latency dashboards, and last-success monitoring.
- Extract validation and audit logic into reusable sub-workflows.
- Add provider-specific pagination, batching, and dead-letter replay.