# The World in One Day — 18 November 2026

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/arwin0204/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/arwin0204/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

A one-image newspaper front page summing up 18 November 2026's world news:
Trump lands in Manila for Quad talks, Nvidia revenue doubles to $115.8bn,
drone attacks target Kuwait and Bahrain, the Board of Peace warns the Gaza
truce may collapse — plus Dhoni retiring from the IPL, Cyclone Akvan over the
Bay of Bengal, and DR Congo peace efforts failing to halt violence in the east.

The page is drawn programmatically (Python + PIL): crisp vector-style art and
sharp text, no AI-image generation, so every headline stays legible. Every
story was checked against live news reporting before the image was rendered.

## How it runs

`main.py` copies the pre-rendered `entry.png` (1024x1024) into
`$MAKEFUN_OUTPUT_DIR`. Standard library only, no network. Running it twice
produces byte-identical output.

Entry for the [make.fun bounty](https://make.fun/bounty/news-image-20261118).
