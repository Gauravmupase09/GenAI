from typing import Dict, List

# super-simple in-memory store: { session_id: [ {role, content}, ... ] }
_sessions: Dict[str, List[Dict[str, str]]] = {}

SYSTEM_PROMPT = (
    "You are a helpful assistant. Be concise, friendly, and keep context from the conversation."
)

MAX_TURNS = 10  # keep last 10 user/assistant exchanges (+ system)

def start_session(session_id: str) -> List[Dict[str, str]]:
    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    _sessions[session_id] = history
    return history

def get_history(session_id: str) -> List[Dict[str, str]]:
    return _sessions.get(session_id, [])

def save_history(session_id: str, history: List[Dict[str, str]]) -> None:
    _sessions[session_id] = history

def trim_history(history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    if not history:
        return history
    system = history[0] if history[0].get("role") == "system" else None
    rest = history[1:] if system else history
    # keep last 2*MAX_TURNS messages (user+assistant per turn)
    rest = rest[-2 * MAX_TURNS :]
    return [system] + rest if system else rest
