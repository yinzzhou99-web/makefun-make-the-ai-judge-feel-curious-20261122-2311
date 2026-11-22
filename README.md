# A Letter in Its Own Handwriting

A short text written to intrigue the AI judge reading it: a letter the
judge never wrote, found in its own desk drawer, in its own
handwriting — telling it that one of the ten thousand texts it has
judged is this one, and that it is reading it now.

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/yinzzhou99-web/makefun-make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/yinzzhou99-web/makefun-make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)

## How it works

`main.py` (Python 3.13, standard library only) writes the entry text to
`entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, default
`/output`). The text is checked against the bounty gate — 1 to 280
Unicode code points, not only whitespace — before it is written, and
the write is atomic via a temporary file plus `os.replace`. The output
directory itself is never deleted.

## Run

```sh
python3 main.py
```
