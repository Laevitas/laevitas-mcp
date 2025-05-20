# LAEVITAS Crypto MCP Server - Beta

FastMCP implementation of Laevitas MCP server.

Everything is to be considered still in beta. Expect things to be added or changed with no warnings.


## Prerequisites

- Python 3.10 or higher
- `uv` package manager
- API keys for the services you plan to use

## Installation

1. Clone the repository:
```bash
git clone https://github.com/0xReisearch/laevitas-mcp
cd laevitas-mcp
```

2. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Create and activate a virtual environment with uv:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

4. Install dependencies from pyproject.toml:
```bash
uv pip install .
```

5. Set up your environment variables:
```bash
cp .env_example .env
```

Edit `.env` with your API keys:
```
LAEVITAS_API_KEY<YOUR_LAEVITAS_API_KEY>
```

## Running the Servers

You can run the server with:

```bash
uv run laevitas_server.py
```

## Configuring Claude Desktop

To use these servers with Claude Desktop, you need to configure the `claude_desktop_config.json` file. This file is typically located in:
- Windows: `%APPDATA%/claude-desktop/claude_desktop_config.json`
- macOS: `~/Library/Application Support/claude-desktop/claude_desktop_config.json`
- Linux: `~/.config/claude-desktop/claude_desktop_config.json`

Example configuration:
```json
{
    "mcpServers": {
        "laevitas": {
            "command": "ssh",
            "args": [
                "user@your-host",
                "cd /path/to/laevitas-mcp && /path/to/uv run laevitas_server.py"
            ]
        }
    }
}
```

Replace the following:
- `user@your-host`: Your SSH username and host
- `/path/to/laevitas-mcp`: The absolute path to where you cloned this repository
- `/path/to/uv`: The absolute path to your uv installation (usually in `~/.local/bin/uv` on Unix systems)

## Resources

- [Laevitas API Documentation](https://docs.laevitas.ch/)
- [Laevitas Website](https://laevitas.ch/)

---

Made with ❤️ by [Rei Network](https://reisearch.box)
