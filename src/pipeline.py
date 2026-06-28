from pathlib import Path

from src.audio_processor import clean_audio
from src.audio_normalizer import normalize_audio


def process_audio(input_file: str) -> str:
    """
    Complete audio processing pipeline.

    Args:
        input_file: Path to the input audio file.

    Returns:
        Path to the final processed audio file.
    """

    # Step 1: AI Noise Reduction
    denoised_file = clean_audio(input_file)

    # Step 2: Generate output filename
    input_path = Path(input_file)

    output_file = (
        Path("output")
        / f"{input_path.stem}_normalized{input_path.suffix}"
    )

    # Step 3: Loudness Normalization
    normalize_audio(denoised_file, str(output_file))

    return str(output_file)