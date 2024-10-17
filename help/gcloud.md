
## How To Deploy On Google Cloud
<!--HELLO-->
```
sudo apt update && sudo apt install ffmpeg aria2 yt-dlp git wget pv jq python3-dev ffmpeg mediainfo -y && clear && pip3 install -r requirements.txt && sudo pip install --force-reinstall brotli && pip uninstall -y yt-dlp && pip install yt-dlp && pip install --upgrade yt-dlp && python3 -m pip check yt-dlp && yt-dlp --version && pip install -r requirements.txt && clear && python3 modules/main.py
```
<!--
<b><p>After ls If You Got ```app.json  Dockerfile  help  heroku.yml  LICENSE  modules  Procfile  README.md  render.yaml  requirements.txt  text_leech_bot``` Output Then Start</p><b>
-->

## If ~/cloudshell_open/text-leech-bot$ Then Do 

```
sudo apt-get install python3 python3-pip
```


```
pip3 install -r requirements.txt
```

```
sudo apt update
```

```
sudo apt install ffmpeg
```

```
python3 modules/main.py
```

```
find . -type f \( -name "*.session" -o -name "*.pyc" -o -name "*.session-journal" -o -name "*.MP4" -o -name "*.pdf" -o -name "*.mp4" -o -name "*.aria2" -o -name "*.part" \) -delete
find . -type f \( -name "*.MP4" -o -name "*.pdf" -o -name "*.mp4" -o -name "*.aria2" -o -name "*.part" \) -delete
find . -type d \( -name "__pycache__" -o -name "downloads" \) -exec rm -rf {} +
```

## If Rapo Not Clone Then Do This 

```
git clone https://github.com/AshutoshGoswami24/text-leech-bot
```

```
cd text-leech-bot
```

```
pip install -r requirements.txt
```

```
sudo apt update
```

```
sudo apt install ffmpeg
```

```
python3 modules/main.py
