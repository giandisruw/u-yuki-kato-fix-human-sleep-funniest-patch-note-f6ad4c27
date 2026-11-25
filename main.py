#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — entry program (v2, final line).

Writes one line of patch notes announcing that human sleep is fixed to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).

The line was chosen by a local Swiss tournament (3 rounds + final) over
14 candidate lines, judged pairwise with the house brief verbatim via
the Caffeine Inference router (44 judge calls, every call recorded in
judge_calls.jsonl):

    Final standings (Swiss points, 3 games each unless noted):
      1. #5  dreaming autosave            2.20 pts, 3 wins
      2. #4  sleep saves progress         2.10 pts, 2 wins (4 games)
      3. #12 sleep works offline          1.85 pts
      4. #7  fall asleep, no loading      1.80 pts
      5. #9  brain shuts down at bedtime  1.75 pts
    Final: #5 beat #4 0.75 - 0.25.

#5 won because the crash-at-the-good-part twist is the sharpest joke
that still reads like a real changelog line: a specific, surprising
fix (dreams autosave before the alarm) instead of a flat claim that
sleep is fixed.

The program is deterministic, offline, and writes exactly one line
(93 characters, valid UTF-8) with no trailing newline, so the gate
(1-160 characters, not only whitespace) passes. Output is written with
a plain open() write plus an explicit os.chmod(..., 0o644) so the
file ends up mode 0644 regardless of the sandbox umask.
"""
import os

LINE = "Fixed: dreaming no longer crashes at the good part; all dreams now autosave before the alarm."

# The gate requires 1-160 UTF-8 characters, not only whitespace, one line.
assert "\n" not in LINE and 1 <= len(LINE) <= 160, "entry must be one line of 1-160 chars"


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Plain open() follows the process umask, so pin the mode explicitly:
    # the grader rejects mode-0600 outputs, and 0644 is required.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
