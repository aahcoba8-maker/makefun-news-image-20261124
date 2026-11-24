# The World Today — News Image, 24 November 2026

[![Competition](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/aahcoba8-maker/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/aahcoba8-maker/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Entry for the make.fun bounty
[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124).

`main.py` is a self-contained Python program that draws a newspaper-style
poster — "THE WORLD TODAY", dated 24 November 2026 — and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.png` (falling back to the script directory).
It runs offline, is fully deterministic, and needs no input. It renders
with PIL when available; otherwise it copies `poster.png`, the same poster
rendered ahead of time, so the output is identical either way.

## The day's headlines on the poster

- **Markets (lead):** Jensen Huang is reinstated as Nvidia's chief
  executive 11 days after resigning; Nvidia shares leap 31%, the Nasdaq
  jumps 6.5% and the S&P 500 climbs 4.7%.
- **Ukraine war / diplomacy:** Zelenskyy readies four-way peace talks
  with the US, Europe and Russia as Brussels and Washington clash over
  whether a ceasefire must come before a security deal.
- **Climate:** COP31 in Antalya collapses with no deal after oil states
  block any mention of fossil fuels — the longest COP ever and the first
  collapse since Copenhagen in 2009.
- **Americas:** The US designates Venezuela's Cartel de los Soles a
  foreign terrorist organisation, raising pressure on President Maduro.
- **Asia:** A fire at a candy factory in Banten, Indonesia, kills at
  least 24 workers; rescuers search for the missing.
- **Sport:** Max Verstappen wins the Las Vegas Grand Prix; Carlos
  Alcaraz claims his first ATP Finals crown in Turin.

## Sources (reporting of 23–24 November 2026)

- Reuters, "Trading Day: Market euphoria as Huang returns to Nvidia" —
  https://www.reuters.com/commentary/reuters-open-interest/global-markets-trading-day-graphic-2026-11-23/
- Azernews, "Ukraine preparing four-way talks with US, EU, and Russia" —
  https://www.azernews.az/region/267966.html
- Brussels Reporter, "EU and US Clash Over Timing of Ukraine Peace
  Talks" — https://brusselsreporter.com/europe/2026/von-der-leyen-and-kushner/
- CNN, "Global climate summit collapses as countries fail to agree on
  moving away from fossil fuels" (COP31, Antalya)
- CBC World Report, 24 November (Cartel de los Soles designation;
  Ukraine peace plan) —
  https://podscripts.co/podcasts/world-report/november-24-mondays-top-stories-in-10-minutes
- Times of India / Education Times, school assembly headlines for
  24 November 2026 (Banten factory fire; Verstappen in Las Vegas) —
  https://www.educationtimes.com/news/school-assembly-news-headlines-for-24-november-2026-top-indian-international-sports-and-business-news/articleshow/136100381.cms

## Run it

```sh
python3 main.py            # writes ./entry.png
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Output: a 1024×1024 PNG, about 146 KB — inside the contest limits of
1024×1024 pixels and 1 MiB.
