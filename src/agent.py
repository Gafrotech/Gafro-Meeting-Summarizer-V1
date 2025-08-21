from crewai import Agent, Task
from main import process_meeting

class MeetingSummarizerAgent(Agent):
    def __init__(self, config):
        super().__init__(
            name="MeetingSummarizer",
            role="Summarizes meeting audio",
            goal="Generate structured summaries of meeting audio",
            backstory="A diligent AI notetaker that extracts key insights."
        )
        self.config = config

    def run_task(self, audio_file):
        return process_meeting(audio_file)

if __name__ == "__main__":
    import yaml
    config = yaml.safe_load(open("config.yaml"))
    agent = MeetingSummarizerAgent(config)
    task = Task("Summarize meeting", agent=agent)
    task.execute({"audio_file": "data/sample_meeting.wav"})
