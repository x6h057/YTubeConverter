from flask import Flask, render_template, request, send_file, jsonify
import source.api as api
import inspect
import os


app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download_file():
    try:
        url = request.form["urlInput"]
        format_type = request.form["format"]
        folder = request.form.get("folder", "temp")
        app.logger.debug(f"Received URL: {url}, Format: {format_type}")

        file = api.download_video(url, format_type, folder)
        app.logger.debug(f"Downloaded file path: {folder}")

        app.logger.debug(f"Downloaded file: {file}")

        return file
    
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 400

def __init__():
    api.cleanup("temp")
    api.auto_cleanup("temp", 30 * 30)

if __name__ == "__main__":
    app.run(debug=True)
