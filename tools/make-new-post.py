# Quick little script for creating a new post
#   It will create a new post in _posts/, auto-populate it with some basic
#   text, and create a folder in assets/img/posts/
# TOOD: Clean up this mess

# Imports
import argparse
import urllib.parse
import urllib.request
import json
import os               # Finding if folder exists
import datetime         # For parsing date strings
import re               # Regex
import sys              # To exit script on error

from pathlib import Path

# For getting html file and parsing it
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

# Via: https://www.thepythoncode.com/article/get-youtube-data-python
#      https://github.com/x4nth055/pythoncode-tutorials/blob/master/web-scraping/youtube-extractor/extract_video_info.py
def get_video_info(url):
    # init session
    session = HTMLSession()

    # download HTML code
    response = session.get(url)
    # execute Javascript
    response.html.render(timeout=60)
    # create beautiful soup object to parse HTML
    soup = bs(response.html.html, "html.parser")
    # open("index.html", "w").write(response.html.html)
    # initialize the result
    result = {}
    # video title
    result["title"] = soup.find("meta", itemprop="name")['content']
    # video views
    result["views"] = soup.find("meta", itemprop="interactionCount")['content']
    # video description
    result["description"] = soup.find("meta", itemprop="description")['content']
    # date published
    result["date_published"] = soup.find("meta", itemprop="datePublished")['content']
    # get the duration of the video
    result["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text
    # get the video tags
    result["tags"] = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])

    # Additional video and channel information (with help from: https://stackoverflow.com/a/68262735)
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data_json = json.loads(data)
    videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    videoSecondaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']
    # number of likes
    likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] # "No likes" or "###,### likes"
    likes_str = likes_label.split(' ')[0].replace(',','')
    result["likes"] = '0' if likes_str == 'No' else likes_str
    # number of dislikes - YouTube does not publish this anymore...?
    # result["dislikes"] = ''.join([ c for c in text_yt_formatted_strings[1].attrs.get("aria-label") if c.isdigit() ])
    # result["dislikes"] = '0' if result['dislikes'] == '' else result['dislikes']
    result['dislikes'] = 'UNKNOWN'

    # channel details
    channel_tag = soup.find("meta", itemprop="channelId")['content']
    # channel name
    channel_name = soup.find("span", itemprop="author").next.next['content']
    # channel URL
    # channel_url = soup.find("span", itemprop="author").next['href']
    channel_url = f"https://www.youtube.com{channel_tag}"
    # number of subscribers as str
    channel_subscribers = videoSecondaryInfoRenderer['owner']['videoOwnerRenderer']['subscriberCountText']['accessibility']['accessibilityData']['label']
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    return result

# ---- Main part of script ----

# Make sure we are running the script from the correct directory
if not os.path.exists('make-new-post.py'):
    print("ERROR: make-new-post.py is being ran from the wrong location")
    print("       Please cd to tools/ then run the script from there")
    sys.exit()

# Parse arguments
parser = argparse.ArgumentParser(description="Automatically create some basic files for a new blog post")
parser.add_argument('--youtube-link', '-y', type=str,
                    help='Link to the YouTube video that the blog post is based '
                         'upon, will auto-populate a few fields from here')
parser.add_argument('--title', '-t', type=str,
                    help="Title of the article if not using a predefined title "
                         "from YouTube")

args = parser.parse_args()

# Grab title, dates, and text that should be pre-populated based on the argument
#   specified
if not (args.youtube_link or args.title):
    parser.error("ERROR: You must specify either a '-y' YouTube link or a "
                                                  "'-t' custom title for the post")
    sys.exit()  # Probably unnecessary

elif args.youtube_link:
    # For debugging
    # args.youtube_link = 'https://youtu.be/JuFTTGWe_HQ' # tesla swerve
    # args.youtube_link = "https://www.youtube.com/watch?v=Hv6EMd8dlQk" #joma
    # args.youtube_link = "https://youtu.be/ALsLiy4sLIQ" #airpods
    # args.youtube_link = "https://www.youtube.com/watch?v=L2Pp3c7fN3E" #853 likes Renee Ritchie

    # Get video ID from YouTube Link (string parsing)
    print(f"Received YouTube video link: {args.youtube_link}")
    url_parts = urllib.parse.urlparse(args.youtube_link)
    if 'watch' not in url_parts.path:
        # Ex. 'https://youtu.be/xxxxx'
        video_id = url_parts.path.rsplit('/', 1)[-1]
    else:
        # Ex. 'https://www.youtube.com/watch?v=xxxxx'
        video_id = url_parts.query.replace('v=', '')
    print(f"Identified the YouTube video ID as: {video_id}")

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
    date_time_obj = datetime.datetime.strptime(date_published, '%Y-%m-%d')
    date_for_folder = date_time_obj.strftime("%Y-%m-%d")    # YYYY-MM-DD

    title = data['title']

    # Make template post with header
    with open('post_middle_youtube.txt', 'r') as f:
        post_middle = f.read()

    with open('post_ending_youtube.txt', 'r') as f:
        post_ending = f.read()

    finish_post = post_middle + 'https://www.youtube.com/embed/' + video_id + post_ending

elif args.title:
    title=args.title
    date_for_folder = datetime.datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD
    with open('post_title.txt', 'r') as f:
        finish_post = f.read()

    print("Using a custom title for this post: " + title)

else:
    print("ERROR: Something funky's going on with the arguments specified")
    sys.exit()


# By this point, title, date_for_folder, and finish_post should all be set

title_no_space = title.lower().replace(' ', '-')
title_for_folder = ''.join(c for c in title_no_space if c.isalnum() or c == '-')

folder_name = date_for_folder + '-' + title_for_folder
folder_path = '../assets/img/posts/' + folder_name

# Create folder for images
if os.path.exists(folder_path):
    print("WARNING: folder path was already created: " + folder_path)
else:
    os.makedirs(folder_path)
    print("Created folder: " + folder_path)

post_path = '../_posts/' + folder_name + '.md'
print("Creating text post: " + post_path)

# Make sure the post isn't already created before we overwrite it
if os.path.exists(post_path):
    print("ERROR: Text post was already created. ")
    print("       Check to ensure that you do not need the text post, then "
                 "delete it and run this script again for the text post to be "
                 "populated with template text")
    sys.exit()  # Not necessary but safe
else:
    with open(post_path, 'w') as f:
        f.write('---\n')
        f.write('# See defaults in _config.yml\n')
        f.write('title: "' + title + '"\n')
        f.write('author: Matt Popovich\n')
        # -0600 if in summer, -0700 if in winter
        # TODO: Make this automatic?
        f.write('date: ' + date_for_folder + datetime.datetime.now().strftime(" %H:%M:%S") + ' -0700\n')
        f.write(finish_post)

print("Finished successfully!")
