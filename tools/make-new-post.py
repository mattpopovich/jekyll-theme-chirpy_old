# Quick little script for creating a new post
#   It will create a new post in _posts/, auto-populate it with some basic 
#   text, and create a folder in assets/img/posts/

# Imports
import argparse
import urllib.parse
import urllib.request
import json
import os               # Finding if folder exists
import datetime         # For parsing date strings

from pathlib import Path

# For getting html file and parsing it
from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

# Via: https://www.thepythoncode.com/article/get-youtube-data-python
def get_video_info(url):
    # init session
    session = HTMLSession()

    # download HTML code
    response = session.get(url)
    # execute Javascript
    response.html.render(sleep=1)
    # create beautiful soup object to parse HTML
    soup = bs(response.html.html, "html.parser")
    # open("index.html", "w").write(response.html.html)
    # initialize the result
    result = {}
    # video title
    result["title"] = soup.find("h1").text.strip()
    # video views (converted to integer)
    result["views"] = int(''.join([ c for c in soup.find("span", attrs={"class": "view-count"}).text if c.isdigit() ]))
    # video description
    result["description"] = soup.find("yt-formatted-string", {"class": "content"}).text
    # date published
    result["date_published"] = soup.find("div", {"id": "date"}).text[1:]
    # get the duration of the video
    result["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text
    # get the video tags
    result["tags"] = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])
    # number of likes
    text_yt_formatted_strings = soup.find_all("yt-formatted-string", {"id": "text", "class": "ytd-toggle-button-renderer"})
    result["likes"] = int(''.join([ c for c in text_yt_formatted_strings[0].attrs.get("aria-label") if c.isdigit() ]))
    result['likes'] = 0 if result['likes'] == '' else result['likes']
    # number of dislikes
    result["dislikes"] = ''.join([ c for c in text_yt_formatted_strings[1].attrs.get("aria-label") if c.isdigit() ])
    result['dislikes'] = 0 if result['dislikes'] == '' else result['dislikes']

    # channel details
    channel_tag = soup.find("yt-formatted-string", {"class": "ytd-channel-name"}).find("a")
    # channel name
    channel_name = channel_tag.text
    # channel URL
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    # number of subscribers as str
    channel_subscribers = soup.find("yt-formatted-string", {"id": "owner-sub-count"}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    return result


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

# Get video's date of publish from HTML
date_published = get_video_info(params['url'])['date_published']
date_time_obj = datetime.datetime.strptime(date_published, '%b %d, %Y')
date_for_folder = date_time_obj.strftime("%Y-%m-%d")    # YYYY-MM-DD



title = data['title']
title_no_space = title.lower().replace(' ', '-')
title_for_folder = ''.join(c for c in title_no_space if c.isalnum() or c == '-')

folder_name = date_for_folder + '-' + title_for_folder
folder_path = '../assets/img/posts/' + folder_name

# Create folder for images
if os.path.exists(folder_path): 
    print("Folder path was already created: " + folder_path)
else:
    os.makedirs(folder_path)
    print("Created folder: " + folder_path)


# Make template post with header
with open('post_middle.txt', 'r') as f:
    post_middle = f.read()

with open('post_ending.txt', 'r') as f:
    post_ending = f.read()

post_path = '../_posts/' + folder_name + '.md'
print("Creating text post: " + post_path)
with open(post_path, 'w') as f:
    f.write('---\n')
    f.write('# See defaults in _config\n')
    f.write('title: "' + title + '"\n')
    f.write('author: Matt Popovich\n')
    f.write('date: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' -0600\n')
    f.write(post_middle)
    f.write('https://www.youtube.com/embed/' + video_id)
    f.write(post_ending)



