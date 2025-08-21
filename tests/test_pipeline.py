from src.transcribe import transcribe_audio
import yaml

CONFIG = yaml.safe_load(open("config.yaml"))

def test_transcription():
    segments = transcribe_audio("data/sample_meeting.wav", CONFIG)
    assert isinstance(segments, list)
    assert "text" in segments[0]
