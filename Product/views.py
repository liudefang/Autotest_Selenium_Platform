from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from Product.models import Project
# Create your views here.
from requests import post

from Autotest_Selenium_Platform.helper.Http import *
from Autotest_Selenium_Platform.helper.util import *
from Product.models import Browser


@login_required
def add_project(request):
    """
    新增项目
    :param request:
    :return:
    """
    if request.method == "POST":
        project_name = request.POST.get("project_name")
        project_desc = request.POST.get("project_desc")
        testers = request.POST.get("testers")

        print("project_name:", project_name)

        if len(project_name) != 0 and project_name != str(Project.objects.filter(project_name=project_name).first()):

            Project.objects.create(project_name=project_name, project_desc=project_desc, testers=testers)

            response = {"status": 0, "msg": "添加成功!"}

            # return redirect("/project")
        elif len(project_name) == 0:
            response = {"status": 1, "msg": "项目名称不能为空!"}
        else:
            response = {"status": 2, "msg": "项目名称已存在!"}
        print("response:", response)
        return JsonResponse(response)

    return render(request, "project.html")


@login_required
def del_project(request):
    """
    删除项目
    :param request:
    :return:
    """
    project_ids = request.POST.get("pid")
    project_ids = project_ids.split(',')
    for project_id in project_ids:
        if len(project_id) != 0:
            Project.objects.filter(pid=project_id).delete()

    print("project_ids:", project_ids)
    return render(request, "project.html")

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