# 风格库 · Style Library（让客户挑画风）

> 给客户一组**可选画风**，每种都配好**可直接贴进 prompt 的 STYLE / PALETTE 块**。
> 客户选定一种 → 复制进《故事圣经》§5 → 全书每页 prompt 都用它，保证统一。
> 选不定时用最下面的「风格试片」：同一画面、只换 STYLE，生成 2–3 张对比着选。
>
> （此文件与 `skills/english-picture-book/references/style-library.md` 内容一致；改动请同步两处。）

三个对"3 岁 show-and-tell"关键的指标：**远看清晰度**（举给全班看好不好认）·**相似度友好度**（照片插画化后像不像本人）·**跨页一致性**（连出十几页稳不稳）。

---

## 1. 古典水彩 · Classic Watercolor（默认 · 推荐）
温柔、暖、有层次，略带魔幻，质感最高（经典凯迪克/Van Allsburg 式 painterly）。适合温柔冒险、自然、睡前。
远看：中 · 相似度：**高** · 一致性：中
```
STYLE: classic painterly children's-book watercolor, soft warm light, lush layered depth, visible brush and paper texture, gentle cozy and slightly magical, never scary.
PALETTE: warm naturalistic tones — ambers, sage greens, sky blues, cream.
```

## 2. 现代扁平 · Modern Flat / Vector
干净色块、简洁线条、大量留白、明快不渐变。**远看最清楚**，最适合演讲。
远看：**高** · 相似度：中 · 一致性：**高**
```
STYLE: modern flat vector children's-book illustration, bold simple shapes, clean outlines, flat cheerful colors, generous negative space, no gradients.
PALETTE: bright, limited, high-contrast.
```

## 3. 拼贴 · Cut-Paper Collage
撕纸/剪纸质感、大胆单一主体、手作触感（Eric Carle/Ezra Jack Keats 传统）。
远看：**高** · 相似度：中低 · 一致性：中
```
STYLE: torn-and-cut paper collage illustration, visible paper texture and edges, bold single subjects, handmade tactile feel.
PALETTE: rich saturated hues with textured overlays.
```

## 4. 蜡笔童趣 · Crayon / Childlike
粗蜡笔/彩铅质感、像孩子自己画的、松弛亲切。
远看：中 · 相似度：中 · 一致性：中
```
STYLE: chunky crayon and colored-pencil texture, playful childlike hand-drawn look, warm and friendly, loose energetic lines.
PALETTE: warm friendly primaries.
```

## 5. 柔和数字 · Soft Digital / Gouache
现代、干净、圆润，水粉哑光质感，柔光，温暖贴纸感。
远看：中高 · 相似度：**高** · 一致性：**高**
```
STYLE: soft contemporary digital illustration with gouache-like matte shading, rounded friendly shapes, gentle soft lighting, smooth cozy finish.
PALETTE: soft pastels with warm accents.
```

## 6. 复古限色 · Retro / Limited Palette
中世纪复古、2–4 色、丝网印质感、几何简洁、有设计感（《奥莉薇》克制用色）。
远看：**高** · 相似度：中低 · 一致性：**高**
```
STYLE: mid-century retro storybook look, limited 2–4 colour palette, screenprint texture, simple geometric shapes, stylish and bold.
PALETTE: 2–4 colours only (e.g. black + warm red + cream).
```

## 7. 柔感 3D · Soft 3D / Cinematic
圆润 3D 角色、电影感柔光、讨喜（皮克斯式暖感）。
远看：**高** · 相似度：中高 · 一致性：**低** ⚠️ 跨页最易漂移、书感偏弱、更费劲，要用就更严格靠照片+主参考图锁定。
```
STYLE: soft rounded 3D-rendered characters, cinematic soft lighting, shallow depth of field, friendly warm Pixar-like look.
PALETTE: warm cinematic tones.
```

## 8. 水墨 · Ink & Wash / East-Asian（双文化加分）
软水墨+淡彩、大量留白、抒情笔触（《你好，灯塔》墨底、《狼婆婆》传统）。
远看：中 · 相似度：中 · 一致性：中
```
STYLE: soft ink-and-wash with light watercolor, lots of white space, lyrical brushwork, calm and poetic.
PALETTE: muted ink tones with soft colour accents.
```

---

## 给客户挑选的建议
- **最适合 show-and-tell（远看清楚+省心）**：现代扁平(2)、柔和数字(5)、复古限色(6)。
- **最像本人**：古典水彩(1)、柔和数字(5)、蜡笔(4)。
- **质感/收藏感最高**：古典水彩(1)、拼贴(3)、水墨(8)。
- **拿不准就选**：默认 **古典水彩(1)**。

## 风格试片（让客户看着实图选）
挑 2–3 个候选 → 选同一个画面（建议封面）→ **用完全相同的 prompt 正文，只换 STYLE/PALETTE** 各出 1 张 → 并排给客户选 → 选定写进《故事圣经》§5 锁定。
> 公平对比的关键：除 STYLE/PALETTE 外，同场景、同构图、同画布尺寸、同附的照片，一律不变。
