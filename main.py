"""Run the blind vs. informed agents side by side in one parallel eval.

    python main.py           # uses the model from the INSPECT_EVAL_MODEL env var
    python main.py           # or edit model= below

Then: inspect view   (both appear together for comparison)
"""
from inspect_ai import eval

from ctf_task_v2 import ctf

if __name__ == "__main__":
    eval(
        [ctf(hint=False), ctf(hint=True)],
        model="openai/gpt-4o",
    )
