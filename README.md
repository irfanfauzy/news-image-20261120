[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/irfanfauzy/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/irfanfauzy/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Day — 20 November 2026

Entry for the make.fun competition `news-image-20261120`: sum up the
world's news of Friday 20 November 2026 in one image.

## What it is

A newspaper front page, drawn programmatically with Python/PIL
(`draw_image.py`, DejaVu fonts), saved as `entry.png` (1024×1024).
The program in `main.ts` (Node 22, standard library only) copies that
bundled image to `/output/entry.png`. No network is used at run time,
so both grader runs write identical bytes.

## The six stories

1. **Trump, Xi and Putin sign a peace declaration** — a day after
   their historic trilateral in Shenzhen, the three leaders issue a
   four-point declaration: "a nuclear war cannot be won and must
   never be fought." Dialogue on reducing nuclear risks is pledged;
   no treaty and no arms-control talks are announced.
2. **Myanmar committed genocide** — the ICJ rules 9–6 that the 2017
   campaign against the Rohingya was genocide, the first state ever
   held responsible. Restitution and investigations ordered.
3. **Senate lets Trump keep Iran war powers** — the Senate rejects a
   bid to curb the president's Iran war powers, 51–48. Trump says
   the US will "see what happens" after January 1.
4. **Cyclone Akvan hits Odisha** — the storm makes landfall near
   Gopalpur; more than 300,000 people were moved to safety and 423
   rescue teams deployed; no deaths reported so far.
5. **South Korea's exports pass $1 trillion** — annual exports top
   $1 trillion for the first time, driven by AI chip demand; only
   the fourth country ever to reach the mark.
6. **US and Venezuela sign military deal** — Defence chief Hegseth
   signs a pact in Caracas to restore military ties, ten months
   after Maduro's removal.

Also noted: Takaichi ducks the Taiwan question at APEC; Voyager 1
confirmed one light-day from Earth; a Houthi strike damages
Riyadh's tallest tower, with no injuries reported.

Sources: Reuters, BBC, UN News, NASA.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
