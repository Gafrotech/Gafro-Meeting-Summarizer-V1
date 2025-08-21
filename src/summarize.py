import openai

def summarize_transcript(transcript_segments, diarized_segments, config):
    transcript_text = "\n".join([seg["text"] for seg in transcript_segments])

    sections = "\n".join(config["summarizer"]["sections"])
    prompt = f"""
Summarize the meeting. Provide sections:
{sections}

Transcript:
{transcript_text}
"""

    resp = openai.ChatCompletion.create(
        model=config["summarizer"]["model"],
        messages=[{"role": "system", "content": "You are a precise meeting summarizer."},
                  {"role": "user", "content": prompt}]
    )
    return resp["choices"][0]["message"]["content"]
