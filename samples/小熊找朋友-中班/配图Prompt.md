# 配图 Prompt · 小熊找朋友（中班 4–5）

> 绘画师(青柚) Stage5 产出。**手动出图**：本文件给的每条 prompt 都可**直接整段复制**粘贴到 ChatGPT/即梦等生图工具。
> 画风：**古典水彩（风格库 #1，默认推荐）**——温暖、低龄友好、契合草地交友题材，已与故事圣经锁定。
> 角色一致性方案：**本书主角是虚构小熊，无真实孩子照片**，故 **跳过"照片"环节**，改为「身份锚点逐字复用 + 先生成一张主参考图(master reference)锁全书」。之后每页只附**主参考图**（无照片可附）。
> 统一画布：**竖版 2:3（≈1024×1536）**，封面、内页、满版高潮**全书同一尺寸**，满版页靠构图铺满、绝不换横版。
> 每条 prompt 末尾固定带 `no text in image`（文字由排版时另放）。

---

## 一、角色参考图流程（最先做，定全书）

### 第 0 步 · 无照片 → 用身份锚点生成「主参考图」

本书角色虚构，没有真实照片可锁相似度。改用下面这条 prompt 先生成 **豆豆设定图**，从结果里挑**一张最合锚点、最合风格**的存为**主参考图（master reference）**。全书每一页都附这张主参考图。

**A. 主角豆豆 · 主参考图 prompt（先出这张）**
```
Character reference sheet for a children's picture-book main character: a small honey-brown bear cub named Doubou.
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CHARACTER (lock every trait): round head and round ears, honey-brown soft fur, plump rounded body, very small in scale (a tiny little cub, toddler proportions). Wears ONLY a pair of cream-yellow dungarees / bib overalls (this single outfit never changes), no shoes. A grass-green little scarf tied at the neck (a clear recognisable marker, readable even from far away). Big eyes, two soft pink blush dots on the cheeks. Default expression is shy and timid — gaze tends to drift down or to the side (shy, NOT sad).
SHEET: show front view and 3/4 view on a plain soft cream background. Include two signature poses side by side — (1) shy pose: fingers laced together, hands half-hidden behind the back; (2) brave pose: head lifted, on tiptoe, both hands holding a small woven basket of berries out in front.
Children's picture book illustration style, no text in image.
```
→ 生成 3–4 张，挑一张最符合 6 条锚点（圆头圆耳 / 蜜糖棕 / 奶黄背带裤 / 草绿围巾 / 红晕 / 害羞低视线）且两组对照动作清楚的，**定为主参考图**。之后每页 prompt 后都附这一张。

**B.（可选）配角三只 · 群体参考图 prompt**
> 三个小伙伴是群体角色，建议也先出一张合照设定图存为**配角参考图**，让后续多人页（P8/P9）认得出是同三只。
```
Character reference sheet for three children's picture-book side characters, same art style as the main sheet.
STYLE: classic painterly children's-book watercolor, soft warm light, visible brush and paper texture, gentle cozy, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
THREE FRIENDS (lock, exactly three, distinct silhouettes, all friendly): (1) a white rabbit with long ears; (2) a yellow duck with a flat bill; (3) a little spotted hedgehog with a round back of soft (non-scary) spines.
MOOD: all three are friendly and absorbed in their own play; they NEVER show rejection, mockery or frowning — they simply haven't noticed Doubou yet.
SHEET: the three standing together on a plain soft cream background, front view.
Children's picture book illustration style, no text in image.
```

### 出图顺序
1. 先出 **A 豆豆主参考图** → 定稿。
2.（可选）出 **B 三只配角参考图** → 定稿。
3. 出 **封面**（最能暴露风格问题）。
4. 按 P1→P11 顺序出内页，**每 3 张回看一次一致性**。
5. 全部出完，**P1 vs P11 并排**做最终校验（首尾同角草地，最考验一致性）。

---

## 二、固定块（每页逐字复用，不要顺手改写）

