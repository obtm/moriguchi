# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.models import Site, Result, Detail,Book


class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'serch_site', 'request_url',)  # 一覧に出したい項目
    list_display_links = ('id', 'serch_site',)  # 修正リンクでクリックできる項目
admin.site.register(Site, SiteAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'serch_site', 'serch_date','serch_cnt',)  # 一覧に出したい項目
    list_display_links = ('id', 'keyword',)  # 修正リンクでクリックできる項目
admin.site.register(Result, ResultAdmin)


class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'serch_site', 'title',)  # 一覧に出したい項目
    list_display_links = ('id', 'keyword',)  # 修正リンクでクリックできる項目
admin.site.register(Detail, DetailAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目
admin.site.register(Book, BookAdmin)
