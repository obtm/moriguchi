# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Site(models.Model):
    """検索対象マスタ"""
    id = models.IntegerField('ID', blank=False, default=0,primary_key=True)
    serch_site = models.CharField('検索サイト', max_length=255, blank=True)
    request_url = models.CharField('検索リクエストURL', max_length=255, blank=True)
    def __str__(self):
        return self.serch_site


class Result(models.Model):
    """検索結果サマリ"""
    id = models.IntegerField('ID', blank=False, default=0,primary_key=True)
    keyword = models.CharField('検索ワード', max_length=255, blank=True)
    serch_site = models.CharField('検索サイト', max_length=255, blank=True)
    serch_date = models.DateTimeField('検索実行日')
    serch_cnt = models.IntegerField('検索結果数', blank=True, default=0)

    def __str__(self):
        return self.keyword


class Detail(models.Model):
    """検索結果詳細"""
    result = models.ForeignKey(Result, verbose_name='検索結果サマリ', related_name='details')
    id = models.IntegerField('ID', blank=False, default=0,primary_key=True)
    keyword = models.CharField('検索ワード', max_length=255, blank=True)
    serch_site = models.CharField('検索サイト', max_length=255, blank=True)
    write_user_name = models.CharField('筆者', max_length=255, blank=True)
    title = models.CharField('タイトル', max_length=255, blank=True)
    body = models.TextField('本文', blank=True)
    write_date = models.DateTimeField('作成日')
    fav_cnt = models.IntegerField('お気に入り数', blank=True, default=0)
    buzz_cnt = models.IntegerField('拡散数', blank=True, default=0)
    comment_cnt = models.IntegerField('コメント数', blank=True, default=0)

    def __str__(self):
        return self.keyword

class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name