from __future__ import unicode_literals

user_input = input("Enter YouTube URL:\n")

print("\nURL entered: " + user_input)


try:
    import youtube_dl
    ydl_opts = {
        'format':'mp4',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([user_input])   
except:
    print('\n\nError.  Could not find the video.')
    import sys
    sys.exit(0)
    
    
print('\n\nVideo download completed.')