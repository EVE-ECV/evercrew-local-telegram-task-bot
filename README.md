# EVE

## The Local AI Operating System for SMEs

**Version:** v0.1.0 Alpha

Built by **Evercrew Venture Pte Ltd**

---

EVE is an open-source, local-first AI workflow platform designed to help small and medium-sized enterprises (SMEs) automate everyday business operations using practical AI and lightweight language models.

Unlike traditional AI chatbots, EVE focuses on structured business workflows where humans remain in control of important decisions.

Run locally.

Keep your data private.

Own your intelligence.

---

## Why EVE?

Most SMEs don't need another chatbot.

They need an AI operating system that helps their business run more efficiently.

EVE is designed around five principles:

- 🔒 Local-first deployment
- 🤝 Human-in-the-loop workflows
- 🧠 Small language model friendly
- 🚀 Easy to deploy
- 🏢 Built for real business operations

Built by **Evercrew Venture Pte Ltd**, Singapore.

---

## Current Workflow

The current release demonstrates an end-to-end AI task delegation workflow.

```text
Boss
   │
   ▼
Telegram Message
   │
   ▼
Local LLM (Ollama)
   │
   ▼
Task Parsing
   │
   ▼
Boss Confirmation
   │
   ▼
Employee Assignment
   │
   ▼
Employee Completes Task
   │
   ▼
Boss Notification
```

---

## Example

### Boss sends

> Ask Ah Tan to prepare the June sales report and send it to me by Friday.

### EVE replies

```
Employee : Ah Tan

Task : Prepare June Sales Report

Deadline : Friday

Priority : Normal

Do you want to assign this task?
```

The boss confirms.

### Employee receives

```
New Task Assigned

Task:
Prepare the June Sales Report

Deadline:
Friday

Priority:
Normal

Please reply DONE when completed.
```

### Employee replies

```
DONE
```

### Boss receives

```
Task Completed

Employee:
Ah Tan

Task:
Prepare the June Sales Report
```

---

## Why Local AI?

Many SMEs prefer to keep internal business instructions and operational workflows on their own infrastructure.

EVE is designed to work with local AI models through Ollama, reducing reliance on external cloud AI services for everyday workflow automation.

Recommended models include:

- llama3.2:1b
- llama3.2:3b
- gemma3:1b
- qwen small models

---

## Current Release

**Version:** v0.1.0 Alpha

### Implemented

- ✅ Local LLM via Ollama
- ✅ Telegram Bot
- ✅ Boss Confirmation Workflow
- ✅ Task Parsing
- ✅ Employee Assignment
- ✅ Employee Completion
- ✅ Workflow Sessions
- ✅ Employee Directory
- ✅ Local-first Architecture

### Planned

- SQLite Storage
- Employee Registration
- Multi-user Support
- Task History
- Dashboard
- Email Integration
- WhatsApp Integration
- Microsoft Teams Integration

---

## Technology Stack

- Python 3.10+
- Ollama
- Python Telegram Bot
- Pydantic
- Local LLM
- JSON Configuration

---

## Documentation

- [Architecture](docs/architecture.md)
- [Installation Guide](docs/installation.md)
- [Roadmap](docs/roadmap.md)
- [Philosophy](docs/philosophy.md)
- [Naming Direction](docs/naming.md)
- [Contributing](CONTRIBUTING.md)

---

## Project Goals

EVE aims to become a practical, local-first AI operating system for SMEs.

The project focuses on:

- Privacy by design
- Human-in-the-loop workflows
- Local AI deployment
- Practical business automation
- Open-source collaboration

The long-term vision is to provide modular AI assistants for common SME operations, including:

- Administration
- Sales
- Customer Service
- Human Resources
- Finance
- Procurement
- Workflow Automation

---

## About Evercrew Venture Pte Ltd

Evercrew Venture Pte Ltd is a Singapore-based AI company focused on helping SMEs deploy practical AI workflow automation, local LLM solutions, AI assistants, and business process automation.

🌐 Website: https://evercrew.ai

---

## License

This project is released under the MIT License.
