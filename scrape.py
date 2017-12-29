#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch episode list from svtplay.se
"""

import requests
import sys
import json

if len(sys.argv) > 1:
    urls = sys.argv[1:]

for url in urls:
    urlslash = url.rfind("/") + 1
    series = url[urlslash:]
    #print("name: " + series)

    # Load the HTML from website
    if url.startswith("http"):
        #url = url + '?tab=senast'
        #print("url: " + url)
        html = requests.get(url).text
    # Assume url to svtplay
    else:
        url = "http://svtplay.se/" + url
        html = requests.get(url).text
        # Load the HTML from a local file instead
        # print("file: " + url)
        # fileobject = open(url, "r")
        # html = fileobject.read()
        # fileobject.close()

    # Find the video urls
    lines = html.splitlines()
    #print(len(lines))
    for line in lines:
        line = line.strip()

        # Find the Javascript row which contains the data
        if line.startswith("root['__svtplay'] = "):
            #print("Found the root line.")

            # Find the JSON object within this row
            jsstart = line.find("{")
            jsend = line.rfind("}") + 1
            jsline = line[jsstart:jsend]
            jsobject = json.loads(jsline)
            #print("Got a JSON Object.")

            # Traverse through the JSON object to find the relevant data
            a = jsobject
            b = a["relatedVideoContent"]
            c = b["relatedVideosAccordion"]

            # In the list of related videos, choose the subset "senast sänt"
            for c2 in c:
                if "RELATED_VIDEOS_ACCORDION_SEASON" in c2["type"]:
                    #print("Found the latest.")
                    d = c2["videos"]

            # In the subset of related videos, find a direct url for each video
            videos = []
            for d2 in d:
                video = d2["versions"][0]["contentUrl"]

                # Trim
                if video.find("?") >= 0:
                    video = video[:video.find("?")]

                # Appen url to file
                videos.append(video)
                # Append url to stdout
                print(video)

    # Save result to file.
    with open(series + ".txt", "w+") as newfile:
        newfile.truncate()
        videostr = "\n".join(videos)
        newfile.write(videostr)
