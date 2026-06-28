import sys

from src.pipeline import process_audio


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    final_output = process_audio(input_file)

    print(f"\nProcessing completed!")
    print(f"Output: {final_output}")


if __name__ == "__main__":
    main()