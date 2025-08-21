from pathlib import Path
import datetime

def export_markdown(summary_text, folder: Path):
    folder.mkdir(parents=True, exist_ok=True)
    fname = folder / f"meeting_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.md"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("# Meeting Summary\n\n")
        f.write(summary_text)
    print(f"📄 Exported to {fname}")
