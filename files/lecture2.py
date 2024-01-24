from pathlib import Path

def get_number_lines_for_files():
    root_dir = Path(__file__).parent / "files"
    for filepath in root_dir.glob("*.txt"):
        with open(filepath, mode="r") as file:
            num_lines = len(file.readlines())
            print(f"File {filepath} has {num_lines} lines.")
            
if __name__ == "__main__":
    get_number_lines_for_files()