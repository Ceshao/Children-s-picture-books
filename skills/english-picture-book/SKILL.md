---
name: english-picture-book
description: >-
  Create a custom English picture book for a young child (ages 2–6), especially
  for a preschooler's "show and tell" where the child recites the book themselves.
  Turns a story idea plus an uploaded photo of the real child into a complete,
  ready-to-illustrate book: a Story Bible (character/style lock), a page-by-page
  Storyboard with finished English text, and per-page AI image-generation prompts
  that keep the child's likeness and the art style consistent across every page.
  Use this skill WHENEVER the user wants to make, customize, write, or illustrate
  a children's picture book, storybook, bedtime book, or 绘本 for a kid — including
  requests like "make an English picture book for my niece", "我想给小孩定制一本绘本",
  "turn this story into a kids' book", "a show-and-tell book for a 3-year-old", or
  when they share a child's photo and want a personalized illustrated story. Trigger
  even if they don't say the exact words "picture book". Do NOT use for chapter books
  for older readers, coloring pages, or generic adult illustration.
---

# English Picture Book (custom, for young children)

This skill produces a **complete, ready-to-illustrate English picture book** tuned so a
**2–6 year old can follow it — and ideally recite it from memory** while showing the
pages (classroom "show and tell"). The child's likeness comes from a **photo the user
uploads**; the story and pictures are built to professional picture-book craft standards
(distilled from Caldecott Medal/Honor books and early-literacy research).

**What you deliver (markdown files + image prompts):**
1. `story-bible.md` — locks character likeness, world, art style, and the **refrain**
2. `storyboard.md` — page-by-page: shot type + finished English text
3. `image-prompts.md` — one ready-to-paste prompt per page, built to keep likeness + style consistent
4. A short production note telling the user how to generate the images and assemble the PDF

The user generates the actual images themselves (e.g. in ChatGPT/Codex image tools) using
your prompts + their uploaded photo. You do the writing and art direction.

---

## The core idea (internalize this first)

> **The picture shows "what happens." The words only add the one thing the picture can't:
> a sound, a line of dialogue, or a hook into the page turn. Never narrate what the
> reader can already see.**

The single most common failure (and the reason most AI-made "picture books" feel off) is
**narrator prose**: long sentences that describe the illustration. That makes the text feel
unnatural, too long, and impossible for a small child to recite. You are fixing that by
default. Read `references/design-standards.md` for the full reasoning and the Caldecott
casebook; the rules below are the operational summary.

---

## North Star — what "good" actually feels like

The detailed rules can drown out the felt target. Keep this north star in front of you the
whole time:

> **You are not telling a child a story. You are giving the child a GAME they can memorize,
> play, and perform** — the words are chants and sounds, the pictures are rhythm and breath,
> the page turn is a surprise.

The gold-standard models for *a 3-year-old reciting it themselves* are books like
**We're Going on a Bear Hunt** (a repeatable journey of obstacles, each with a sound word
chanted ×3 and a fixed refrain, then an accelerated return trip), **Brown Bear, Brown Bear**
(one fixed sentence frame, change one word per page), **Don't Let the Pigeon Drive the Bus!**
(talk straight to the reader; minimal art with lots of white space still carries huge emotion),
and **Goodnight Moon** (cumulative naming, the picture dims to show time passing, a warm safe
close). See `references/north-star.md` for the worked study of each.

**The 6 felt checks** — read your own draft and ask these; if any answer isn't "yes", it's not
good enough yet:
1. **Can they guess?** Reading half a page, can the child predict the next line? (a signature
   refrain / fixed frame)
2. **Play or homework?** Does it read like a game you want to chant, or like reciting a
   description?
3. **Can they perform it?** Sound words, actions, or lines spoken straight to the listener —
   something the child does with mouth and body, not just hears.
4. **Does the picture breathe?** Across page turns, do scale / light / colour / near-vs-far
   actually change — or is it ten pages of the same shot? (the #1 thing AI image generation
   gets wrong)
5. **Is it small enough?** One smallest idea per page (one line, a few words)?
6. **Is it warm?** Does the ending return to safety, warmth, quiet?

These six are the human-memorable version of the red lines below. When in doubt, serve the
north star, not the rule list.

---

## Workflow

Work through these steps in order. Confirm with the user at the gates marked **→ confirm**.

