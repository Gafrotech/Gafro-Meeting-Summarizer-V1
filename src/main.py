import sys, yaml
from pathlib import Path
from transcribe import transcribe_audio
from diarize import diarize_audio
from summarize import summarize_transcript
from export import export_markdown

CONFIG = yaml.safe_load(open("config.yaml"))

def process_meeting(audio_file: str):
    print("[1/4] Diarizing...")
    diarized_segments = diarize_audio(audio_file)

    print("[2/4] Transcribing...")
    transcript = transcribe_audio(audio_file, CONFIG)

    print("[3/4] Summarizing...")
    structured_summary = summarize_transcript(transcript, diarized_segments, CONFIG)

    print("[4/4] Exporting...")
    export_markdown(structured_summary, Path(CONFIG["output"]["folder"]))

    print("✅ Done!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/main.py data/sample_meeting.wav")
        sys.exit(1)
    process_meeting(sys.argv[1])
