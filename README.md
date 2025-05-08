# instagram_following-not-follow-back
Check which accounts you follow but they don't follow you back

<h3><b>Prerequsites</b></h3>
<ul>
  <li>User must have Python installed. To install, head to python.org for installation.</li>
  <li>User must have the followers and following data downloaded. If not, refer to the next section.</li>
</ul>

<h3><b>How to download your information</b></h3>
<ol>
  <li>Head to the Instagram accounts centre on either desktop or through the mobile app.</li>
  <li>Press on 'Download your information', then 'Download or transfer information'. Select 'some of your information'.</li>
  <li>Scroll down to the connections section and check the box 'Followers and following'.</li>
  <li>Select 'Download to device'</li>
  <li>Ensure that the format is changed to JSON. Then, create files. </li>
</ol>
<body>Note that this process can take a few hours to finish. Once it is done, refer to your email inbox to retrieve the link to download your information. Alternatively, you can head back to the same page to retrieve your files once download is complete.</body>

<h3><b>How to use the code</b></h3>
<ol>
  <li>Download the relevant ZIP files from the page as well as the main.py file from this repository.</li>
  <li>Unzip the ZIP file by double-clicking it in your file explorer. This should result in a new folder with all the unzipped content from the ZIP file being created in the same directory named 'connections'.</li>
  <li>Enter the followers_and_following file inside the connections folder created and paste your downloaded main.py file inside.</li>
  <li>Open the followers_and_following file using Python installed (If the download was done through python.org, head to your IDLE app and press File > Open file and select the main.py file.</li>
  <li>Finally, run the code and you should get a list of people that you follow but they do not follow you back!</li>
</ol>
