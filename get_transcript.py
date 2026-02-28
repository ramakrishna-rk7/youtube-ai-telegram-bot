from youtube_transcript_api import YouTubeTranscriptApi

video_url = "https://www.youtube.com/watch?v=8hly31xKli0"
video_id = video_url.split("v=")[1]

api = YouTubeTranscriptApi()
transcript = api.fetch(video_id)

full_text = " ".join([line.text for line in transcript])

print("Transcript length:", len(full_text))
print("\nFirst 500 characters:\n")
print(full_text[:500])