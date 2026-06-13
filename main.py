from src.audio_processor import clean_audio
from src.audio_normalizer import normalize_audio


if __name__ == "__main__":
    denoised_file = clean_audio("input/sample_audio_1.wav")

    normalize_audio(
        denoised_file,
        "output/sample_audio_1_normalized.wav",
    )