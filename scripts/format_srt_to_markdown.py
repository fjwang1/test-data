#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


TIMING_RE = re.compile(
	r'^(?P<start>\d{2}:\d{2}:\d{2},\d{3})\s+-->\s+(?P<end>\d{2}:\d{2}:\d{2},\d{3})(?P<settings>.*)$'
)


@dataclass(frozen=True)
class SubtitleBlock:
	index: str
	timing: str
	text_lines: list[str]


def parse_srt(path: Path) -> list[SubtitleBlock]:
	raw = path.read_text(encoding='utf-8-sig')
	raw = raw.replace('\r\n', '\n').replace('\r', '\n')
	blocks: list[SubtitleBlock] = []

	for chunk in re.split(r'\n{2,}', raw.strip()):
		lines = chunk.split('\n')
		if len(lines) < 3:
			continue

		index = lines[0]
		timing = lines[1]
		if not TIMING_RE.match(timing):
			continue

		blocks.append(SubtitleBlock(index=index, timing=timing, text_lines=lines[2:]))

	return blocks


def write_markdown(blocks: list[SubtitleBlock], output_path: Path, title: str, source_path: Path) -> None:
	output_path.parent.mkdir(parents=True, exist_ok=True)

	with output_path.open('w', encoding='utf-8', newline='\n') as f:
		f.write(f'# {title}\n\n')
		f.write('> This file was generated from a local SRT file. Subtitle text lines are copied unchanged by this formatter.\n')
		f.write(f'> Source SRT: `{source_path}`\n\n')
		f.write('## Subtitles\n\n')

		for block in blocks:
			f.write(f'### {block.index} | {block.timing}\n\n')
			for line in block.text_lines:
				f.write(f'{line}\n')
			f.write('\n')


def main() -> None:
	parser = argparse.ArgumentParser(
		description='Format an existing local SRT file as Markdown without changing subtitle text lines.'
	)
	parser.add_argument('srt_path', type=Path, help='Input .srt file')
	parser.add_argument('output_path', type=Path, help='Output .md file')
	parser.add_argument('--title', default='Original subtitles', help='Markdown title')
	args = parser.parse_args()

	assert args.srt_path.exists(), f'SRT file not found: {args.srt_path}'
	assert args.srt_path.is_file(), f'SRT path is not a file: {args.srt_path}'

	blocks = parse_srt(args.srt_path)
	assert blocks, f'No valid SRT subtitle blocks found in: {args.srt_path}'

	write_markdown(blocks, args.output_path, args.title, args.srt_path)
	print(f'Wrote {len(blocks)} subtitle blocks to {args.output_path}')


if __name__ == '__main__':
	main()
