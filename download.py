# In this file, we define download_model
# It runs during container build time to get model weights built into the container

import pathlib
from modelscope.pipelines import pipeline
from huggingface_hub import snapshot_download
import transformers

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    model_dir = pathlib.Path('weights')
    snapshot_download('kabachuha/animov-0.1-modelscope-original-format', repo_type='model', local_dir=model_dir)
    transformers.utils.move_cache()

if __name__ == "__main__":
    download_model()