> 下面两块每页都原样粘贴。**风格块**全书不变；**豆豆锚点块**凡豆豆出场就放；多人页再加**三只配角锚点块**。

**【风格锚点块】**（每页都放）
```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
```

**【豆豆锚点块】**（豆豆出场页都放，逐字一致）
```
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
```

**【三只配角锚点块】**（多人页 P8/P9 才放；远景小身影 P1/P3/P11 也可放精简版）
```
THREE FRIENDS (exactly three, same as the reference, distinct and friendly): a white rabbit (long ears), a yellow duck (flat bill), a spotted hedgehog (round back, soft spines). They are warm and friendly — never frowning, never mocking, never rejecting.
```

**【脊梁道具 · 那一篮野果】**（除特别说明外每页都要能找到它，按需嵌进 ACTION/COMPOSITION）
```
PROP (must appear, the story's spine): a small woven rattan basket of round red-and-purple wild berries, always near Doubou (in his arms / at his side / behind his back). The basket is the brightest, most eye-catching point in each page.
```

### 镜头代码 → SHOT 英文（本书用到的，按模板表翻）
| 代码 | 写进 SHOT |
|---|---|
| EST/WIDE | wide establishing shot, high angle, show the whole environment, the character very small |
| MED | medium shot, character roughly waist-up, focus on the action and interaction |
| CU | close-up on the face and expression, emotional |
| DET | detail / still-life of one object, no main character's face in frame |
| FULL | epic composition filling the SAME portrait canvas edge-to-edge, no border (NOT a wider/landscape spread — keep the same 2:3 size) |

---

## 三、封面 + 11 页 · 每页可直接粘贴的 prompt

> 用法：每条 prompt 已把【风格块】+【豆豆锚点块】(+配角块) 拼好，**整段复制**即可。括号里「(attach: 主参考图)」提示你出图时附上第一步定稿的主参考图。

---

### 封面 · COVER（MED）

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
SHOT: medium shot, Doubou from roughly the waist up, focus on him and the basket.
SCENE: a sunny open meadow in late spring — low wildflowers, one or two round trees, a gentle slope far away.
ACTION: Doubou holds a full small woven rattan basket of round red-and-purple wild berries in both arms, standing in the sunny meadow, smiling shyly with a tiny smile, eyes drifting slightly to the side/down. His grass-green scarf and cream-yellow dungarees are clearly readable. Far in the background, three tiny little figures are faintly playing on the meadow.
COMPOSITION: Doubou centred slightly left, half-figure, his body turned gently to the RIGHT (facing into the book); warm light makes the berry basket the brightest, most eye-catching point; the three distant figures stay tiny and soft in the far background.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 封面脊梁锚：那只篮子作书名物件先亮相。封面不计入 11 页配比。

---

### P1 · 大远景俯瞰，建立世界（EST/WIDE）— 全书唯一「追蝴蝶」页

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
SHOT: wide establishing shot, high angle / slight bird's-eye view, show the whole sunny meadow, the character very small.
SCENE: a whole sunny meadow opening out from above — low wildflowers, one or two round trees, a gentle slope in the distance, lots of empty space and a high horizon.
ACTION: across the far side of the meadow, a white rabbit, a yellow duck and a spotted hedgehog cluster together CHASING A BUTTERFLY (this is the ONLY page in the whole book that shows butterfly-chasing). On THIS near corner of the meadow, a very tiny little Doubou sits crouched, holding his berry basket, looking far away toward them — curious, wanting to come over.
COMPOSITION: wide establishing / slightly high angle; high horizon, lots of sky and empty meadow. Doubou is a TINY dot in the LOWER-RIGHT corner, FACING UP-LEFT, gazing diagonally across the empty grass toward the little group of friends in the far upper-left. His berry basket is the single brightest point on him.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 非人物主导页①（环境为主、豆豆极小）。**机位锚点：全书唯一「追蝴蝶＋大远景俯瞰＋豆豆极小」页，刻意与 P3 拉开**。拟声「沙沙」。

