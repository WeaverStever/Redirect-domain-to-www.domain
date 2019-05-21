How to redirect a root domain to the www version.

<b>The problem:</b>
<p>I have a domain from Google, I want to keep the root domain at Google to take advantage of their email functionality, but the www address is hosted on an Apache2 server elsewhere.  I have the www version working by providing the www alias to the Google DNS, but this leaves the root domain with no host.</p>

<p>Again, my goal is to keep DNS at Gootle, so a Google solution seems appropriate, but an .htaccess 301 redirect does not seem to be an option with Gcloud / App Engine.

<p><b>For this solution,</b> the first step is to create a Python2.7 account for <a href="https://cloud.google.com/appengine/docs/standard/python/quickstart">Quickstart for Python App Engine Standard Environment</a>.  If you are using a later version of Python, perhaps these documents will help you adapt this solution to your version.</p> 

<p>If you followed the Quickstart, you should have a website working at http://[YOUR_PROJECT_ID].appspot.com. Download or clone this GIT.</p>

<p>You will need your Gcloud  [YOUR_PROJECT_ID] (not the entire URL), add the ID to the <b>gae_deploy.sh</b> file in the python27 directory.</p>

<p>In the python27/code directory, edit <b>main.py</b> file and modify https://www.example.com/ to your desired URL. Here is the documentation for the web.py redirect.  http://webpy.org/cookbook/redirect%2Bseeother</p>

<p>You should replace the <b>favicon.ico</b> file with your favicon, I provided a favicon because Gcloud raises an exception if it does not find one.</p>
   
<p>You should now be able to open a terminal in the python27 directory and run the gae_deploy.sh file (sh gae_deploy.sh).  You might have to make the file executable. If it is working, it should start the Gcloud upload process. On completion, your appspot url should be redirecting to your www subdomain.</p>

 <p>Navigate to https://console.cloud.google.com/appengine and select "Settings" in the left menu. Select the tab, "Custom domains".  Follow the instrucions on how to map your root domain to your App Engine host.</p>

  
