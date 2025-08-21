from pyannote.audio import Pipeline

def diarize_audio(audio_file):
    # ⚠️ Replace with your HF token
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token="YOUR_HF_TOKEN")
    diarization = pipeline(audio_file)
    return [(turn.start, turn.end, spk) for turn, spk in diarization.itertracks(yield_label=True)]
