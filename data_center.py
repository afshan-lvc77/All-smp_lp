def format_data(raw_info, original_url):
    try:
        title = raw_info.get('title', 'Fast Video Downloader Video')
        thumbnail = raw_info.get('thumbnail', '')
        
        video_formats = []
        audio_formats = []
        
        formats = raw_info.get('formats', [])
        
        for f in formats:
            format_id = str(f.get('format_id', '')).lower()
            ext = f.get('ext', '')
            
            # Watermark wale filter out karna (Moj/TikTok ke liye)
            if 'watermark' in format_id or 'wm' in format_id:
                continue
                
            f_data = {
                "quality": f.get('format_note') or f.get('resolution') or 'unknown',
                "url": f.get('url'),
                "ext": ext,
                "filesize": f.get('filesize') or f.get('filesize_approx') or 'Unknown'
            }
            
            # Agar sirf audio hai
            if f.get('vcodec') == 'none' and f.get('acodec') != 'none':
                audio_formats.append(f_data)
            # Agar video hai
            elif f.get('vcodec') != 'none':
                video_formats.append(f_data)

        # Turant filter karke original link ke saath wapas bhej dena
        return {
            "status": "success",
            "original_url": original_url,
            "title": title,
            "thumbnail": thumbnail,
            "videos": video_formats,
            "audios": audio_formats
        }
        
    except Exception as e:
        return {"error": f"Data process karne mein error: {str(e)}", "status": "failed"}
      
