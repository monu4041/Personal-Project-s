from pytube import YouTube
def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully!")
    except exception as e:
        print("Error:", str(e))
        
# prompt the user to enter the YouTube video link
video_url = input("Enter the YouTube video URL: ")

#Call the download_video function
download_video(video_url)