# How to Import n8n Workflows

1. Download JSON from `examples/`.
2. Choose **Workflows ? Import from File** in n8n.
3. Replace every `YOUR_*` placeholder.
4. Select credentials from the credential picker.
5. Verify webhook paths, callbacks, time zones, mappings, and API versions.
6. Execute one node at a time with sanitized data.
7. Add failure handling and save while inactive.
8. Activate after an end-to-end test.

Review exports before committing; they may contain URLs, email addresses, expressions, IDs, or execution samples.