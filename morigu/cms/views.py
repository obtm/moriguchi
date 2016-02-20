# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def serach_list(request):
    """検索結果サマリの一覧"""
    lists = T_search_result.object.all().order_by('id')
    return render(request,
                  'cms/serach_list.html',     # 使用するテンプレート
                  {'lists': lists})         # テンプレートに渡すデータ