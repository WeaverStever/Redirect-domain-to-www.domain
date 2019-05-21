How to redirect a root domain to the www version.

<b>The problem:</b>
<p>I have a domain from Google, I want to keep the root domain at Google to take advantage of their email redirect functionality, but the www address is hosted on an Appache2 server on DigitalOcean.  I have the www version working by providing the www alias to the Google DNS, but this leave the root domain with no host.</p>

<p>For this solution, the first step is to create a Python2.7 account for <a href="https://cloud.google.com/appengine/docs/standard/python/quickstart">Quickstart for Python App Engine Standard Environment</a>.  If you are using a later version of Python, perhaps these documents will help you adapt this solution to your version.</p> 