---

### P2 · 想走近又把手藏身后（MED）— 重复句①

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
SHOT: medium shot, Doubou roughly waist-up, focus on his hesitating action.
SCENE: the same sunny meadow, a little closer in; the same berry basket.
ACTION: Doubou gathers a little courage to step toward the friends — one foot just stepping forward — but then PULLS the arm holding the basket BEHIND HIS BACK and LACES HIS FINGERS together, and stops; a classic shy, "didn't-dare" hesitation. The friends are playing a short way off and have not turned around.
COMPOSITION: medium shot, Doubou slightly LEFT and turned to the RIGHT toward the friends; the basket is half-hidden behind his back but a few berries still peek out. He has clearly moved a few steps closer than in P1 (readable "first… then…" progression).
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 重复句①「豆豆，慢了一步。」（犹豫）。**标志动作「手藏身后」首次亮相**。

---

### P3 · v2 中近景·扑空落差（MED）— 重复句②／三处落空同框

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
SHOT: medium / medium-close shot (a sense of "just missed it" close-up), camera clearly closer than P1, lower eye-level.
SCENE: the same meadow, lower eye-level near the grass; NO butterflies anywhere on this page.
ACTION: this time the three friends are NOT chasing a butterfly — they are running off together toward behind the slope, laughing, their BACKS turned to the RIGHT, kicking up a little dust / grass. Doubou really did come a few steps closer this time: ONE HAND is already STRETCHED OUT toward them but STOPS IN MID-AIR, just out of reach; his body JERKS to a STOP (one foot still LIFTED, not yet landed); his FACE is still turned, chasing-gazing after the direction the friends ran. He stopped, but his heart didn't. From the rim of his basket, ONE red-purple berry has been jolted loose and is FALLING DOWNWARD (weightlessness = the concrete feeling of coming up empty).
COMPOSITION: medium-close, Doubou fills nearly half the frame, on the LEFT and slightly forward. The THREE "pause / missing" details — the hand stopped in mid-air, the foot lifted not landed, and the falling berry — are grouped together in the clear FOREGROUND. The friends are only small BACKS in the UPPER-RIGHT, running out past the right page edge (orientation pulls the page-turn). Camera is clearly nearer than P1 and the eye-level is lower — a strong contrast to P1's high wide shot.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 重复句②「豆豆，慢了一步。」（错过）。拟声「咕噜」（果子滚落）。**务必：半空的手＋抬着未落的脚＋正滚落的果子三处落空同框、全在前景清晰可读；小伙伴只剩较小背影、明确在「跑离」而非在场玩；机位明显比 P1 近——确保第一眼读成「豆豆又没跟上」，不是「也在追蝴蝶」或「和 P1 同一张图」。**

---

