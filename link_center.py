import instagram, facebook, youtube, tiktok, moj, x_twitter

def route_link(url):
    url_lower = url.lower()
    
    # Check karke sahi platform ki file ko link bhejna
    if "instagram.com" in url_lower:
        return instagram.process(url)
    elif "facebook.com" in url_lower or "fb.watch" in url_lower:
        return facebook.process(url)
    elif "youtube.com" in url_lower or "youtu.be" in url_lower:
        return youtube.process(url)
    elif "tiktok.com" in url_lower:
        return tiktok.process(url)
    elif "mojapp.in" in url_lower:
        return moj.process(url)
    elif "twitter.com" in url_lower or "x.com" in url_lower:
        return x_twitter.process(url)
    else:
        return {"error": "Yeh platform abhi support nahi karta", "status": "failed"}
      
