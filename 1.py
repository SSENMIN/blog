import subprocess
import requests
import json


def dingtalk_error(txt):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=116cbc87342cdb05b0530d113db3bf19c7f531bd413a8fcd2b9af349a5d44238'
    send_data = {
        "msgtype": "text",
        "text": {
            "content": txt
        }
    }
    req = requests.post(url, json=send_data)
    return req.json()


def trivy(image):
    sh = subprocess.Popen("trivy image -f json -o /root/results.json {}".format(image), shell=True,
                          stdout=subprocess.PIPE)
    out = sh.stdout.readlines()
    return out


image_list = ['h3yun-corp']

for image in image_list:
    trivy(image)

    with open("/root/results.json") as f:
        trivy_dict = json.dumps(f.readlines()[0])

    Vulnerabilities = trivy_dict['trivy_dict']
    for i in Vulnerabilities:
        if i['Severity'] == "High":
            dingtalk_error("trivy is image {} high".format(image))
