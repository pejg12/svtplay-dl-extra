#!/bin/bash

# $1 is the first argument sent to the command.
# If the user wrote:
#   ./download.sh aventyr-i-tid-och-rum
# then
#   $1="aventyr-i-tid-och-rum"

# Create a new directory for this series
# -p means to not complain if the directory already exists
# Enter this series' directory
# Scrape svtplay.se to find all available episodes
mkdir -p "$1" && cd "$1" && ../scrape.py "$1" |

# Loop once for each episode found
    while read ROW
    do
        # Use a prettier filename than svtplay-dl default
        CURRENT=$(basename "$ROW")

        # -S means to download the subtitles
        # -q 800 -Q 200 means to download a bitrate between 600-1000 (medium quality)
        # --stream-priority
        #    dash=mp4 (smallest file size, no conversion necessary)
        #     hds=flv (smaller file size)
        #     hls=ts  (large file size)
        #    http=?
        #    rtmp=?
        # -o is the chosen output filename
        svtplay-dl -S -q 1050 -Q 200 --stream-priority=dash,hds,hls,http,rtmp -o "$CURRENT" http://svtplay.se"$ROW"

        # < /dev/null is necessary so that ffmpeg doesn't try to use the output from previous commands
        # -n assumes "no" on "Do you want to overwrite existing file?"
        # -i is input file
        < /dev/null ffmpeg -n -i "$CURRENT".ts "$CURRENT".mp4

        # Remove the ts file after the conversion to save space
        rm "$CURRENT".ts

        # Copy files to remote server
        # -a archive, keep permissions
        # --progress show progress bar
        #rsync -a --progress "$CURRENT".* username@server:"/path/to/remote/videos/"
    done

