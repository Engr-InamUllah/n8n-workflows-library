# 067 ? Google Sheets Duplicate Row Cleanup

## Business use case

Automate **Google Sheets Duplicate Row Cleanup** for a traceable handoff that reduces manual processing and missed follow-up.

## Tools/apps used

- Schedule Trigger
- Google Sheets

## Trigger type

Scheduled

## Step-by-step node logic

1. **Scheduled** ? capture the event and execution metadata.
2. **Validate Input** ? require event ID, source ID, and business-critical fields.
3. **Normalize** ? standardize time zone, text, addresses, and identifiers; compute an idempotency key.
4. **Lookup** ? retrieve destination context and detect an existing record.
5. **Google Sheets Duplicate Row Cleanup** ? perform the core operation through a native node or authenticated HTTP Request.
6. **Route Result** ? separate success, duplicate, invalid, and retryable outcomes.
7. **Audit/Notify** ? write sanitized status and IDs; alert an owner only when intervention is needed.

## Required credentials

- Least-privilege n8n credential for Google Sheets

Use n8n Credentials; never commit secrets in workflow fields or exports.

## Input example

`json
{"event_id":"evt_067","source_id":"SRC-1001","actor":"automation@example.com","occurred_at":"2026-06-18T10:00:00Z"}
`

## Output example

`json
{"status":"processed","workflow_id":"067","destination_id":"DEST-2001","duplicate":false}
`

## Error handling

- Reject malformed input before side effects and quarantine invalid items.
- Retry rate limits and temporary provider failures with capped backoff.
- Stop on authentication, permission, and permanent validation errors.
- Send execution ID and sanitized category to a centralized Error Trigger workflow.
- Check idempotency state before replaying.

## Security notes

- Use least-privilege scopes and separate development/production credentials.
- Verify signed webhooks and restrict public endpoint methods and payload size.
- Avoid posting personal, message, document, or token content into shared alerts.
- Review retention, sharing permissions, API limits, and regional processing.

## Possible improvements

- Add approval for external publishing or destructive changes.
- Add pagination, batching, caching, and rate-limit telemetry.
- Add SLA, latency, success-rate, and last-success dashboards.
- Extract common validation, notification, and audit nodes into sub-workflows.