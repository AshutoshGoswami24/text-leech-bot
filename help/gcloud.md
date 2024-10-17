
## How To Deploy On Google Cloud

<a href="https://www.youtube.com/@AshutoshGoswami24" target="_blank">
       <img src="https://raw.githubusercontent.com/AshutoshGoswami24/Me/refs/heads/main/img/wathconyt.png" alt="Wathconyt" height="100">
</a>

## STEP 1 : ADD ENV

```
nano modules/vars.py
```
# USE : `ctrl + s` : FOR SAVE | `ctrl + x` : FOR EXIT

## STEP 2 : BUITL DOCKERFILE

```
docker build -t text-leech-bot-by-ashu .
```

## STEP 3 : RUN APP
```
docker run -it --rm text-leech-bot-by-ashu

