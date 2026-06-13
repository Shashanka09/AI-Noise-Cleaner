import subprocess
from pathlib import Path


def clean_audio(input_file: str, output_dir: str = "output"):
    Path(output_dir).mkdir(exist_ok=True)

    command = [
        "deepFilter",
        input_file,
        "-o",
        output_dir,
    ]

    subprocess.run(command, check=True)

    print("Noise reduction completed.")

    wav_files = sorted(
        Path(output_dir).glob("*_DeepFilterNet3.wav"),
        key=lambda f: f.stat().st_mtime,
        reverse=True,
    )

    if not wav_files:
        raise FileNotFoundError("No DeepFilterNet output file found.")

    return str(wav_files[0])