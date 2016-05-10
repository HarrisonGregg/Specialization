from apiclient.discovery import build
from .models import Link, Topic


DEVELOPER_KEY = "AIzaSyByq6lPWIbhe-5nLe78IIhCoc072LCXXbg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(q=options['q'],part="id,snippet",maxResults=options['max_results']).execute()


  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
    	videoid = search_result["id"]["videoId"]
    	videotitle = search_result["snippet"]["title"]
    	videourl = "https://www.youtube.com/watch?v=%s" % (videoid) 


    	link = Link(topic = options['topic'], title = videotitle, url = videourl)
    	link.save()
