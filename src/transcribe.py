import json, subprocess, tempfile
from pathlib import Path

def transcribe_audio(audio_file, config):
    if config.get("mock_mode", False):
        print("⚠️ Using mock transcript (sample_transcript.json)")
        return json.load(open("data/sample_transcript.json"))

    tmpdir = tempfile.mkdtemp()
    subprocess.run([
        "whisper", audio_file,
        "--model", config["asr_model"],
        "--language", config["language"],
        "--output_dir", tmpdir,
        "--output_format", "json"
    ], check=True)

    out_file = Path(tmpdir) / (Path(audio_file).stem + ".json")
    return json.load(open(out_file))["segments"]
