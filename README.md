# test-data

## Contents

- `worldview-china-podcast/hA7hZjLaN8s.podcast-script.md`: Worldview China 播客文字稿，源视频为 The Bridge to China Podcast《China: Rise of a Superpower》。
- `xiaoyuehan-hardcore-henren/BV11tVczFExN.chaptered-notes.md`: 小约翰可汗《谁是对苏联破坏力最大的特工？【硬核狠人83】》章节化整理稿。
- `xiaoyuehan-hardcore-henren/BV11tVczFExN.full-content-notes.md`: 同一期视频的完整内容改写稿，按视频顺序覆盖主要叙事和细节。
- `xiaoyuehan-hardcore-henren/BV11tVczFExN.sentence-analysis.md`: 同一期视频的逐句分析索引，按 269 个句级单元给出时间码、内容定位、话语功能和纠错备注。
- `generated/BV11tVczFExN.original-subtitles.md`: 已授权归档的原字幕 Markdown，字幕正文从本地 SRT 原样排版。
- `generated/BV11tVczFExN.chaptered-original-subtitles.md`: 已授权归档的原字幕章节阅读版，不显示字幕编号和时间戳，仅按章节分组。
- `generated/BV11tVczFExN.article-original-subtitles.md`: 已授权归档的原字幕文章阅读版，不显示字幕编号和时间戳，按章节合并为连续段落并仅补入逗号、句号。
- `generated/BV17jTw6REJc.article-original-subtitles.md`: 太吾车神《加盟勇士？詹姆斯到底去哪儿？四大球队最强解析！》原字幕文章阅读版。
- `generated/BV1ujjS6YEK8.article-original-subtitles.md`: 太吾车神《字母哥加盟热火！热火被雄鹿彻底掏空！他们未来还有机会夺冠吗？》原字幕文章阅读版。
- `generated/BV13DjB66Ebw.article-original-subtitles.md`: 太吾车神《杰伦布朗换字母哥？这笔交易行不行？布朗和塔图姆到底谁更强？》原字幕文章阅读版。
- `generated/BV1MZ6iBDENz.article-original-subtitles.md`: 太吾车神《比弗拉格还强？康神克尼普尔到底有多强？为什么他能霸占最佳新秀？》原字幕文章阅读版。
- `generated/BV1YzDTBqECj.article-original-subtitles.md`: 太吾车神《19岁砍50分！弗拉格到底有多强？为什么最佳新秀第一不是他？》原字幕文章阅读版。
- `scripts/format_srt_to_markdown.py`: 本地 SRT 转 Markdown 工具，用于把已有字幕按编号和时间轴排版。

## Local subtitle formatting

```bash
python3 scripts/format_srt_to_markdown.py \
  /Volumes/GT34/Generated/xiaoyuehan-hardcore-henren/BV11tVczFExN/BV11tVczFExN.ai-zh.srt \
  generated/BV11tVczFExN.original-subtitles.md \
  --title "《谁是对苏联破坏力最大的特工？【硬核狠人83】》原字幕"
```
