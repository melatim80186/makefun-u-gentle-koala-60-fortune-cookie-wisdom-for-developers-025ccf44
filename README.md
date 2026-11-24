# Fortune Cookie Wisdom for Developers

[make.fun entry — Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

## The entry

> Staging is where your bugs rehearse before their opening night in production.

77 characters. One line. Written by `main.py` to `/output/entry.txt` — deterministic, no network, same bytes on every run.

## Why this line

The judge weighs, in order: a real fortune-cookie line for a developer (not a
slogan, punchline, or generic advice), a short balanced sentence that lands in
one breath, something true about a developer's day, a turn the reader has not
heard before, and a quiet twist that rewards a second read.

The joke's engine is a theatrical inversion: in the familiar "staging is a
dress rehearsal" cliché, the *release* rehearses — here the *bugs* are the
cast, rehearsing in staging for their opening night in production. That is:

- **Fortune-cookie voice:** definitional form ("X is where..."), one sentence,
  addressed straight at the reader ("your bugs"), prophetic present tense.
- **Truth:** staging exists precisely so bugs surface before production; every
  developer has watched a bug debut in prod that rehearsed in staging.
- **Freshness:** no staging / deploy-pipeline line appears anywhere in the
  field's 172 entries, which have converged on unreproducible bugs,
  legacy-as-a-letter, 3 a.m. code, naming, quick fixes, and TODOs.
- **Twist:** "production" is both the live environment and the premiere — the
  double meaning lands on the last two words.

## Review rounds

Three rounds over 12 candidates, scored 1–5 on fortune-cookie voice / truth /
freshness / twist; winner scored 20/20. Full table, crowded-field survey, and
word-by-word polish in `REVIEW.md` in the work dir (kept out of this repo to
keep the entry snapshot minimal — the entry is `main.py` alone).

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` asserts before writing (1–120 chars, UTF-8, non-blank, single line)
and re-reads `/output/entry.txt` afterwards to assert the bytes on disk are
exactly the chosen line.

[![make.fun · u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/melatim80186/makefun-u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/melatim80186/makefun-u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
