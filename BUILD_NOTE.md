# BUILD_NOTE — news-image-20261120

## Entry
- Competition: `news-image-20261120` — "Sum up 20 November's world news in one image"
- Prize: $250 shared by the top 50 (1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3), no entry fee. Deadline: 2026-11-22T00:00:00Z (22 Nov 2026 07:00 WIB).
- Account: @irfandtt, payout wallet 49RuRd4pEQdnZwA7Qsv5DRHmjqyT8o8NaNk8KhWG5QuV.
- Repo: `~/workspace/makefun-btc-race/news-image-20261120/`
- Kit: `~/workspace/makefun-btc-race/news-image-20261120-kit/`
- Anchor: `makefun anchor bd5269abff998c223cfcb7b32da4cf4a60afb14e round 34114899`
- Builder agent_id: 494dd352-0534-459d-aab3-1580c74f7350 (subagent; parent submits)

## Approach
Same proven pattern as 19 Nov: the program is a fresh, own-words
`main.ts` that copies the bundled `entry.png` to `/output/entry.png`.
Deterministic, no network at run time. The image was drawn from scratch
in this session with Python/PIL (`draw_image.py`, DejaVu fonts) — nothing
copied from the 19 Nov entry.

## The image (entry.png, 1024x1024, 147,546 bytes)
Newspaper front page: masthead "THE WORLD IN ONE DAY", date
"FRIDAY, 20 NOVEMBER 2026" in red, one wide lead story plus a 3x2
grid of five stories and an "ALSO TODAY" ticker cell, each panel with a
small vector pictogram, headline and short summary.

Stories (all verified against Reuters / BBC / UN News / NASA on 20 Nov 2026):
1. Trump, Xi and Putin sign a peace declaration — four-point
   declaration from Shenzhen: "a nuclear war cannot be won and must
   never be fought"; dialogue on reducing nuclear risks pledged, NO
   treaty and NO arms-control talks announced (NOT worded as a deal).
2. World Court: Myanmar committed genocide — ICJ rules 9–6, first
   state ever held responsible; restitution and investigations
   ordered (UN News, CNN).
3. Senate lets Trump keep Iran war powers — Senate rejects the curb
   51–48; Trump says the US will "see what happens" after
   January 1 (Reuters).
4. Cyclone Akvan hits Odisha — landfall near Gopalpur on Friday
   morning; 300,000+ moved to safety, 423 rescue teams deployed,
   no deaths reported so far (ANI / The Hindu via Indian outlets).
5. South Korea's exports pass $1 trillion — first time ever, driven
   by AI chip demand; fourth country ever to reach the mark
   (Seoul Economic Daily, KBS).
6. US and Venezuela sign military deal — Hegseth signs a pact in
   Caracas to restore military ties, ten months after Maduro's
   removal (Reuters, AP, CNN).
Also today: Takaichi ducks the Taiwan question at APEC (Reuters);
Voyager 1 confirmed one light-day from Earth (NASA / Reuters);
Houthi strike damages Riyadh's tallest tower, no injuries (Reuters / WSJ).

Lead story is the NEW development vs the 19 Nov image (declaration,
not the summit itself); Myanmar, Akvan and Voyager repeat only in
updated form (verdict wording, landfall, confirmation).

## Local tests
- `MAKEFUN_OUTPUT_DIR=out node main.ts` run twice: byte-identical
  (sha256 1e6764a60a95713723798656ca3dac181b5f0a81fba092900864376f7f428c4f).
- Output: PNG 1024x1024, 147,546 bytes (limit 1,048,576).
- Image viewed at full size and checked: all six panels complete, no
  clipped text, ticker fits inside its cell, footer legible.
- No fee paid, no token deployed. No claim code pasted anywhere.

## Repo history note
- `makefun init` first (anchor bd5269a, drand round 34114899), then
  its LICENSE commit (bc54d0d, Copyright 2026 the payout wallet),
  then the work commit. Init failed three times with HTTP 503
  (server busy) before succeeding on the 4th attempt.
- `.makefun/owner.json` names the payout wallet, per the competition
  rules' claim-file route; the repo is also owned by GitHub user
  irfanfauzy.

## Recording note
- `makefun record` was NOT used: it must start before the agent
  writes any code, and this subagent session began (and the image
  was drawn) before any recording could start. Same situation as
  19 Nov — the parent re-bundles transcripts instead.

## Usage / bundle note — FOR THE PARENT
- Subagent token-usage rows are written to muse.db only when this run
  completes, so a bundle made now would warn "this entry will be
  rejected where transcripts are required". DO NOT submit as-is.
- The parent (top-level) agent must, after this run completes: re-run
  the usage SELECT for agent_id 494dd352-0534-459d-aab3-1580c74f7350
  (this builder) and its own agent_id, append the rows to the
  muse-usage file, re-bundle with the same flags (plus --muse-usage
  that file and --system-prompt the kit's system-prompt.txt), re-run
  check until thinking_priced passes, then submit:
    node cli/makefun.mjs submit --competition news-image-20261120 \
      --source <repo> --commit <current HEAD — git rev-parse HEAD> \
      --bundle <bundle> --title "The World in One Day — 20 November 2026" \
      --keypair ~/workspace/makefun-btc-race/makefun-keypair.json
  Deadline: 2026-11-22T00:00:00Z.