### P4 · 想喊没敢出声·脸部特写（CU）— 重复句③／情绪最低点

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
SHOT: close-up on Doubou's face and upper body, emotional.
SCENE: the same meadow, softly blurred behind him.
ACTION: Doubou has caught up a little; his mouth is JUST SLIGHTLY OPEN as if about to call out "want to play together?", but the words don't come and he PRESSES his lips shut again; pink blush on the cheeks, eyes cast DOWN — wanting to speak but not daring. His hands still grip the basket handle.
COMPOSITION: big close-up, the face is the main subject; gaze directed to the RIGHT (toward the friends who haven't noticed him); the basket handle still enters frame (berries findable even in the close-up). Lowest emotional point of the book.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 重复句③「豆豆，慢了一步。」（没敢开口）。**第一处特写，与 P6「抬头特写」成对照（同机位、相反情绪）。情绪最低点。**

---

### P5 · 那一篮野果·静物换气页（DET）

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
SHOT: detail / still-life of one object, no main character's face in frame.
SCENE: looking down at the basket; soft warm light.
ACTION: still-life of THE BASKET OF BERRIES as the main subject — a woven rattan basket, woven texture visible, full of round red-and-purple berries, one berry rolled to the rim. Only a sliver of Doubou enters frame: one stretch of the arm hugging the basket and the bottom of his chin (with the grass-green scarf just visible), as he looks DOWN at the basket as if thinking.
COMPOSITION: close still-life, the basket centred and nearly filling the frame, warm light on it; almost no character. This is the breathing page that breaks the three "just-too-late" beats.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 非人物主导页②（DET）。拟声「咕噜」（野果滚动）。**这一页把脊梁物件单独放大，为「用它迈一步」埋伏笔；只露一截手臂/下巴，不画整张脸。**

---

### P6 · 抬头深吸一口气·情绪转折特写（CU）

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
SHOT: close-up turning to half-figure, on the face and emotional turn.
SCENE: the same meadow, warm light, softly behind him.
ACTION: Doubou LIFTS HIS HEAD, chest swelling as he takes a deep breath in; for the first time his eyes look STRAIGHT AHEAD, no longer dodging downward; his face shifts from shy to a touch of resolve (still has the pink blush, but the eyes and brow brighten). Below, his TWO HANDS are seen starting to lift the basket steadily — the beginning of the gesture.
COMPOSITION: big close-up turning to half-figure, Doubou turning to face RIGHT (toward the friends and the page-turn), composition tilted slightly UPWARD. This is the deliberate match-and-reverse of P4's downcast close-up: same framing, opposite emotion (a visible "he changed").
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 拟声「呼——」（深吸气）。**全书情绪转折点；与 P4 配对的对照特写（同机位、相反情绪、篮子从静物回到手上被托起）。**

---

### P7 · 踮脚端篮走过去（MED）

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
SHOT: medium shot, Doubou roughly waist-up to full, focus on his walking action.
SCENE: the same sunny meadow, warm light.
ACTION: Doubou rises ON TIPTOE and STEPS toward the friends, bringing the berry basket UP and FORWARD in both hands (the offering pre-gesture is already starting); his grass-green scarf lifts a little with the motion. The friends are ahead on the right, still playing, not yet turned around.
COMPOSITION: medium shot, Doubou's whole body angled to the RIGHT and LEANING FORWARD, walking toward the right page edge (strong page-turn pull); the basket is at the very front of his body and the brightest point.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图)
```
> 拟声「沙沙」（踮脚走草地，呼应 P1 环境音）。**把动作推到高潮门口；篮子从「托起」到「端着往前送」。**

---

### P8 · 满版高潮·把整篮野果递出去（FULL）— 反转句

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
THREE FRIENDS (exactly three, same as the reference, distinct and friendly): a white rabbit (long ears), a yellow duck (flat bill), a spotted hedgehog (round back, soft spines). They are warm and friendly — never frowning, never mocking, never rejecting.
SHOT: epic composition filling the SAME portrait canvas edge-to-edge, no border (NOT a wider/landscape spread — keep the same 2:3 size).
SCENE: the sunny meadow, glowing warm light, the whole 2:3 canvas filled edge to edge.
ACTION: the climax — Doubou on tiptoe, head lifted, HOLDING THE WHOLE BASKET OF BERRIES HIGH AND FORWARD in both hands as an offering — open, brave and radiant, the strongest possible contrast to the earlier "hands hidden behind the back" hesitation. The three friends are JUST TURNING AROUND, their EYES LIGHTING UP. The berry basket sits at the very centre of the picture, lit by light, the focal point of the whole scene.
COMPOSITION: fill the SAME 2:3 portrait canvas edge-to-edge. Doubou centred slightly left, offering to the RIGHT; the three friends on the right turning back toward the LEFT — all the gazes CONVERGE on the basket (composition locks every orientation onto the basket). Epic full-bleed, highest emotional point.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图 + 配角参考图)
```
> 反转句「这一次，豆豆没有等。」拟声「呀」（小伙伴惊喜）。**高潮满版——保持同一 2:3 画布，靠构图铺满气势，不换横版。递出姿态＝P2「藏身后」的最强反转。**

---

### P9 · 小伙伴围过来欢迎（MED 群像）

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
THREE FRIENDS (exactly three, same as the reference, distinct and friendly): a white rabbit (long ears), a yellow duck (flat bill), a spotted hedgehog (round back, soft spines). They are warm and friendly — never frowning, never mocking, never rejecting.
SHOT: medium shot group, character interaction.
SCENE: the same sunny meadow, warm and lively light.
ACTION: the three friends gather AROUND Doubou — the rabbit reaching out a paw, the duck flapping its wings, the hedgehog leaning in close — all SMILING and WAVING, welcoming him. Doubou is surrounded in the MIDDLE, letting out a relieved breath with a big happy smile (the blush is happiness this time). Everyone's hands reach toward the berry basket. ALL expressions are friendly and warm.
COMPOSITION: medium group shot, Doubou centred; the four orientations all CIRCLE INWARD toward the basket; warm, lively, busy.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图 + 配角参考图)
```
> **表情全部友好（落实「不排斥」红线）。接 P8 递出＝此页的「接住」；同三只小伙伴认得出。情绪：被接纳的安心与喜悦。**

---

### P10 · 一起分野果·篮子空了大半（DET 众手）

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
SHOT: detail / still-life close-up, a ring of small hands, no single main face in frame.
SCENE: the same meadow, warm, dense, lively light.
ACTION: a close ring of little hands / little paws all taking berries from THE BASKET together, each holding one or two round red-purple berries; THE BASKET IS ALREADY MORE THAN HALF EMPTY (the visible clue: it's being shared out). Only the hands and the satisfied chins / corners of smiling faces show — including Doubou's grass-green scarf and chin among them — but no full single face.
COMPOSITION: close still-life plus many hands, the basket centred and ringed by hands; warm, dense, busy. The basket's arc closes from full → emptying.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图 + 配角参考图)
```
> 非人物主导页③（以「手＋篮」细节为主、不靠脸）。拟声「咕噜」（轻俏）。**篮子从满→空＝全书物件弧线收口；落实「分享是善意道具、不渲染吃下去」。**

