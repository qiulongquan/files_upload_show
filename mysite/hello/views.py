# coding=gbk
from .models import Img
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
import random
import string
import os
from django import forms
import datetime

# 文件上传，复数个文件上传，参考下面的官方文档
# https://docs.djangoproject.com/ja/3.0/topics/http/file-uploads/


def handle_uploaded_file(f, img_path):
    with open(img_path, 'wb') as destination:
        # 在传送大文件的时候，防止内存专用，所以使用chunks，而没有使用read
        for chunk in f.chunks():
            destination.write(chunk)


def uploadImg(request):
    """
    图片上传
    :param request:
    :return:
    """
    print("upload file and then show file")
    if request.method == 'POST':
        name = request.FILES.get('img').name
        img_path = os.path.join("media/file", name)

        if os.path.exists(img_path.encode('utf-8')):
            print(str(img_path.encode('utf-8')) + "  exists.")
            return render(request, 'hello/uploading.html')
        else:
            print(str(img_path) + "  no exists.")
            handle_uploaded_file(request.FILES.get('img'), img_path)
            Img(img=os.path.join("file", name), name=name).save()
            print("upload done.")

        # 重新调用了一次urls分发器  views可以调用html模板也可以调用urls分发器
    return render(request, 'hello/uploading.html')
    # return HttpResponsePermanentRedirect("/s/" + code + "/")


# 下面的这种方法是固定存储在一个地方img下面，不能改变路径。不推荐
# from django.shortcuts import render
# from .models import Img
#
#
# def uploadImg(request):
#     """
#     图片上传
#     :param request:
#     :return:
#     """
#     if request.method == 'POST':
#         new_img = Img(
#             img=request.FILES.get('img'),
#             name=request.FILES.get('img').name
#         )
#         new_img.save()
#     return render(request, 'hello/uploading.html')


def showImg(request):
    """
    图片显示
    :param request:
    :return:
    """
    imgs = Img.objects.all()
    content = {
        'imgs': imgs,
        # 这个是获取当前使用的端口号方法
        'port': request.META['SERVER_PORT'],
        # 这个是获取当前host的方法，里面已经包括了端口号
        'host': request.get_host(),
    }
    for i in imgs:
        print("qiulongquan_url={}".format(i.img.url))
    return render(request, 'hello/showing.html', content)


