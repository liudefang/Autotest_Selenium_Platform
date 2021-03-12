from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from Product.models import Project as project
# Create your views here.
from requests import post

from Autotest_Selenium_Platform.helper.Http import *
from Autotest_Selenium_Platform.helper.util import *
from Product.models import Browser


class Project:
    @staticmethod

    @post
    # 新建项目
    def create(request):
        try:
            parameter = get_request_body(request)
        except ValueError:
            return JsonResponse.BadRequest("json格式错误!")
        p = project()
        p.creator = request.user.username
        p.name = parameter.get("name", "")
        p.remark = parameter.get("remark", "")
        try:
            p.clean()
        except ValidationError as ve:
            return JsonResponse.BadRequest(','.join(ve.messages))
        p.name = p.name.strip()
        if project.objects.filter(name__exact=p.name):
            return JsonResponse.BadRequest("项目已存在，请修改后重试!")
        try:
            p.save()
        except:
            return JsonResponse.ServerError("服务器发送错误!")
        return JsonResponse.OK()





class Public:
    @staticmethod
    def data(request):
        browsers = Browser.objects.all()
        browsers_re = list()
        for browser in browsers:
            dic = model_to_dict(browsers, ['id', 'name', 'value', 'remark'])
            browsers_re.append(dic)
        result = dict()
        result['browsers'] = browsers_re
        return JsonResponse(200, 'ok', result)

    @staticmethod
    def index(request):
        import datetime
        data = list()
        #projects = project.objects.all()
        today = datetime.datetime.now().strftime('%Y-%m-%d')