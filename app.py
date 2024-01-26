from flask import Flask, request, abort
import os

app = Flask(__name__)

DATA_DIR = '/tmp/data/'

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if not file_name:
        abort(400, "Parameter 'n' is required.")

    file_path = os.path.join(DATA_DIR, f"{file_name}.txt")

    if not os.path.exists(file_path):
        abort(404, "File not found.")

    if line_number:
        try:
            line_number = int(line_number)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if 1 <= line_number <= len(lines):
                    return lines[line_number - 1]
                else:
                    abort(400, "Invalid line number.")
        except ValueError:
            abort(400, "Invalid line number.")
    else:
        with open(file_path, 'r') as file:
            return file.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
