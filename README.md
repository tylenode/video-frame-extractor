# Local video frame extractor
Extract a video frame at higher resolution than screenshotting it.

The motivation is this should be something very simple i.e. no need to download a third-party software or go on a website. We can all do-it-ourselves to keep our data local. This provides a very quick script to do that.

### Just do this:
1. Download the package manager `uv`
   - `curl -LsSf https://astral.sh/uv/install.sh | sh`
  
2. Put your video in the root directory (or just specify the path to the video)

3. Then run in terminal
    - example: `uv run src/main.py input.mov 00:00:03.500 frame.png`
    - Your video file = `input.mov`
    - The moment to extract = `00:00:03.500` (HH:MM:SS.MS)
    - The resulting file = `frame.png`
