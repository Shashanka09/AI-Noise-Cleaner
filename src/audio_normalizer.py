import subprocess


def normalize_audio(input_file: str, output_file: str):
    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-af",
        "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-y",
        output_file,
    ]

    subprocess.run(command, check=True)

    print(f"Normalized audio saved to: {output_file}")