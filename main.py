from flask import Flask, request, jsonify, render_template # render_template use kiya hai
import link_center
import os

app = Flask(__name__)

# --- INDEX.HTML LOGIC (Home Route) ---
@app.route('/')
def home():
    # Kyunki file 'templates' folder mein hai, Flask ise automatic wahan se utha lega
    return render_template('index.html')

@app.route('/extract', methods=['GET'])
def extract_link():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "No URL provided", "status": "failed"}), 400

    # 1. Jaise hi app se link aaye, turant link_center ko bhej do
    result = link_center.route_link(video_url)

    # 2. Jo bhi data mile (success ya error), app ko wapas bhej do
    if result.get("status") == "failed":
        return jsonify(result), 404
        
    return jsonify(result), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Render ke liye gunicorn use hoga, par local testing ke liye Flask run:
    app.run(host='0.0.0.0', port=port)
    
