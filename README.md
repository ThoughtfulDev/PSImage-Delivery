# Invoke-PSImage Delivery (alias: Kira)
	║ K I R A
	╔════════ ╗
	║████████ ║
	║Ð£A†нηΘ†E║
	║████████ ║
	║████████ ║
	║████████ ║
	║████████ ║
	╚════════ 


## What does this do?

**Embed a Powershell base64 encoded Shellcode into an Image  (Invoke-PSImage) an generate a Downloader for this Image. The Downloader will download the Image, extract the Shellcode and run it. Then it will delete itself and show the Image**

## Using

**Tested with Python 3.5 - ONLY WINDOWS SUPPORTED**

Make sure that your Image is at least 720p (so that the payload can fit into the Image).

On Windows install *GOLang* and add it to your path.
```
$ pip install -r requirements.txt
$ python kira.py -img <your_img>
```
Then follow the Instructions of the Script.

# Tools used
[Invoke-PSImage](https://github.com/peewpw/Invoke-PSImage) - *Huge Props to this dude*

[rcedit](https://github.com/electron/rcedit)
