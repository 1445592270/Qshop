from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from Qshop.settings import BASE_DIR
import os
class MiddleWareTest(MiddlewareMixin):
    def process_request(self,request):
        req_ip=request.META['REMOTE_ADDR']
        if req_ip=='10.10.107.xx':
            return HttpResponse('hello 你被封号了小伙子')
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('i im process_view')
    # def process_exception(self,request,exception):
    #     print('i im process_exception')
    #     print(exception)
    #     return HttpResponse('代码错误<br>%s'%exception)
    #写日志
    # def process_exception(self, request, exception):
    #     print("我是 process_exception")
    #     print(exception)
    #     file = os.path.join(BASE_DIR, 'error.log')
    #     with open(file, "a") as f:
    #         ## 日志
    #         import time
    #         now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         content = "[%s]:%s\n" % (now, str(exception))
    #         ## 写入内容
    #         f.write(content)
    #         ## 写完日志 给boss发送短信/邮件/
    #     ## 发送 异步
    #     # from CeleryTask.tasks import send_email
    #     # params = {
    #     #   "content":"报错了，赶紧解决"
    #     # }
    #     # send_email.delay(params)
    #     return HttpResponse("代码报错了 <br> %s " % exception)

    def process_template_response(self, request, response):

        print("我是 process_temlate_response")
        return response

    def process_response(self,request,response):
        print('im process_response')
        return response
