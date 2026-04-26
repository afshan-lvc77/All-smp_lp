import yt_dlp
import data_center

def process(url):
    ydl_opts = {
        'quiet': True,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'user_agent': 'com.zhiliaoapp.musically/2022405040 (Linux; U; Android 10; en_US; SM-G960F; Build/QP1A.190711.020)',
        'referer': 'https://www.tiktok.com/',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return data_center.format_data(info, url)
    except Exception as e:
        return {"error": str(e), "status": "failed"}

