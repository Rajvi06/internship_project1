from pathlib import Path
import shutil

def organize_files(source_dir):
    files_moved = 0

    for item in source_dir.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()
            if not file_extension:
                continue
            dest_folder_name = file_extension[1:] if file_extension.startswith(".") else file_extension
            if not dest_folder_name:
                dest_folder_name = "unknown"
            destination_dir = source_dir / dest_folder_name
            try:
                destination_dir.mkdir(parents=True, exist_ok=True)
                destination_final_path = destination_dir / item.name
                shutil.move(str(item), str(destination_final_path))
                files_moved += 1
            except Exception:
                continue
    return files_moved