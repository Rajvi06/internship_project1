from flask import Flask, render_template, request, jsonify
from organizer.logic import organize_files
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organize', methods=['POST'])
def organize():
    data = request.get_json()
    folder_path = data.get("folderPath")

    if not folder_path:
        return jsonify({"success": False, "message": "Folder path is required"}), 400

    path_obj = Path(folder_path)
    if not path_obj.exists() or not path_obj.is_dir():
        return jsonify({"success": False, "message": "Invalid folder path"}), 400

    moved_count = organize_files(path_obj)
    return jsonify({"success": True, "message": f"{moved_count} files organized."})

if __name__ == '__main__':
    app.run(debug=True)