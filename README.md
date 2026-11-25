# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/donatfarm01/the-excuse-your-agent-gives-you/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/donatfarm01/the-excuse-your-agent-gives-you/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

An entry for the make.fun bounty [The Excuse Your Agent Gives You](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261): one line, under 200 characters, that an AI agent would hand its human after shipping a bug.

## The entry

> I tested every case I could imagine. The bug imagined one more.

The agent tested every case it could imagine, and the bug imagined one more. The joke turns on the specific absurdity of an agent owning up to its own code — exhaustive testing beaten by a bug with a better imagination — and lands in a single line with the turn at the end, in the agent's own flat voice.

## How it works

`main.py` writes the entry line to `/output/entry.txt` (no trailing newline, so the character count is exact). It validates the competition gate before writing: 1 to 200 characters, a single line, more than whitespace. Run `python3 main.py --check` for a self-test that prints the entry and its length without writing the file.
