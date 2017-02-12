# svtplay-dl-extra
Personal script to work around (and with) spaam/svtplay-dl

# Dependencies
* [python3](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/)
* pip install requests
* [spaam/svtplay-dl](https://github.com/spaam/svtplay-dl)
* ffmpeg or avconv

# Features
* Enter the name of a show from [svtplay.se](http://svtplay.se) and the scripts will automatically download all available episodes, using a medium quality, and convert them to mp4. Subtitles will also be downloaded.

# Usage
```
./download.sh aventyr-i-tid-och-rum
```

The above command will create a directory `aventyr-i-tid-och-rum/`, download all available episodes from `http://svtplay.se/aventyr-i-tid-och-rum` using a medium quality, download the default subtitles for each episode, and convert `ts` files to `mp4` instead.

If you don't have `ffmpeg` you can modify the code to replace `ffmpeg` with `avconv` instead.

```
ffmpeg -n -i "$CURRENT".ts "$CURRENT".mp4
avconv -n -i "$CURRENT".ts -strict experimental "$CURRENT".mp4
```
