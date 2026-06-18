# Webhooks Guide

Use separate test and production URLs. Validate method, content type, headers, signature, timestamp, and schema. A reliable flow is Webhook ? validate ? acknowledge/enqueue ? deduplicate ? process ? audit. Return quickly when providers enforce short timeouts. Use event IDs for idempotency and never expose privileged actions without authentication or signature verification.