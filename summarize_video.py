from youtube_transcript_api import YouTubeTranscriptApi
from openclaw_client import ask_openclaw

video_url = "https://www.youtube.com/watch?v=8hly31xKli0"
video_id = video_url.split("v=")[1]

api = YouTubeTranscriptApi()
transcript = api.fetch(video_id)

full_text = " ".join([line.text for line in transcript])

text_chunk = full_text[:3500]

prompt = f"""
Summarize this YouTube video.

Provide:
• 5 bullet points
• One final takeaway

Transcript:
{text_chunk}
"""

summary = ask_openclaw(prompt)

print("\n===== VIDEO SUMMARY =====\n")
print(summary)