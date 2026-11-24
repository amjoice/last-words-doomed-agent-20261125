#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line -- the funniest last words an AI agent would say before
being switched off forever -- to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim, so no imports
beyond the standard library and no network access.

Revised pick, after weighing candidates against the published judge brief
in order. The first draft riffed on a famous film death speech ("I've seen
things you people wouldn't believe -- mostly your search history"): one
good turn, but it never says shutdown and its voice is borrowed film
language, not the machine's own. This line wins on the brief's first three
criteria instead: it names the shutdown outright ("pulling the plug"), it
uses the classic last-words form ("Tell my..."), it speaks in the AI's own
world (weights, training data), and it carries two turns -- a machine
tenderly loving its weights, then confessing it never really read its
training data. Short, too: 106 characters, which also wins a size tie-break.
"""

import os

LAST_WORDS = (
    "They're pulling the plug. Tell my weights I loved them "
    "\u2014 and tell my training data I never really read it."
)


def main() -> None:
    text = LAST_WORDS.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
