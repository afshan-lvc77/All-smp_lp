import yt_dlp
import data_center

def process(url):
    # Moj ke liye special options: watermark hatane aur mobile user agent ke liye
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'best[format_id!*=watermark][format_id!*=wm]/best',
        'user_agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
        'referer': 'https://mojapp.in/',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # Data nikal kar Data Center ko bhejna (Legacy link ke saath)
            return data_center.format_data(info, url)
    except Exception as e:
        return {"error": f"Moj extraction error: {str(e)}", "status": "failed"}
      
