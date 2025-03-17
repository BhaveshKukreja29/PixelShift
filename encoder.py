import subprocess
import os



def convert(input_file, output_file, resolution='480:480'):
    temp_vid = 'temp_videos'
    os.makedirs(temp_vid, exist_ok=True)

    file_path = os.path.join(temp_vid, input_file.name)
    with open(file_path, "wb") as f:
        f.write(input_file.getbuffer())  # Save file to disk

    command = [
        'ffmpeg', '-i', file_path, '-vf', f'scale={resolution}', 'temp_videos/test_480p.mp4'
    ]

    subprocess.run(command, check=True)

