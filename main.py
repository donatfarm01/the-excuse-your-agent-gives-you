"""The Excuse Your Agent Gives You.

Writes one single-line excuse to /output/entry.txt: the excuse an AI
agent hands its human after shipping a bug.

The line: the agent tested every case it could imagine, and the bug
imagined one more. The joke is the specific absurdity of an agent
owning up to its own code — exhaustive testing beaten by a bug with
a better imagination — and it lands in one line with the turn at the
end, in the agent's own flat voice.
"""

import os
import sys

ENTRY = "I tested every case I could imagine. The bug imagined one more."


def validate(text: str) -> str:
    if not text or text.strip() == "":
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 gate")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    return text


def main() -> None:
    if "--check" in sys.argv:
        entry = validate(ENTRY)
        print(f"self-test ok: {entry} ({len(entry)} chars, 1 line)")
        return
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
