# coding=utf-8
import unittest
import time
from public.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

# 这个是优化版执行所有用例并发送报告，分四个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行)

# 获取当前脚本所在的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(caseName="case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在case文件自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:%s"% case_path)
    # 定义discover方法
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的测试用例，并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)
    # 如果这个report文件不存在，自动创建一个
    if not os.path.join(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result.html")
    print("report path:%s"% report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title=u'享骑自动化测试报告，测试结果如下： ',
                            description=u'用例执行情况')
    # 调用add_case函数的返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告文件： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


# def send_mail(sender, psw, receiver, smtpserver, report_file, port):
#     '''第四步：发送最新的测试报告内容'''
#     with open(report_file, "wb") as f:
#         mail_body = f.read()
#     # 定义邮件的内容
#     msg = MIMEMultipart()
#     body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
#     msg['Subject'] = u"自动化测试报告"
#     msg["from"] = sender
#     msg["to"] = ",".join(receiver) # 只能字符串
#     msg.attach(body)
#     # 添加附件
#     att = MIMEText(open(report_file, "wb").read(), "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename= "report.html"'
#     msg.attach(att)
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)    # 连接服务器
#         smtp.login(sender, psw)
#     except:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#         smtp.login(sender, psw)    # 登陆
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()
#     print("test report email has send out!")


if __name__ == "__main__":
    all_case = add_case()  # 加载所有的用例
    # 生成测试报告的路径
    run_case(all_case)   # 执行用例
    # 获取最新的测试报告
    report_path = os.path.join(cur_path, "report")  # 用例文件夹
    report_file = get_report_file(report_path)  # 获取最新的测试报告
    # # 邮箱配置
    # sender = "214256271@qq.com"
    # psw = "zhu199508"
    # smtp_server = "smtp.qq.com"
    # port = 465
    # receiver = "214256271@qq.com"
    # send_mail(sender, psw, receiver, smtp_server, report_file, port) # 发送报告