---

### P11 · 结尾暖场景·首尾呼应（EST/WIDE）

```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
DOUBOU (the bear cub, keep identical every page): round head and round ears, honey-brown soft fur, plump small body, a tiny little cub. Wears ONLY cream-yellow dungarees (never changes), no shoes; a grass-green little scarf at the neck (readable even far away); big eyes, two pink blush dots on the cheeks. Same face, same outfit, same scarf every page.
THREE FRIENDS (exactly three, same as the reference, distinct and friendly): a white rabbit (long ears), a yellow duck (flat bill), a spotted hedgehog (round back, soft spines). They are warm and friendly — never frowning, never mocking, never rejecting.
SHOT: wide establishing shot, show the whole meadow, characters small within the landscape.
SCENE: pull back to THE SAME CORNER of the meadow as P1 — the same low wildflowers, round trees and gentle slope (we've come full circle).
ACTION: this time Doubou is playing TOGETHER IN THE MIDDLE of the friends (rolling a ball / chasing together), his grass-green scarf fluttering, everyone laughing. The EMPTY basket rests on the grass nearby with one or two berries fallen beside it (the same one basket — the story's full stop).
COMPOSITION: wide shot; this time Doubou is right IN THE MIDDLE of the group (the deliberate contrast to P1, where he was alone in the lower-left corner); spread out horizontally within the same 2:3 canvas, warm light flooding the whole scene.
Children's picture book illustration, single page, warm and child-friendly, no text in image.
(attach: 主参考图 + 配角参考图)
```
> 非人物/环境主导页④（远景为主）。拟声「沙沙」收尾（呼应 P1/P7）。**镜头回到 P1 同一角草地、豆豆从左下角落单 → 人群正中央：用同一画面位置的对照讲出「我也有朋友了」。结尾给画面、不给说教。**

