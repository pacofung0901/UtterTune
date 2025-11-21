#!/usr/bin/env python3
"""
Join JSUT/JVS transcripts with token paths to final 4-col TSV.
Columns: spk_id <TAB> text <TAB> token.npy <TAB> wav_path
"""

import argparse
import csv
from logging import getLogger, StreamHandler, INFO
from pathlib import Path

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.propagate = False

ap = argparse.ArgumentParser()
ap.add_argument(
    "--corpus_root",
    type=Path,
)
ap.add_argument("--out", type=Path, default=Path("data/manifests/all.tsv"))
args = ap.parse_args()

transcript_path = args.corpus_root / "transcript"
audio_path = args.corpus_root / "audio"
token_path = args.corpus_root / "cosy_speech_token"


rows = []

# mdcc
for spk_id, spkdir in enumerate(sorted(transcript_path.glob("speaker*")), 1):
    txt = spkdir / "trans.txt"

    with txt.open(encoding="utf-8") as f:
        for line in f:

            uid, trans = line.rstrip().split(":")
            tok = token_path / f"{uid}.npy"
            wav = audio_path / spkdir.name / f"{uid}.wav"
            rows.append([spk_id, trans, tok, wav])

args.out.parent.mkdir(parents=True, exist_ok=True)

with args.out.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="	")
    writer.writerows(rows)

print("✓ manifest", args.out, "lines", len(rows))
