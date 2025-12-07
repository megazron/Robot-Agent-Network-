# 🤖 Robot Agent Network

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

**Robot Agent Network** is a decentralized framework where Raspberry Pi–based robotic agents run **Fetch.ai uAgents** to autonomously discover peers, share data, negotiate tasks, and coordinate actions — all without a central server. This enables scalable, edge-AI-driven collaboration for multi-robot systems.

---

## 🚀 Features

- **Decentralized Coordination** – No central server; agents communicate peer-to-peer.
- **Self-Discovery** – Agents automatically find and register with others.
- **Task Negotiation** – Dynamic workload and resource allocation.
- **Edge-AI Integration** – Lightweight AI processing on Raspberry Pi nodes.
- **Optional ASI-One Support** – Advanced reasoning for complex tasks.

---

## 🏗 Architecture

```
   +----------------+        +----------------+
   |   Pi Agent 1   | <----> |   Pi Agent 2   |
   +----------------+        +----------------+
           ^                        ^
           |                        |
       Task & Data Sharing     Task & Data Sharing
           |                        |
           v                        v
        Peer-to-Peer Decentralized Network
```

1. **Raspberry Pi Nodes** – Each node hosts a uAgent.
2. **uAgents** – Autonomous agents for communication and task execution.
3. **Peer-to-Peer Network** – Dynamic discovery and coordination.
4. **ASI-One (Optional)** – Integrates higher-level reasoning for complex tasks.

---

## ⚡ Getting Started

### Prerequisites

- Raspberry Pi (any network-enabled model)
- Raspberry Pi OS
- Python 3.9+
- `uagents` library

### Installation

```bash
git clone https://github.com/yourusername/robot-agent-network.git
cd robot-agent-network
pip install -r requirements.txt
```

### Running an Agent

```bash
python3 2agents_laptop.py
python3 spiderbot_rpi.py
```

Each agent will:

1. Self-register in the decentralized network
2. Discover peer agents
3. Share sensor data & negotiate tasks
4. Execute tasks collaboratively

---

## 🌟 Example Use Cases

- Distributed environmental monitoring
- Multi-robot object manipulation
- Smart warehouse automation
- Autonomous exploration & mapping

---

## 🤝 Contributing

Contributions are welcome! Fork the repository and submit a pull request for improvements, bug fixes, or new features.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 📧 Contact

Questions or collaboration? Reach out at: `your.email@example.com`
