# test-data

## Contents

- `worldview-china-podcast/hA7hZjLaN8s.podcast-script.md`: Worldview China 播客文字稿，源视频为 The Bridge to China Podcast《China: Rise of a Superpower》。
- `xiaoyuehan-hardcore-henren/BV11tVczFExN.chaptered-notes.md`: 小约翰可汗《谁是对苏联破坏力最大的特工？【硬核狠人83】》章节化整理稿。
- `xiaoyuehan-hardcore-henren/BV11tVczFExN.full-content-notes.md`: 同一期视频的完整内容改写稿，按视频顺序覆盖主要叙事和细节。
- `xiaoyuehan-hardcore-henren/BV11tVczFExN.sentence-analysis.md`: 同一期视频的逐句分析索引，按 269 个句级单元给出时间码、内容定位、话语功能和纠错备注。
- `generated/BV11tVczFExN.original-subtitles.md`: 已授权归档的原字幕 Markdown，字幕正文从本地 SRT 原样排版。
- `generated/BV11tVczFExN.chaptered-original-subtitles.md`: 已授权归档的原字幕章节阅读版，不显示字幕编号和时间戳，仅按章节分组。
- `scripts/format_srt_to_markdown.py`: 本地 SRT 转 Markdown 工具，用于把已有字幕按编号和时间轴排版。

## Local subtitle formatting

```bash
python3 scripts/format_srt_to_markdown.py \
  /Volumes/GT34/Generated/xiaoyuehan-hardcore-henren/BV11tVczFExN/BV11tVczFExN.ai-zh.srt \
  generated/BV11tVczFExN.original-subtitles.md \
  --title "《谁是对苏联破坏力最大的特工？【硬核狠人83】》原字幕"
```
