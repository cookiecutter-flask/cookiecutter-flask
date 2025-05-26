# Agents Directory

This directory contains local STDIO agent binaries for the PromptYoSelf application.

## Purpose

Agents are standalone executables that can be invoked by the Flask application to perform specific tasks through standard input/output communication.

## Structure

```
agents/
├── README.md           # This file
├── reminder_agent      # Example: Reminder processing agent
├── notification_agent  # Example: Notification delivery agent
└── data_agent         # Example: Data processing agent
```

## Usage

Agents should be designed to:
- Accept JSON input via stdin
- Return JSON output via stdout
- Handle errors gracefully
- Be stateless and idempotent

## Development

When developing new agents:
1. Create executable files in this directory
2. Ensure they follow the STDIO protocol
3. Add appropriate error handling
4. Document their input/output format
5. Add tests in the main test suite

## Security

- Agents should validate all input
- Use appropriate sandboxing if processing untrusted data
- Follow principle of least privilege
