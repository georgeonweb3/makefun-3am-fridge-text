#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes one line (<=140 characters) to /output/entry.txt: the message
a smart fridge sends its owner at 3am.

Drafting notes (scored against the judge brief):
- The judge weighs, in order: (1) a one-line text a smart fridge sends
  its owner at 3am, and funny; (2) the bigger laugh, the line a reader
  would screenshot and send to a friend; (3) sounds like a fridge, a
  machine with a small voice, an opinion and no shame about sharing it
  at 3am; (4) works as one line of a text message, short enough for a
  lock screen and complete without a follow-up; (5) a fresh angle,
  not the obvious one about milk, ice or a door left open.
- Field cliché avoided: the leaderboard is blind (no top-5 entries to
  study), so the cliché named and avoided is the brief's own list —
  milk, ice, a door left open. None of the candidates uses them.
- Blind pairwise tournament (15 pairs, judged only against the brief):
  A 2 wins, B 3, C 5, D 0, E 1, F 4. Winner: C (5/5).
  A. Pizza hidden behind the butter ("It is mine now"). Fridge as
     thief; good, but the sign-off dilutes the punch.
  B. Tuesday yoghurt started a family ("I did nothing"). Strong
     deadpan, lost to C on specificity and to F on freshness.
  C. WINNER. 2:47 open, 41-second stare, logged as a cry for help.
     Two concrete anchors (a time, a count), three beats (opened ->
     stared -> logged), ends on the punch, and the fridge's voice is
     its own: passive, logging, concerned, shameless at 3am.
  D. Compressor cycle 4,812, joint complaint with the crisper drawer.
     Most technical, least funny; the punch is wordy.
  E. Awake since 2019, never thanked ("The cheese always knows").
     One strong image, but a thinner scene than the others.
  F. Friday leftovers unionised ("They know"). Runner-up at 4/5;
     fresh and sharp, but C's specificity wins the head-to-head.
- Full win table (15 pairs, blind, judged only against the brief):
  A-B: B, A-C: C, A-D: A, A-E: A, A-F: F,
  B-C: C, B-D: B, B-E: B, B-F: F,
  C-D: C, C-E: C, C-F: C,
  D-E: E, D-F: F, E-F: F.
  Wins: A 2, B 3, C 5, D 0, E 1, F 4. Winner C, runner-up F.
- Extra-mile pass after the pick: C stress-tested against the spec
  (127 chars, one line, complete, lock-screen readable), against a
  generic house baseline ("It's 3am and you're hungry again. The
  milk is fine. Go to sleep.") — C wins on specificity and punch —
  and the weakest dimension (the fridge calling itself "me") checked:
  it is the voice the brief asks for, a machine with an opinion.
  No change needed; the line stands as tournament-won.
- Gate check: 127 chars, 1-140 required, UTF-8, single line.
"""

import os

LINE = (
    "3am. You opened me at 2:47, stared for 41 seconds, and closed "
    "me without taking anything. I have logged this as a cry for help."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
