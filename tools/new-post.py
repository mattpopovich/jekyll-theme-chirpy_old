# Quick little script for creating a new post
#   It will create a new post in _posts/, auto-populate it with some basic 
#   text, and create a folder in assets/img/posts/

# Imports
import argparse
import urllib.parse
import urllib.request
import json


parser = argparse.ArgumentParser(description="Automatically create some basic files for a new blog post")
parser.add_argument('--youtube-link', '-y', type=str,
                    help='Link to the YouTube video that the blog post is based '
                         'upon, will auto-populate a few fields from here')

args = parser.parse_args()


# Get video ID from YouTube Link (string parsing)
print("Received YouTube video link: {}".format(args.youtube_link))
url_parts = urllib.parse.urlparse(args.youtube_link)
video_id = url_parts.path.rsplit('/', 1)[-1]
print("Identified the YouTube video ID as: {}".format(video_id))

# Get YouTube video title from video ID
params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_id}
url = "https://www.youtube.com/oembed"
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string

with urllib.request.urlopen(url) as response:
    response_text = response.read()
    data = json.loads(response_text.decode())
    print(data['title'])




