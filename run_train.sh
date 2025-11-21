# python scripts/cv2/extract_speech_tokens.py \
#     --wav_root /lan/ifc/pacofung/uttertune_yue/mdcc/audio/ \
#     --out_dir /lan/ifc/pacofung/uttertune_yue/mdcc/cosy_speech_token/ \
#     --onnx_path pretrained_models/CosyVoice2-0.5B/speech_tokenizer_v2.onnx

# python scripts/cv2/extract_jyutping.py \
#     --corpus_root /lan/ifc/pacofung/uttertune_yue/mdcc/transcript


# python scripts/cv2/prepare_manifest.py \
#     --corpus_root /lan/ifc/pacofung/uttertune_yue/mdcc \
#     --out /lan/ifc/pacofung/uttertune_yue/mdcc/all.tsv

python -m scripts.cv2.train \
    --config configs/train/mdcc.yaml
