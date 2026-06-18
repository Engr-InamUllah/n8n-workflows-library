# 045 ? AI Product Description Generator

## Business use case

Use **AI Product Description Generator** to remove repetitive work, shorten cycle time, and produce an auditable result for the owning team.

## Tools/apps used

- Airtable
- OpenAI
- Shopify

## Trigger type

Airtable record event

## Step-by-step node logic

1. **Airtable record event** ? receive the source event and stamp the execution time.
2. **Validate** ? require event ID, source record ID, and operation-specific fields.
3. **Normalize** ? standardize timestamps, text, identifiers, and create an idempotency key.
4. **Enrich/Transform** ? retrieve required context and map it into a stable internal object.
5. **AI Product Description Generator** ? execute the primary action using native n8n nodes or an authenticated HTTP Request.
6. **Route** ? separate processed, duplicate, rejected, and retryable outcomes with IF/Switch nodes.
7. **Audit** ? save the execution ID, source/destination IDs, status, duration, and sanitized error category.

## Required credentials

- Least-privilege n8n credential for Airtable
- Least-privilege n8n credential for OpenAI
- Least-privilege n8n credential for Shopify

Use n8n Credentials; never embed a secret in workflow JSON or expressions.

## Input example

`json
{"event_id":"evt_045","record_id":"REC-1001","email":"user@example.com","occurred_at":"2026-06-18T10:00:00Z"}
`

## Output example

`json
{"status":"processed","workflow_id":"045","destination_id":"DEST-2001","processed_at":"2026-06-18T10:00:04Z"}
`

## Error handling

- Fail fast on invalid input and quarantine rejected records.
- Retry 429/temporary 5xx responses with capped exponential backoff and jitter.
- Treat authentication, authorization, and schema errors as non-retryable.
- Alert through an Error Trigger workflow using execution IDs, not full sensitive payloads.
- Check the idempotency key before replay.

## Security notes

- Apply least privilege, separate environments, and provider-supported OAuth where possible.
- Verify signatures on public webhooks and minimize retained personal or confidential data.
- Redact prompts, messages, addresses, and tokens from logs and collaboration alerts.
- Review provider data-use, retention, regional processing, and rate-limit policies.

## Possible improvements

- Add human approval for high-impact actions.
- Add batching, pagination, caching, and provider-specific backoff.
- Track success rate, latency, volume, cost, and last-success time.
- Move common validation and audit logic into versioned sub-workflows.