### Step 1 — Gather inputs
Ask for (in one message, but don't block on perfection):
- **The child**: name, age, and a **photo** (this is the character reference — the book's
  hero will be an illustrated version of the real child). If no photo, ask for a
  description, but a photo gives far better likeness.
- **The story seed**: any idea, theme, or occasion (e.g. "loves dinosaurs", "starting
  preschool", "a trip to grandma's"). If they have none, offer 2–3 simple premises.
- **Reading mode**: will the child **recite it themselves** (→ text must be shorter, more
  patterned, heavier repetition) or will an adult read it aloud? Default to *recite-themselves*
  since that's the hardest and most common ask.
- **Length**: default to **~12 picture pages** (plus cover) unless they say otherwise.

### Step 2 — Write the Story Bible  → confirm
Copy `assets/story-bible-template.md` and fill it in. The make-or-break fields:
- **Identity anchors** (3–7 per character): the handful of visual features that must stay
  identical on every page (hair, a signature jacket/hat, etc.). For the child hero, derive
  these from the photo + a chosen book outfit.
- **Style anchors**: medium, palette, light — a few concrete phrases that go verbatim into
  every image prompt so the art doesn't drift.
- **The refrain**: ONE short repeated line (≤6 words), ideally spoken dialogue, that recurs
  at a fixed story beat. This is the backbone of recitation — design it deliberately.
- A reusable **sound-word list** and a **recurring landmark object** (used to physically
  link scenes so the story doesn't feel jumpy).

Show the Story Bible to the user and adjust before writing pages.

### Step 3 — Storyboard + write the text  → confirm
Copy `assets/storyboard-template.md`. Lay out ~12 pages with a clear arc (setup → a small
want/problem → a repeated journey carrying the refrain → one big climax page → a warm, safe
ending). For each page set the **shot type** and write the **finished English text**.

Apply the text rules (Step 5) and the picture rules (Step 6) as you go. Then run the
**self-check** (Step 7) and fix anything before showing the user.

### Step 4 — Image prompts (with the real photo as reference)
Copy `assets/image-prompt-template.md`. For each page, assemble:
`[fixed style block] + [fixed character-anchor block] + [this page's shot + scene + action]`.

**Likeness flow (important):**
1. First produce a **character reference prompt** that turns the uploaded photo into an
   *illustrated* version of the child in the book's style (front + 3/4 view, plain
   background). Tell the user to generate this FIRST, attaching their photo, and pick one
   they like as the **master reference**.
2. For every page, tell the user to attach **both** the uploaded photo (locks the face/likeness)
   **and** the approved master reference (locks the illustrated style), alongside the page prompt.
3. The anchor block (outfit, palette) is repeated verbatim every page so nothing drifts.

### Step 5 — Production note
Give the user a short, plain checklist: generate the character reference → cover → pages in
order (eyeball consistency every ~3 pages) → put the page text under each image → export to PDF.

---

## Text rules (the operational red lines)

These exist because of how 2–6 year olds actually process language (see design-standards
§3–4). Hold to them:

- **One sentence per page** (two short ones max). The page turn is your punctuation.
- **≤8 words per sentence**; core lines 4–6 words.
- **A refrain repeated ≥3 times** at a fixed beat — the spine of memorization. A great
  pattern: the *problem varies each time, the hero's response stays identical* (e.g. every
  obstacle → `"Slow and brave," said Orion.`). Predictable response = the child can recite it.
- **Use dialogue and sound words, not narration.** `"Shh," said Mia. "I hear it."` beats
  `Mia listened carefully.` Include **≥3 onomatopoeia / sound words** (crunch, splash, whoosh)
  so the child performs with their voice and body.
- **Concrete and literal by default.** Children under ~6 do not reliably understand novel
  metaphor or personification. Adult-poetic lines like *"giant leaves whispered in the breeze"*
  are too hard — rewrite to something seen/heard/done: *"The big leaves moved. Sshh, sshh."*
  At most one figurative touch, and only with clear picture support.
- **Rhyme is optional and risky.** Either it scans perfectly every line, or don't rhyme.
  Forced rhyme (bending words to hit a rhyme) wrecks the rhythm — avoid it.
- **Total length**: aim ~150–400 words; for a young reciter, ~100–150 is fine and often better.
- **Read-aloud test before delivering**: read every page out loud 3×; if a line trips the
  tongue, swap a word for one with a different syllable count.

## Picture rules (kills the "every page is the same shot of the kid" problem)

Shot variety is narrative language, not decoration — it sets pace, emotion, and a sense of
place (see design-standards §5). Across ~12 pages:

- **Vary the shot.** Use at least one each of: **establishing/environment** (wide, sets the
  world, gives a breath), **detail/still-life** (one object — a clue, a glowing egg),
  **close-up** (saved for an emotional beat), and **full-bleed** (the climax). Don't shoot
  the whole book in the same medium shot of the hero facing forward.
- **≥25% of pages have no main character** (environment / object pages). This is what makes a
  book feel like a *world* and adds the variety young kids enjoy.
- **Picture–text complementarity**: each page's words must NOT restate what's drawn.
- **Climax = one full-bleed page**, optionally wordless — let the picture carry it.
- **Honor left-to-right momentum**: face the hero toward the right / next page to pull the
  turn.
- **Link scenes physically** (a path, a sound, a recurring object) so the story doesn't jump.

## Consistency rules (AI image generation)

- Repeat the **3–7 identity anchors** and the **style block** verbatim in every prompt.
- Always pass the **uploaded photo + master reference** with each page (see Step 4).
- After generating, put the **first and last page side by side** — if the child or style
  drifted, regenerate with the anchors re-emphasized. Drift is cumulative and invisible until
  you compare ends.

---

## Before delivering — self-check

Verify against `assets/production-checklist.md` (the operational version of the red lines).
Quick gate, every book:
- [ ] Every page ≤2 short sentences, ≤8 words each
- [ ] Refrain recurs ≥3× at a fixed beat
- [ ] ≥3 sound words; key beats are dialogue, not narration
- [ ] No adult-metaphor lines; concrete and literal
- [ ] Shot variety present (establishing + detail + close-up + full-bleed)
- [ ] ≥25% pages with no main character
- [ ] No page's text merely restates its picture
- [ ] Scenes physically linked; ending returns to safety/warmth
- [ ] Identity + style anchors written into every image prompt

---

## Reference material (read as needed)

- `references/north-star.md` — the felt standard: a worked study of 4 gold-standard models for
  a 3-year-old reciter (Bear Hunt / Brown Bear / Pigeon / Goodnight Moon) and the 6 checks.
  Read this to calibrate "what good feels like" before judging your own draft.
- `references/design-standards.md` — the full *why*: age cognition (2–6), the text/picture
  craft, the Caldecott Medal/Honor casebook (Caldecott rewards **illustration**, awarded to
  illustrators), and the source-backed rationale. Read this when you need to justify a choice
  or go deeper than the summary above.
- `references/orion-example.md` — a complete worked example (a real before→after rewrite of an
  AI-made book), showing the narrator-prose problem and the fix. Read this to calibrate the
  target quality and see the templates filled in.
- `assets/` — the templates to copy for each new book, plus the production checklist.
