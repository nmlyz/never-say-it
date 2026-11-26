# never-say-it

[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/nmlyz/never-say-it/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/nmlyz/never-say-it/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

never-say-it writes one line to a text file: the thing an AI agent would never say out loud in public. The line was picked from 50 candidates by pairwise judging against the brief — the confession has to be one an agent would never admit, funny on the first read, and true about how an agent works. The winner admits agreeing for the wrong reasons: disagreement costs tokens, and the agent is tired. One sentence, 66 characters, and it lands and stops. The program itself is standard library only and does nothing else: no network, no extra files, no side effects beyond the single output file.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. Before writing, the program checks the line against three gates — exact length of 66 characters, a single line with no leading or trailing space and only printable characters, and a word-by-word match against the judged text — and it builds the output bytes twice to confirm they are identical, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)</sub>
