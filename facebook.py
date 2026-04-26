import yt_dlp
import data_center

def process(url):
    ydl_opts = {
        'quiet': True,
        'format': 'bestvideo+bestaudio/best',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return data_center.format_data(info, url)
    except Exception as e:
        return {"error": str(e), "status": "failed"}
      
