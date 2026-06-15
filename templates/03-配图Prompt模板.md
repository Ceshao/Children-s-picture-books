# 配图 Prompt 模板（AI 生图 · 保角色一致 + 风格一致）

> 作用：把 Story Bible 的"锚点"和分镜表的"画面内容/镜头"拼成稳定的生图 prompt。
> 核心原则：**每条 prompt = 固定块（风格+角色锚点，每页不变）+ 变化块（这一页的镜头+动作+场景）。**

---

## 0. 生图前置：先做"角色参考图"
1. 第一步**只生成角色设定图**（不带场景）：正面 + 3/4 侧，干净背景。
   - prompt 用下面的「角色锚点块」+ `character reference sheet, front and 3/4 view, plain background`。
2. 选定一张满意的作为**主参考图**。之后每页：
   - 能上传参考图的工具（如 ChatGPT 图像）→ **每页都附这张参考图** + 文字 prompt。
   - 只能纯文字的工具 → 把「角色锚点块」**一字不差**地复制进每页。

---

## 1. 固定块（从 Story Bible 复制，每页都放）

**【风格锚点块】**（来自 Story Bible §5）
```
STYLE: classic painterly children's-book watercolor, soft warm golden light,
layered depth, gentle cozy slightly-magical mood, never scary.
PALETTE: warm amber, sage green, soft sky blue, cream.
```

**【角色锚点块】**（来自 Story Bible §3，每个出场角色都写）
```
ORION: a round-faced young Asian boy, orange hooded jacket, blue bucket hat,
small shoulder bag, blue sneakers. Same face and outfit every page.
PIP: a small friendly baby pterosaur, green body, orange wing membranes,
orange head-crest, big eyes, half a head shorter than Orion. Same every page.
```

## 2. 变化块（从分镜表每行取值）
```
SHOT: [EST/WIDE/MED/CU/DET/FULL → 翻译成英文镜头描述，见下表]
SCENE: [这一页的场景，来自 Story Bible §4]
ACTION: [这一页角色在做什么，来自分镜"画面内容"]
COMPOSITION: [构图/朝向，配合从左到右翻页动量]
```

### 镜头代码 → prompt 英文
| 代码 | 写进 SHOT 的英文 |
|---|---|
| EST | wide establishing shot, high angle, show the whole environment, characters small |
| WIDE | wide shot, character within a large landscape |
| MED | medium shot, characters from waist up, focus on interaction |
| CU | close-up on face and expression, emotional |
| DET | detail shot / still life of one object, no characters or characters out of frame |
| FULL | full-bleed dramatic spread, fills the whole page, epic |

## 3. 完整 prompt 拼装公式
```
[风格锚点块]
[出场角色的角色锚点块]
SHOT: <镜头英文>
SCENE: <场景>
ACTION: <动作>
COMPOSITION: <构图，e.g. character facing right, leading the eye toward the page edge>
Children's picture book illustration, single page.
```

### 示例（分镜第 6 页：环境建立镜头，无人物）
```
STYLE: classic painterly children's-book watercolor, soft warm golden light, layered depth, gentle cozy slightly-magical mood, never scary.
PALETTE: warm amber, sage green, soft sky blue, cream.
SHOT: wide establishing shot, high angle, show the whole fern valley, a winding trail and a distant waterfall with a faint rainbow.
SCENE: the giant fern forest, silver footprints on the trail.
ACTION: no characters in frame — just the quiet valley and the trail of silver prints leading toward the cliffs.
COMPOSITION: trail leads from lower-left toward upper-right, inviting the eye forward.
Children's picture book illustration, single page.
```
> 注意：这是一张**纯环境页**（满足"非人物页 ≥25%"），文字那页只配一个声音词，如 *Shh. The valley was very quiet.*

## 4. 一致性校验（出图后必做）
- [ ] 每个角色锚点是否都在（脸/服装/比例/配色）？
- [ ] 风格/光线/色调和前几页一致？
- [ ] **把第 1 页和最后一页并排**，角色像不像同一个？
- [ ] 漂移了就：重新喂参考图 / 在 prompt 里加重锚点描述 / 局部重绘。

## 5. 出图顺序建议
1. 先出**角色参考图** → 定稿。
2. 出**封面**（信息量最大，最能暴露风格问题）。
3. 按分镜顺序出内页，每出 3 张回看一次一致性。
4. 全部出完，首尾并排做最终校验。
