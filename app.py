from flask import Flask, request, jsonify, render_template, send_from_directory
import os

# Initialize Flask app
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB max file size

# Route: Serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Upload video
@app.route('/upload', methods=['POST'])
def upload_video():
    title = request.form.get('title', '')
    tags = request.form.get('tags', '')
    video = request.files.get('video')

    if not video:
        return jsonify({"message": "No video file provided!"}), 400

    # Save video
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    return jsonify({"message": "Video uploaded successfully!"})

# Route: Fetch dashboard videos
@app.route('/videos')
def get_videos():
    video_files = os.listdir(UPLOAD_FOLDER)
    return jsonify({"videos": video_files})

# Route: Serve uploaded video files
@app.route('/uploads/<filename>')
def serve_video(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
