
from subprocess import check_output
import subprocess
import json
def lambda_handler(event,context):
    try:
        p = subprocess.Popen(["echo", event["body-json"] ],stdout=subprocess.PIPE)
        p1 = subprocess.Popen(["python3", "./colorLyrics.py", ],stdin=p.stdout,stdout=subprocess.PIPE)
        stdout,stderr = subprocess.Popen(["./ansi2html.sh","--palette=xterm"],stdin=p1.stdout,stdout=subprocess.PIPE).communicate()
        return stdout
    except subprocess.CalledProcessError as e:
        print (e)
        print (e.output)
