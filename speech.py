import whisper
import pandas as pd
from textblob import TextBlob

# Dowload model
model = whisper.load_model("medium", download_root = "./static/assets/models/transcription")
    
def transcripe(path):
    pd.options.display.max_rows = 100
    pd.options.display.max_colwidth = 1000

    # Transcribe Options
    transcribe_options = {'task': 'transcribe', 'language': 'English', 'beam_size': 5, 'best_of': 5}
    
    # Transcribe
    result = model.transcribe(path, **transcribe_options)
    text = result["text"]
    translator = TextBlob(text)
    return str(translator.translate(from_lang='ar', to='en'))

if __name__=="__main__":
    pass
