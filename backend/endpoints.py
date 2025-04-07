from flask import Flask, request, jsonify
import os
from flask_cors import CORS
from parse import parse_file
from summarize import generate_summary
from dotenv import load_dotenv
app = Flask(__name__)

dotenv_path = "../../.env"
load_dotenv(dotenv_path,override=True)
cors_origin_local = os.getenv('CORS_ORIGIN_LOCAL', 'http://localhost:4000')
cors_origin_docker =os.getenv('CORS_ORIGIN_DOCKER', 'http://chat-summarizer-frontend:4000')
print(cors_origin_docker)
CORS(app, resources={r"/summarize": {"origins": [cors_origin_local, cors_origin_docker]}})

app.config['UPLOAD_FOLDER'] = 'uploads/'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
@app.route('/', methods=['GET'])
def test():
    return jsonify({"message": "Backend is running"})

@app.route("/summarize", methods=["POST"])
def summarize():
    file_path = None
    try:
        # Check if the request contains a file (PDF) or chat (text)
        if 'userfile' in request.files:
            file = request.files['userfile']
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Parse the PDF and generate summary
            document_text = parse_file(file_path)
            summary = generate_summary(document_text)
            print("SUMMARY:", summary)


        elif 'chat' in request.form:
            chat_text = request.form['chat']
            summary = generate_summary(chat_text)

        else:
            return jsonify({"error": "No file or chat input found."}), 400

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    app.run(debug=True)