---

## 四、一致性校验清单

> 出图过程中按此自检。漂移了就：**重附主参考图 / 加重锚点描述 / 局部重绘（inpainting）**。

**A. 尺寸 / 画布**
- [ ] 每页尺寸完全一致（同一 2:3 画布，封面也一样）？
- [ ] P8 满版高潮**没有**换成更宽/横版？（只靠构图铺满同一张 2:3）
- [ ] 工具出图尺寸略有出入的，排版成 PDF 前**统一裁成同一 2:3**。

**B. 豆豆角色锚点（每出场页逐条核）**
- [ ] 圆头圆耳、蜜糖棕绒毛、圆胖小个子？
- [ ] **仅**奶黄背带裤、无鞋（全书没换装）？
- [ ] 草绿围巾在脖子上（远景也认得出）？
- [ ] 大眼睛 + 两点脸颊红晕？
- [ ] 害羞页眼神往下/往侧（害羞不是难过）；勇气页（P6–P8）抬头、踮脚、双手前递？
- [ ] **「手指绞在身后＝犹豫」** 在 P2 出现、并在 P8「双手前递」处形成反转？

**C. 三只配角（P1/P3/P8/P9/P11）**
- [ ] 始终**恰好 3 只**：白兔(长耳)／黄鸭(扁嘴)／花斑刺猬(圆背软刺)，认得出是同三只？
- [ ] 全程**友好、专注自己玩**，无皱眉/嘲笑/排斥表情？（红线）
- [ ] P1 在追蝴蝶、P3 在结伴跑开——两页玩法**不撞图**？

**D. 脊梁道具「那一篮野果」**
- [ ] 每页都能找到篮子（豆豆手边/身后），且是画面最亮点？
- [ ] 物件弧线：封面→P8 满；P10 空了大半；P11 空篮搁草地——**满→空**读得出来？
- [ ] P3 有一颗野果正滚落（扑空具象）？P5 一颗滚到篮边？

**E. 风格 / 光线 / 色调**
- [ ] 全书古典水彩、暖光、同一色板（ambers / sage / sky blue / cream）统一不忽明忽暗？
- [ ] 每页都带 `no text in image`、出图无残留文字？

**F. 叙事节拍 / 机位（交叉核对画面脚本）**
- [ ] **P1 大远景俯瞰·豆豆极小** ↔ **P3 中近景·视平线放低**：机位明显拉开、不雷同？
- [ ] **P3 三处落空同框且在前景清晰**：半空的手 + 抬着未落的脚 + 正滚落的果子？小伙伴只剩较小背影、明确「跑离」？
- [ ] **P4 低头特写 ↔ P6 抬头特写**：同机位、相反情绪的对照成立？
- [ ] **P8 满版**：所有朝向/视线都锁向篮子、是全场焦点？
- [ ] **P1 ↔ P11 同角草地呼应**：豆豆从左下角落单 → 人群正中央，位置对照读得出？
- [ ] 非人物主导页（P1/P5/P10/P11）没有不小心把豆豆整张脸画成主体（P5/P10 只露局部）？

**G. 出图顺序回看**
- [ ] 先定主参考图 → 封面 → P1…P11，**每 3 张回看一次**？
- [ ] 全部出完后 **P1 vs P11 并排**做最终一致性校验？

---

> 青柚的话：这本书没有真实照片兜底，**主参考图就是命根子**——先把它出到满意再动内页，每页都附上它。三处最容易翻车的地方我已在 prompt 里加重写明：①P3 别又被读成「追蝴蝶／和 P1 同图」（已脱钩玩法 + 拉低机位 + 三处落空同框）；②豆豆「犹豫 vs 勇气」两组对照动作（P2 藏手 ↔ P8 前递、P4 低头 ↔ P6 抬头）要画出可见反差；③篮子满→空的物件弧线每页盯紧。漂移就重附参考图、别将就。
