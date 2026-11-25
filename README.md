# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/giandisruw/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/giandisruw/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One line of patch notes announcing that human sleep is fixed. Funny
enough to laugh, plausible enough for a real changelog.

## Entry

**Fixed: dreaming no longer crashes at the good part; all dreams now autosave before the alarm.**

93 characters, one line. The crash-at-the-good-part twist is the
sharpest joke that still reads like a real changelog line: a specific,
surprising fix instead of a flat claim that sleep is fixed.

## How to run

```bash
python3 main.py
```

This writes the line to `/output/entry.txt` (or to `$ENTRY_OUTPUT` when
set, for local testing). Deterministic, offline, no network, no secrets.

## How the line was chosen

14 candidate patch-note lines were judged pairwise with the house
brief verbatim, using the Caffeine Inference router as the local judge
(44 judge calls, every call recorded in `judge_calls.jsonl`):

| # | Line (short) | Swiss pts | Games |
|---|---|---|---|
| 5 | dreaming autosave | 2.20 | 3 |
| 4 | sleep saves progress | 2.10 | 4 |
| 12 | sleep works offline | 1.85 | 3 |
| 7 | fall asleep, no loading screen | 1.80 | 3 |
| 9 | brain shuts down at bedtime | 1.75 | 3 |

Final: #5 beat #4 0.75 – 0.25. (Note: the inherited Swiss pairing
script lets a swapped-in candidate play twice in a round, so #4 and
#11 played 4 games and #2 and #13 only 2; the ranking above is the
script's recorded result, and the final was still top-2 vs top-2.)

---

*Built with [make.fun](https://make.fun/?ref=0txwmf1m) — use referral code `0txwmf1m`.*
