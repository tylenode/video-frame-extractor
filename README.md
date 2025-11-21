# Local frame extractor from video
Extract a frame at higher res than screenshot

### Just do this:
1. Download the package manager `uv`
   - `curl -LsSf https://astral.sh/uv/install.sh | sh`
  
2. Put your video in the root directory (or just specify the path to the video)

3. Then run in terminal
    - example: `uv run frame_extractor/src/main.py input.mov 00:00:03.500 frame.png`
    - Your video file = `input.mov`
    - The moment to extract = `00:00:03.500` (HH:MM:SS.MS)
    - The resulting file = `frame.png`
