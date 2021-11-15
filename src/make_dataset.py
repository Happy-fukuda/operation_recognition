#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from icrawler.builtin import BingImageCrawler

# Bing用クローラーの生成
bing_crawler =BingImageCrawler(
    downloader_threads=4,           # ダウンローダーのスレッド数
    storage={'root_dir': 'lying'}) # ダウンロード先のディレクトリ名

filters = dict(
    type="photo",
    color='color',)
# クロール（キーワード検索による画像収集）の実行
bing_crawler.crawl(
    keyword="Lying person",   # 検索キーワード（日本語もOK）
     filters=filters,
    max_num=300)                    # ダウンロードする画像の最大枚数
