import logging
from pathlib import Path

log = logging.getLogger("rag")

CONFIGS_DIR = Path(__file__).parent.parent / "customer-configs"


def get_configs(client: str, module: str, config_type: str) -> str:
    path = CONFIGS_DIR / client / module / f"{config_type}.json"
    log.info(f"TOOL | Reading: {path}")

    if not path.exists():
        # Help Gemini understand what's available
        available = _list_available(client, module)
        return (
            f"Config not found: {path}\n"
            f"Available for client='{client}', module='{module}': {available}"
        )

    content = path.read_text(encoding="utf-8")
    log.info(f"TOOL | Found {len(content)} chars")
    return content


def _list_available(client: str = None, module: str = None) -> str:
    if not CONFIGS_DIR.exists():
        return "customer-configs directory not found"

    if client and module:
        path = CONFIGS_DIR / client / module
        if path.exists():
            files = [f.stem for f in path.glob("*.json")]
            return f"files: {files}"
        return f"module '{module}' not found under client '{client}'"

    if client:
        path = CONFIGS_DIR / client
        if path.exists():
            modules = [d.name for d in path.iterdir() if d.is_dir()]
            return f"modules: {modules}"
        return f"client '{client}' not found"

    clients = [d.name for d in CONFIGS_DIR.iterdir() if d.is_dir()]
    return f"clients: {clients}"


def execute_tool(name: str, args: dict) -> str:
    if name == "get_configs":
        return get_configs(**args)
    return f"Unknown tool: {name}"
