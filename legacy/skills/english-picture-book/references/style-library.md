# 风格库 · Style Library（让客户挑画风）

> 作用：给客户一组**可选画风**，每种都配好**可直接贴进 prompt 的 STYLE / PALETTE 块**。
> 用法：客户选定一种 → 把它的 STYLE/PALETTE 复制进 `story-bible.md §5` → 全书每页 prompt 都用它，保证统一。
> 选不定时，用最下面的「风格试片」机制：同一个画面、只换 STYLE，生成 2–3 张让客户对比着选。

每种风格标了三个对"3 岁 show-and-tell"很关键的指标：
- **远看清晰度**：举着书给全班看，从几米外好不好认（高 = 更适合演讲）。
- **相似度友好度**：把真实孩子照片插画化后，还像不像本人（高 = 更保脸）。
- **跨页一致性**：AI 连出十几页，画风/角色稳不稳（高 = 更省心、少漂移）。

---

## 1. 古典水彩 · Classic Watercolor（默认 · 推荐）
温柔、暖、有层次，略带魔幻，质感最高。像经典凯迪克/Van Allsburg 那种 painterly 绘本。适合：温柔冒险、自然、睡前。
- 远看清晰度：中 · 相似度友好度：**高** · 跨页一致性：中
```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
```

## 2. 现代扁平 · Modern Flat / Vector
干净的色块、简洁线条、大量留白、明快不渐变。**远看最清楚**，最适合演讲场景。适合：明快、概念清晰、活泼。
- 远看清晰度：**高** · 相似度友好度：中（孩子被简化成几个锚点特征）· 跨页一致性：**高**
```
STYLE: modern flat vector children's-book illustration, bold simple shapes, clean outlines, flat cheerful colors, generous negative space, no gradients.
PALETTE: bright, limited, high-contrast.
```

## 3. 拼贴 · Cut-Paper Collage
撕纸/剪纸质感、大胆的单一主体、手作触感（Eric Carle《棕熊》、Ezra Jack Keats《下雪天》的传统）。适合：质感、大胆、有记忆点。
- 远看清晰度：**高** · 相似度友好度：中低（很风格化）· 跨页一致性：中
```
STYLE: torn-and-cut paper collage illustration, visible paper texture and edges, bold single subjects, handmade tactile feel.
PALETTE: rich saturated hues with textured overlays.
```

## 4. 蜡笔童趣 · Crayon / Childlike
粗蜡笔/彩铅质感、像孩子自己画的、松弛有活力、亲切。适合：贴近孩子、温暖、不那么"精致"。
- 远看清晰度：中 · 相似度友好度：中 · 跨页一致性：中
```
STYLE: chunky crayon and colored-pencil texture, playful childlike hand-drawn look, warm and friendly, loose energetic lines.
PALETTE: warm friendly primaries.
```

## 5. 柔和数字 · Soft Digital / Gouache
现代、干净、圆润，水粉般的哑光质感，柔光，温暖贴纸感。适合：现代家庭、清新、好印刷。
- 远看清晰度：中高 · 相似度友好度：**高** · 跨页一致性：**高**
```
STYLE: soft contemporary digital illustration with gouache-like matte shading, rounded friendly shapes, gentle soft lighting, smooth cozy finish.
PALETTE: soft pastels with warm accents.
```

## 6. 复古限色 · Retro / Limited Palette
中世纪复古绘本感、只用 2–4 个颜色、丝网印质感、几何简洁、有设计感（《奥莉薇》的克制用色）。适合：风格化、强角色、克制高级。
- 远看清晰度：**高** · 相似度友好度：中低 · 跨页一致性：**高**
```
STYLE: mid-century retro storybook look, limited 2–4 colour palette, screenprint texture, simple geometric shapes, stylish and bold.
PALETTE: 2–4 colours only (e.g. black + warm red + cream).
```

## 7. 柔感 3D · Soft 3D / Cinematic
圆润 3D 角色、电影感柔光、讨喜（皮克斯式暖感）。娃缘好、画面吸睛。
- 远看清晰度：**高** · 相似度友好度：中高 · 跨页一致性：**低**
- ⚠️ 提醒：跨页一致性最难维持、"书感"偏弱、生成更费劲。要这种风格就**更要严格用照片+主参考图锁定**。
```
STYLE: soft rounded 3D-rendered characters, cinematic soft lighting, shallow depth of field, friendly warm Pixar-like look.
PALETTE: warm cinematic tones.
```

## 8. 水墨 · Ink & Wash / East-Asian（双文化加分）
软水墨+淡彩、大量留白、抒情笔触（《你好，灯塔》墨底、《狼婆婆》传统）。适合：抒情、东方韵味、中外双文化家庭的纪念意义。
- 远看清晰度：中 · 相似度友好度：中 · 跨页一致性：中
```
STYLE: soft ink-and-wash with light watercolor, lots of white space, lyrical brushwork, calm and poetic.
PALETTE: muted ink tones with soft colour accents.
```

---

## 给客户挑选的建议（按场景）
- **最适合 show-and-tell（远看清楚 + 省心一致）**：现代扁平(2)、柔和数字(5)、复古限色(6)。
- **最像本人（保脸）**：古典水彩(1)、柔和数字(5)、蜡笔(4)。
- **质感/收藏感最高**：古典水彩(1)、拼贴(3)、水墨(8)。
- **拿不准就选**：默认 **古典水彩(1)**（你现有 V3 就是这种，温暖、保脸、质感好）。

## 风格试片（让客户看着实图选 · 强烈推荐）
1. 跟客户聊完，挑 **2–3 个候选**风格。
2. 选**同一个画面**（建议封面，或一张主角清晰的页）。
3. 用**完全相同的 prompt 正文**，只把 STYLE/PALETTE 换成各候选风格，各生成 1 张。
4. 把这 2–3 张并排给客户 → 客户**看着实图**选。
5. 选定后，把那套 STYLE/PALETTE 写进 `story-bible.md §5` 锁定，全书统一。

> 关键：试片时除了 STYLE/PALETTE，**其它一律不变**（同场景、同构图、同画布尺寸、同附的照片），这样对比才公平。
