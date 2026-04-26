import yt_dlp
import data_center

def process(url):
    ydl_opts = {
        'quiet': True,
        'format': 'best',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return data_center.format_data(info, url)
    except Exception as e:
        return {"error": str(e), "status": "failed"}
      
