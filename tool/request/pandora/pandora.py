import urllib.request
import json
import os
import yaml


def get_task()->list:
  proxy_host="10.20.21.21:3128"
  req_url="http://jjh1216:10261/tasks"
  req = urllib.request.Request(req_url)
  req.set_proxy(proxy_host, 'http')
  resp=urllib.request.urlopen(req)
  html = resp.read()
  res=json.loads(html.decode('utf-8'))
  return res



def modify_kafka_offset(tasks,repo,consumer)->bool:
  exist=False
  for task in tasks:
    if task["repo"]==repo:
      config={}
      exist=True
      offsetList=[]
      config["Topic"]=get_topic_from_taskname(task["name"],repo,task["type"])

      if task["parts"]!=None:
        for part in task["parts"]:
          offsetList.append(part["offset"])
      config["Consumer"]=  consumer
      config["Offsets"]=  offsetList
      print(config)
      write_config_yaml(task["type"],config)
  return exist

def write_config_yaml(fileName:str,content:dict):
  curpath = os.path.dirname(os.path.realpath(__file__))
  yamlpath = os.path.join(curpath, fileName+".yaml")
  # 写入到yaml文件
  with open(yamlpath, "w", encoding="utf-8") as f:
      yaml.dump(content, f)

def get_topic_from_taskname(name:str,repo= "",type=""):
  topic=name.strip().removeprefix(type+"-")
  pos=topic.find("-"+repo)
  topic=topic[0:pos]
  return topic


if __name__ == '__main__':
  repo = input("请输入仓库名称：");
  print ("你输入的仓库类型是: ", repo)
  consumer = input("消费者：");
  print ("你输入的消费者是: ", consumer)

  tasks=get_task()
  exist=modify_kafka_offset(tasks,repo,consumer)
  if not exist:
    print("你输入的repo不存在")
  else:
    print("已经写文件")
  pass
