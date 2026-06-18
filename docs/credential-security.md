# Credential Security

- Store secrets in n8n Credentials or an approved secret store.
- Prefer OAuth, scoped service accounts, short-lived tokens, and least privilege.
- Never put secrets in Set nodes, Code nodes, URLs, examples, logs, or Git history.
- Separate development and production credentials.
- Verify webhook signatures when supported.
- Restrict webhook methods, payload size, origins, and networks where practical.
- Redact personal/payment data before logging or AI processing.
- Rotate exposed credentials and review execution history.
- Reduce saved execution data when requirements permit.

`YOUR_API_KEY` is a marker, not a usable credential.