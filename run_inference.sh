python -m scripts.cv2.infer \
    --base_model pretrained_models/CosyVoice2-0.5B \
    --lora_dir lora_weights/UtterTune-CosyVoice2-ja-JSUTJVS/ \
    --texts "魑魅魍魎が跋扈する。|チミモーリョーがバッコする。|<PHON_START>チ'ミ/モーリョー<PHON_END>が<PHON_START>バ'ッコ<PHON_END>する。" \
    --prompt_wav prompts/wav/common_voice_ja_41758953.wav \
    --prompt_text prompts/trans/common_voice_ja_41758953.txt