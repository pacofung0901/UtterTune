from pathlib import Path
import ToJyutping
from tqdm import tqdm
import argparse
"""
Extract the jyutping of each polyphone and 
Save as a txt per each speaker
"""



def poly2jyut(text):
    candidates = ToJyutping.get_jyutping_candidates(text)


    char = []
    for candidate in candidates:
        word, jyut = candidate[0], candidate[1]
        if len(jyut) > 1:
            char.append('poly')
        elif len(jyut) == 1:
            char.append('mono')
        else:
            char.append('punc')

    start_tokens = "<PHON_START>"
    end_tokens = "<PHON_END>"

    jyutpings = ToJyutping.get_jyutping_list(text)
    final_text = []
    for i, jyutping in enumerate(jyutpings):
        if char[i] == 'poly':
            final_text.append(start_tokens)
            final_text.append(jyutping[1])
            final_text.append(end_tokens)
        elif char[i] == 'mono':
            final_text.append(jyutping[0])
        else:
            final_text.append(jyutping[0]) 

    combined = "".join(final_text)
    result = combined.replace("<PHON_END><PHON_START>", " ")

    return result


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--corpus_root",
        type=Path,
        default=Path("data/corpora"),
        help="folder containing jsut/ and jvs/",
    )
    args = ap.parse_args()

    root_path = Path(args.corpus_root)

    speaker_dirs = [p for p in root_path.iterdir() if p.is_dir()]
    print(f"Speakers found: {len(speaker_dirs)}")

    for speaker_dir in speaker_dirs:
        # Find all .lab files for this speaker
        lab_files = list(speaker_dir.rglob("*.lab"))
        
        results = []
        for lab_file in tqdm(lab_files, desc=f"Processing {speaker_dir.name}"):
            text = lab_file.read_text(encoding="utf-8")
            text_poly = poly2jyut(text)  # your processing function
            results.append(text_poly)
        
        # Save transcriptions to trans.txt inside this speaker folder
        output_path = speaker_dir / "trans.txt"
        with output_path.open("w", encoding="utf-8") as f:
            for lab_file, result in zip(lab_files, results):
                f.write(f"{lab_file.stem}:{result}\n")


