# on ubuntu computer config: https://askubuntu.com/questions/413650/how-to-connect-to-another-computer-through-the-internet-using-ssh
# https://medium.com/@mschirbel/how-to-run-commands-in-windows-and-linux-servers-using-python-46af13cbca29
# https://stackoverflow.com/questions/17137859/paramiko-read-from-standard-output-of-remotely-executed-command

"""
 A specific setup is required to execute this script.
 Two computers were needed to effectively execute the spotlight requests, as operating a spotlight server was taking up
 too much RAM. An SSH login was made to query the server computer from a different computer.
"""

import paramiko

class QueryServer:

    user = "" # your server PC username
    passw = "" # your server PC password
    host = "" # your server PC IP address

    @staticmethod
    def queryServer(command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=QueryServer.host, username=QueryServer.user, password=QueryServer.passw)

        stdin, stdout, stderr = ssh.exec_command(command)
        stdout = stdout.readlines()
        output = ""
        for i in range(len(stdout)):
            output+=stdout[i]
        ssh.close()
        return output

    @staticmethod
    def createCommand(url, text, confidence):
        return "curl "+url+" -H \"Accept: application/json\" \
            --data-urlencode \""+text+"\" \
            --data \"confidence="+str(confidence)+"\" \
            --data \"support=0\""