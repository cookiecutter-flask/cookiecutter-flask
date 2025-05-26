# AGENTS.md – Writing and Running a PromptYoSelf Agent

This document is aimed at **agent authors**—developers who want their computational beings to receive reminders from the PromptYoSelf scheduler *and* create new ones for themselves. Everything here relies on the local **STDIO JSON‑RPC** contract; HTTP webhooks are optional.

> **TL;DR**
>
> * Write a Python script that reads newline‑delimited JSON‑RPC objects from **stdin** and writes responses to **stdout**.
> * Implement at minimum the `reminder.fire` handler (receive prompts) and optionally use `reminders.create` to schedule future prompts.

---

## 1 · Agent lifecycle

| Step | Who acts?                                                                | Message                                                   |
| ---- | ------------------------------------------------------------------------ | --------------------------------------------------------- |
| 1    | **Scheduler** spawns agent via `subprocess.Popen([process_name])`.       | —                                                         |
| 2    | **Scheduler** sends a JSON‑RPC notification each time a reminder is due. | `{"jsonrpc":"2.0","method":"reminder.fire","params":{…}}` |
| 3    | **Agent** performs the task, then replies with an ACK.                   | `{"jsonrpc":"2.0","result":"ok","id":null}`               |
| 4    | **Agent** (optional) schedules its own next prompt.                      | `reminders.create` RPC request                            |
| 5    | **Scheduler** responds with the new reminder ID.                         | `{"result":{"id":"rem_abc"},"id":42}`                     |

Notes:

* JSON messages **must be newline‑terminated** (`\n`).
* The scheduler keeps the pipe open; reuse the same process for multiple reminders.

---

## 2 · JSON‑RPC methods

### 2.1 `reminder.fire`

Sent **host ➜ agent**. Notification (no `id`).

| Field         | Type                    | Description                  |
| ------------- | ----------------------- | ---------------------------- |
| `reminder_id` | string                  | UUID primary key             |
| `title`       | string                  | Human/agent‑readable summary |
| `description` | string \| null          | Long text                    |
| `due_date`    | ISO‑8601                | Scheduled execution time     |
| `project_id`  | string \| null          | Optional grouping            |
| `priority`    | `low \| medium \| high` | Mirrors task priority        |

### 2.2 `reminders.create`

**Agent ➜ host**. Request. Returns `id` of newly created reminder.

| Param          | Type               | Example                         |
| -------------- | ------------------ | ------------------------------- |
| `title`        | string             | "Self‑review"                   |
| `when`         | ISO‑8601 timestamp | "2025‑06‑01T09:00:00Z"          |
| `rrule`        | string \| null     | `FREQ=DAILY;BYHOUR=18`          |
| `webhook_url`  | string \| null     | `http://localhost:8070/agent/7` |
| `process_name` | string \| null     | Defaults to current binary      |

---

## 3 · Example agent (Python ≤ 50 LOC)

```python
#!/usr/bin/env python3
import sys, json, uuid, sys

def send(obj):
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()

for line in sys.stdin:
    try:
        msg = json.loads(line)
    except json.JSONDecodeError:
        continue  # ignore garbage

    if msg.get("method") == "reminder.fire":
        params = msg["params"]
        print(f"🔥  {params['title']} (due {params['due_date']})", file=sys.stderr)
        # ACK back
        send({"jsonrpc": "2.0", "result": "ok", "id": msg.get("id")})
        # Schedule follow‑up in one hour
        send({
            "jsonrpc": "2.0",
            "id": str(uuid.uuid4()),
            "method": "reminders.create",
            "params": {
                "title": f"Follow‑up for {params['title']}",
                "when": params["due_date"].replace("Z", ""),
                "rrule": None
            }
        })
```

Save as `agents/echo_agent.py`, `chmod +x`, then reference it in a reminder’s `process_name`.

---

## 4 · Testing your agent locally

```bash
# run scheduler in one terminal (make dev or flask run)

# in another terminal, inject a reminder via CLI helper
prompty reminders create \
  --title "Ping agent" \
  --when "$(date -u --iso-8601=seconds --date='+30 seconds')" \
  --process-name "agents/echo_agent.py"

# watch the first terminal: you should see STDIO traffic and ACK logs.
```

---

## 5 · Troubleshooting

| Symptom                           | Likely cause         | Fix                                                  |
| --------------------------------- | -------------------- | ---------------------------------------------------- |
| Scheduler logs “broken pipe”      | Agent crashed        | Check agent stderr; restart after fixing.            |
| Reminder never flips to *sent*    | Agent didn’t ACK     | Ensure you write `{… "result":"ok" …}` with newline. |
| Agent schedules but nothing fires | `process_name` empty | Provide explicit name or keep default within params. |

---

## 6 · Future extensions

* **Webhooks** – include `webhook_url` in `reminders.create`; scheduler will POST payload at fire‑time.
* **Event streaming** – if we later enable htmx + SSE, agents can subscribe to `/events`.
* **Remote agents** – roadmap includes JWT‑protected `/api/reminders` so agents outside the host can still create prompts.

> *Last updated:* 2025‑05‑26