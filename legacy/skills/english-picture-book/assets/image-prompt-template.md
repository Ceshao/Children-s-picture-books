# 配图 Prompt 模板（AI 生图 · 用真实照片锁相似度 + 锁风格）

> 核心：每条 prompt = **固定块（风格 + 角色锚点 + 画布尺寸，每页不变）+ 变化块（这一页的镜头/动作/场景）**。
> 相似度靠"附图"保证：每页都附 **① 用户上传的照片** + **② 已定稿的插画版主参考图**。

> **🔒 统一尺寸铁律**：所有页（封面、扉页、内页、满版高潮页）都用**同一个画布尺寸**（默认竖版 2:3，≈1024×1536），来自 Story Bible 的 Canvas 字段。每条 prompt 都带 `CANVAS` 行；高潮页靠**构图**铺满同一张画布制造气势，**绝不换更宽/横版尺寸**。若所用工具出图尺寸略有出入，排版成 PDF 前**统一裁成同一尺寸**。

---

## 第 0 步 · 把照片变成"插画版角色参考图"（最先做，定全书）

让用户**附上孩子的真实照片**，配下面的 prompt 生成插画版设定图：
```
Turn the child in the attached photo into a children's-book character.
Keep the child's real likeness: face shape, hair, skin tone, the look in the photo.
Render in the book's art style.
STYLE: [从 Story Bible §5 复制风格锚点块]
OUTFIT: [书中固定服装，来自 Story Bible §3 锚点]
Character reference sheet: front view and 3/4 view, plain soft background, friendly expression.
```
→ 生成几张，选一张最像、最合风格的，存为 **主参考图**。之后每页都附"照片 + 主参考图"。

> 工具说明：能附参考图的工具（如 ChatGPT/多数图像模型）效果最好。纯文字工具则把下面的「角色锚点块」一字不差复制进每页（相似度会差一些）。

---

## 固定块（从 Story Bible 复制，每页都放）

**【风格锚点块】**（Story Bible §5）
```
STYLE: <medium / mood>.
PALETTE: <主色板>.
CANVAS: portrait 2:3 (≈1024×1536) — the SAME size on every page, cover included.
```

**【角色锚点块】**（Story Bible §3，每个出场角色都写）
```
<NAME>: <3–7 个身份锚点：脸/发/服装/比例/特征>. Same face and outfit every page.
```

## 变化块（分镜表每行取值）
```
SHOT:  <见下表，把镜头代码翻成英文>
SCENE: <场景，来自 Story Bible §4>
ACTION:<这一页角色在做什么，来自分镜"画面内容">
COMPOSITION: <构图/朝向，配合左→右翻页动量>
```

### 镜头代码 → prompt 英文
| 代码 | 写进 SHOT |
|---|---|
| EST | wide establishing shot, high angle, show the whole environment, characters small or absent |
| WIDE | wide shot, character within a large landscape |
| MED | medium shot, characters from the waist up, focus on interaction |
| CU | close-up on face and expression, emotional |
| DET | detail / still-life of one object, no main character in frame |
| FULL | epic composition filling the SAME portrait canvas edge-to-edge, no border (NOT a wider/landscape spread — keep the same size) |

## 完整 prompt 拼装公式
```
[风格锚点块]
[出场角色的角色锚点块]
SHOT: <镜头英文>
SCENE: <场景>
ACTION: <动作>
COMPOSITION: <构图，e.g. character facing right, leading the eye toward the page edge>
Children's picture book illustration, single page.
(attach: 孩子照片 + 主参考图)
```

### 示例（一张纯环境建立镜头，无主角）
```
STYLE: classic painterly children's-book watercolor, soft warm morning light, lush layered depth, gentle and cozy, never scary.
PALETTE: warm amber, sage green, soft sky blue, cream.
CANVAS: portrait 2:3 (≈1024×1536) — same size as every page.
SHOT: wide establishing shot, high angle, show the whole valley, a winding trail and a distant waterfall.
SCENE: a quiet green valley at sunrise.
ACTION: no characters in frame — just the calm valley and the trail leading forward.
COMPOSITION: trail leads from lower-left toward upper-right, inviting the eye forward.
Children's picture book illustration, single page.
```
> 这是满足"非人物页 ≥25%"的环境页；该页文字只配一个声音词或一句短句。

---

## 出图顺序 & 一致性校验
1. 先出**角色参考图** → 定稿主参考图。
2. 出**封面**（最能暴露风格问题）。
3. 按分镜顺序出内页，每 3 张回看一次一致性。
4. 全部出完，**首页 vs 末页并排**做最终校验。

校验清单：
- [ ] **每页尺寸完全一致**（同一画布，封面也一样）？满版页没有换成更宽/横版？
- [ ] 每页角色锚点都在（脸/发/服装/比例）、且像照片里的孩子？
- [ ] 画风/光线/色调全书统一？
- [ ] 非人物页没有不小心又画上主角？
- [ ] 漂移了就：重新附照片+主参考图 / 加重锚点描述 / 局部重绘。
