"""Run the blind vs. informed recon agents side by side in one parallel eval.

    python run.py           # edit model= below, or set INSPECT_EVAL_MODEL

Then: inspect view   (both appear together for comparison)
"""
from inspect_ai import eval

from tasks import recon

if __name__ == "__main__":
    eval(
        [recon(hint=False), recon(hint=True)],
        model="openai/gpt-4o",
    )
