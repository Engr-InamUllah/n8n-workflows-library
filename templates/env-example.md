# Environment Placeholder Reference

Do not commit a populated `.env` file.

```dotenv
N8N_HOST=YOUR_N8N_HOST
N8N_PROTOCOL=https
N8N_ENCRYPTION_KEY=GENERATE_A_LONG_RANDOM_VALUE
OPENAI_API_KEY=YOUR_API_KEY
SLACK_WEBHOOK_URL=YOUR_WEBHOOK_URL
GOOGLE_SHEET_ID=YOUR_GOOGLE_SHEET_ID
DATABASE_URL=YOUR_DATABASE_URL
```

Prefer supported n8n credential types over environment variables for integration secrets.