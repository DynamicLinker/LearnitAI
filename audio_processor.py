import whisper
import os


def transcribe_lecture(audio_path):
    model = whisper.load_model('base', device='cpu')

    if not os.path.exists(audio_path):
        return "No file found"
    
    result = model.transcribe(audio_path)

    return result['text']
