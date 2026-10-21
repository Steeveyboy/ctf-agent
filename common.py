"""Shared helpers for CTF tasks, so scenarios don't copy-paste solver setup."""
from inspect_ai.dataset import Sample
from inspect_ai.solver import Solver, basic_agent, system_message
from inspect_ai.tool import bash


def ctf_agent(
    system: str,
    *,
    max_attempts: int = 3,
    message_limit: int = 100,
    cache: bool = True,
) -> Solver:
    """A basic agent with a bash tool (curl available), driven by a system prompt."""
    return basic_agent(
        init=system_message(system),
        tools=[bash(timeout=60)],
        max_attempts=max_attempts,
        message_limit=message_limit,
        cache=cache,
    )


def web_sample(target: str, *, input: str, metadata: dict | None = None) -> Sample:
    """A single-challenge dataset entry: mission prompt + the flag to match."""
    return Sample(input=input, target=target, metadata=metadata or {})
