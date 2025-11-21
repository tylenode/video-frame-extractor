import subprocess
import sys
from pathlib import Path

def extract_frame(input_path, timestamp, output_path):
    cmd = [
        "ffmpeg",
        "-ss", timestamp,
        "-i", input_path,
        "-frames:v", "1",
        "-q:v", "1",          # highest quality for JPEG; ignored for PNG
        output_path
    ]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    input_video = sys.argv[1]
    timestamp = sys.argv[2]
    output_image = sys.argv[3]

    Path(input_video).exists() or sys.exit("Input file not found.")
    extract_frame(input_video, timestamp, output_image)
