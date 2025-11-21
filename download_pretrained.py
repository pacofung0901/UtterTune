from huggingface_hub import snapshot_download

# download lora weight
snapshot_download(
    repo_id="shuheikatoinfo/UtterTune-CosyVoice2-ja-JSUTJVS", 
    local_dir="lora_weights/UtterTune-CosyVoice2-ja-JSUTJVS"
)

# download llm weight
snapshot_download(
    repo_id="FunAudioLLM/CosyVoice2-0.5B", 
    local_dir="pretrained_models/CosyVoice2-0.5B"
)

