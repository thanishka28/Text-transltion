from huggingface_hub import snapshot_download

# Map each language code to the model ID and folder to store it in
models = {
    'hi': 'Helsinki-NLP/opus-mt-en-hi',
    'te': 'Helsinki-NLP/opus-mt-en-te',
    'ta': 'Helsinki-NLP/opus-mt-en-ta',
    'bn': 'Helsinki-NLP/opus-mt-en-bn',
    'ur': 'Helsinki-NLP/opus-mt-en-ur',
    'pa': 'Helsinki-NLP/opus-mt-en-pa',
    'mr': 'Helsinki-NLP/opus-mt-en-mr',
    'gu': 'Helsinki-NLP/opus-mt-en-gu'
}

for lang_code, model_id in models.items():
    local_dir = f"models/en-{lang_code}"
    print(f"📥 Downloading {model_id} to {local_dir}")
    snapshot_download(
        repo_id=model_id,
        local_dir=local_dir,
        local_dir_use_symlinks=False
    )
    print(f"✅ Done: {model_id}")
