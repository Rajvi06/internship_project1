# File Organizer Web Application

This is a simple web-based file organizer built using Python and Flask. It allows users to enter a folder path, and it will automatically organize the files inside the folder into subdirectories based on file extensions.

## Features

- Organizes files into folders by file extension.
- Simple frontend interface using HTML/CSS and JavaScript.
- Built with Flask backend.
- Cross-platform file management using Python's `pathlib` and `shutil`.

## Requirements

- Python 3.7+
- Flask

## Installation

1. Clone the repository or unzip the downloaded project.
2. Navigate to the project directory.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

5. Open your browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter the full folder path you want to organize in the input box.
- Click "Organize Files".
- Files will be sorted into folders based on their file extensions within the same directory.

## Example

Before:
```
Documents/
├── image.png
├── report.pdf
├── notes.txt
```

After:
```
Documents/
├── png/
│   └── image.png
├── pdf/
│   └── report.pdf
├── txt/
    └── notes.txt
```

## License

This project is free to use and modify for educational purposes.