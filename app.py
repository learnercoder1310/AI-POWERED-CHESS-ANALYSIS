from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    print("Home route hit")
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    print("Upload route hit")
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            print(f"Saving uploaded file to: {filepath}")
            file.save(filepath)

            # Step 1: Run detection to generate FEN
            subprocess.run(["python", "chess_fen_generator.py", filepath])

            # Step 2: Run Stockfish analysis
            result = subprocess.run(["python", "stockfish_analyzer.py"], capture_output=True, text=True)
            output = result.stdout

            return f"<pre>{output}</pre><br><a href='/'>← Back</a>"

    return render_template('upload.html')

if __name__ == '__main__':
    print("Starting Flask server on http://127.0.0.1:5000 ...")
    app.run(debug=True)
