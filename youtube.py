import yt_dlp
import data_center

def process(url):
    ydl_opts = {
        'quiet': True,
        'format': 'bestvideo+bestaudio/best',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # Data nikal kar Data Center ko bhejna
            return data_center.format_data(info, url)
    except Exception as e:
        return {"error": str(e), "status": "failed"}
      
