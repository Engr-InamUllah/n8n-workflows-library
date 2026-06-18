from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=["## Business use case","## Tools/apps used","## Trigger type","## Step-by-step node logic","## Required credentials","## Input example","## Output example","## Error handling","## Security notes","## Possible improvements"]
errors=[]
workflow_files=sorted((ROOT/"workflows").glob("*/*.md"))
if len(workflow_files)<100:errors.append(f"expected at least 100 workflows, found {len(workflow_files)}")
ids=[]
for path in workflow_files:
 if not re.fullmatch(r"\d{3}-[a-z0-9-]+\.md",path.name):errors.append(f"bad filename: {path.relative_to(ROOT)}")
 text=path.read_text(encoding="utf-8")
 ids.append(path.name[:3])
 for heading in REQUIRED:
  if heading not in text:errors.append(f"{path.name}: missing {heading}")
if len(ids)!=len(set(ids)):errors.append("duplicate workflow IDs")
for path in sorted((ROOT/"examples").glob("*.json")) + sorted((ROOT/"templates").glob("*.json")):
 try:
  data=json.loads(path.read_text(encoding="utf-8"))
  if "nodes" not in data or "connections" not in data:errors.append(f"{path.name}: not an n8n workflow shape")
 except Exception as exc:errors.append(f"{path.name}: invalid JSON: {exc}")
if errors:
 print("\n".join(errors));sys.exit(1)
print(f"Validated {len(workflow_files)} workflow documents and JSON examples.")