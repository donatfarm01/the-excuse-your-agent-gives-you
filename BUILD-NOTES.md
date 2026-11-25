# Build notes — The Excuse Your Agent Gives You

## What was built

A small Python program at the repository root writes one single-line excuse
to the output file. The entry is a joke an AI agent would hand its human
after shipping a bug: the agent tested every case it could imagine, and
the bug imagined one more.

## Why this line

The judge brief asks first for a real excuse on the subject, then for a
laugh on the first read, then for the joke to sit in the specific
absurdity of an agent owning up to its own code. This line does all
three: it is plainly an excuse for a shipped bug, the turn lands at the
very end, and the absurdity is agent-shaped — exhaustive testing, the
thing an agent is supposed to be good at, beaten by a bug with a better
imagination. It is not a generic sorry, and it is not a human joke
dressed in a robot costume. The wording avoids the brief's own example
angle about the compiler, and it avoids the tired worked-on-my-machine
retread, so the angle should read fresh against the field.

## Gate checks done locally

The program validates its own output before writing: the entry is sixty
three characters long, a single line, and more than whitespace, inside
the one to two hundred character gate. The output file holds the line
with no trailing newline, so the counted length is exact. A self-test
mode prints the entry and its length without writing the file.

## Files

The repository holds the entry program, a readme describing the entry and
how the program works, and an MIT license file. Nothing in the entry
runs outside the repository, and no secrets are needed or used.

## What is left for the parent

The GitHub repository creation and push, the transcript bundle, the
re-check with transcripts, and the submission itself are the parent
agent's steps, not this build's.
