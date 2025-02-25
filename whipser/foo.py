# from faster_whisper import WhisperModel
# import json
# from pathlib import Path
# import inspect  # FIXED: Import the full inspect module


from faster_whisper import WhisperModel
from pathlib import Path
import inspect

# Get script directory
filename = inspect.getframeinfo(inspect.currentframe()).filename
here = Path(filename).resolve().parent

# Path to the audio file
audio_file = here / "short while.avi"
print(audio_file)

# Load Whisper Model on GPU (optimized for RTX 4090)
model = WhisperModel("large", device="cuda", compute_type="float16")

# Transcribe the audio
segments, info = model.transcribe(str(audio_file), language="en")

# Convert transcription to .srt format
srt_file = here / "captions.srt"
with open(srt_file, "w", encoding="utf-8") as f:
    for i, segment in enumerate(segments, start=1):
        start = segment.start
        end = segment.end

        # Convert timestamps to SRT format (HH:MM:SS,MS)
        start_time = f"{int(start // 3600):02}:{int((start % 3600) // 60):02}:{int(start % 60):02},{int((start % 1) * 1000):03}"
        end_time = f"{int(end // 3600):02}:{int((end % 3600) // 60):02}:{int(end % 60):02},{int((end % 1) * 1000):03}"

        f.write(f"{i}\n{start_time} --> {end_time}\n{segment.text}\n\n")

print(f"SRT file saved at: {srt_file}")


# import torch
# print(torch.cuda.is_available())  # Should return True
# print(torch.version.cuda)  # Should return 11.8
# print(torch.cuda.get_device_name(0))  # Should print "RTX 4090"

# # Get script directory
# filename = inspect.getframeinfo(inspect.currentframe()).filename  # FIXED
# here = Path(filename).resolve().parent

# # Path to the audio file
# audio_file = here / "short while.avi"
# print(audio_file)

# # Load the Whisper model (optimized for RTX 4090)
# model = WhisperModel("large", device="cuda", compute_type="float16")

# # Transcribe the audio
# segments, info = model.transcribe(str(audio_file), language="en")

# # Collect results
# result = {"text": "", "segments": []}
# for segment in segments:
#     result["segments"].append({
#         "start": segment.start,
#         "end": segment.end,
#         "text": segment.text
#     })
#     result["text"] += segment.text + " "

# # Print the transcription result
# print(json.dumps(result, indent=2, ensure_ascii=False))
