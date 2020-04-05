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

# �ļ��ϴ����������ļ��ϴ����ο�����Ĺٷ��ĵ�
# https://docs.djangoproject.com/ja/3.0/topics/http/file-uploads/


def handle_uploaded_file(f, img_path):
    with open(img_path, 'wb') as destination:
        # �ڴ��ʹ��ļ���ʱ�򣬷�ֹ�ڴ�ר�ã�����ʹ��chunks����û��ʹ��read
        for chunk in f.chunks():
            destination.write(chunk)


def uploadImg(request):
    """
    ͼƬ�ϴ�
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

        # ���µ�����һ��urls�ַ���  views���Ե���htmlģ��Ҳ���Ե���urls�ַ���
    return render(request, 'hello/uploading.html')
    # return HttpResponsePermanentRedirect("/s/" + code + "/")


# ��������ַ����ǹ̶��洢��һ���ط�img���棬���ܸı�·�������Ƽ�
# from django.shortcuts import render
# from .models import Img
#
#
# def uploadImg(request):
#     """
#     ͼƬ�ϴ�
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
    ͼƬ��ʾ
    :param request:
    :return:
    """
    imgs = Img.objects.all()
    content = {
        'imgs': imgs,
        # ����ǻ�ȡ��ǰʹ�õĶ˿ںŷ���
        'port': request.META['SERVER_PORT'],
        # ����ǻ�ȡ��ǰhost�ķ����������Ѿ������˶˿ں�
        'host': request.get_host(),
    }
    for i in imgs:
        print("qiulongquan_url={}".format(i.img.url))
    return render(request, 'hello/showing.html', content)


