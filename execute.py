
from subprocess import check_output
import subprocess
import json
def lambda_handler(event,context):
    try:
        print(event["body-json"])
        p = subprocess.Popen(["echo", event["body-json"] ],stdout=subprocess.PIPE)
        #print(p.stdout.read())
        p1 = subprocess.Popen(["python3", "./colorLyrics.py", ],stdin=p.stdout,stdout=subprocess.PIPE)
        #print(p1.stdout.read())
        stdout,stderr = subprocess.Popen(["./ansi2html.sh","--palette=tango","--bg=dark"],stdin=p1.stdout,stdout=subprocess.PIPE).communicate()
        #return "{\"statusCode\": 200,\"headers\": {}, \"body\": \""+stdout.replace('"','\\"')+"\" }"
        #stdout,stderr = subprocess.call("echo" + event["body-json"] + " | python3 ./colorLyrics.py | ./ansi2html.sh --bg=dark",shell=True).communicate()
        return stdout
    except subprocess.CalledProcessError as e:
        print ("lol")
        print (e)
        print (e.output)

#try:
    #p1 = subprocess.Popen(["python3", "./colorLyrics.py", "./loseYourself", ],stdout=subprocess.PIPE)
    #stdout,stderr = subprocess.Popen(["./ansi2html.sh","--bg=dark"],stdin=p1.stdout,stdout=subprocess.PIPE).communicate()
    #print(stdout)
#except subprocess.CalledProcessError as e:
    #print (e.output)

    #p = Popen(['program', 'arg1'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    #output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    #rc = p.returncode
