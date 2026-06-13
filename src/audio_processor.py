import subprocess
from pathlib import Path


def clean_audio(input_file: str, output_dir: str = "output"):
    Path(output_dir).mkdir(exist_ok=True)

    cmd = [
        "deepFilter",
        input_file,
        "-o",
        output_dir
    ]

    subprocess.run(cmd, check=True)

    print("Noise reduction completed.")