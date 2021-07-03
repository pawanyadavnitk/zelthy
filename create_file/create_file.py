from datetime import datetime
import os

FILENAME = "/new_file.txt"

def main():
    content = input("Please enter file content: ")

    dirname = datetime.today().strftime("%d_%m_%Y")
    dirname = os.path.expanduser('~/') + dirname
    filename = dirname + FILENAME

    os.makedirs(dirname, exist_ok=True)

    with open(filename, "w") as f:
        f.write(content)
        print(f"File is saved in a directory like: '{filename}'")

if __name__ == "__main__":
    main()
