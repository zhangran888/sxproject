# author: zhangran
# createTime: 2022/5/11 16:09:10
# describe: 钉钉机器人发送测试报告  未调通


# 获取jenkins构建信息和本次报告地址
import jenkins  # 安装pip install python-jenkins
import json
import urllib3

# jenkins登录地址
jenkins_url = "http://10.88.88.20:8080/"
# 获取jenkins对象
server = jenkins.Jenkins(jenkins_url, username='zhangran', password='123456789')  # Jenkins登录名 ，密码
# job名称
job_name = "job/sx-bank/"  # Jenkins运行任务名称
# job的url地址
job_url = jenkins_url + job_name
# 获取最后一次构建
job_last_build_url = server.get_info(job_name)['lastBuild']['url']
# 报告地址
report_url = job_last_build_url + 'allure'  # 'allure'为我的Jenkins全局工具配置中allure别名



def DingTalkSend():
    # 钉钉推送
    url = 'https://oapi.dingtalk.com/robot/send?access_token=2491588901f6c42862f2216667ef80ab8eb811e0137e8a75ac2ff90a99c0feb7'  # webhook
    con = {"msgtype": "text",
           "text": {
               "content": "自动化脚本执行完成。"
                          "\n测试概述:" +
                          "\n构建地址：\n" + job_url +
                          "\n报告地址：\n" + report_url
           }
           }
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    jd = json.dumps(con)
    jd = bytes(jd, 'utf-8')
    http.request('POST', url, body=jd, headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    DingTalkSend()
