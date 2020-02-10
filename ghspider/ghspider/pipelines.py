# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests


class GhspiderPipeline(object):
    def process_item(self, item, spider):
        # spider.logger.info(item)
        _headers = {"Authorization": "Token a17fe39bc573227107212bd484346225929aad98"}
        req = requests.post(
            "http://203.156.197.140/api/gh/", json=item, headers=_headers
        )
        if req.status_code == 201:
            spider.logger.info("post ok")
        else:
            spider.logger.error(req.text)

        return item
