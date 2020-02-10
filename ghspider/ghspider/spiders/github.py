# -*- coding: utf-8 -*-
import json
from urllib import parse

import requests
import scrapy
from w3lib.http import basic_auth_header
from scrapy.utils.project import get_project_settings


def process_url(value) -> str:
    if isinstance(value, str):
        o = parse.urlparse(value)
    else:
        raise
    return f"{o.scheme}://{o.netloc}{o.path}"


class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]

    def __init__(self, *args, **kwargs):
        self.since = kwargs.get("since", 0)
        settings = get_project_settings()
        self.username = settings.get("GITHUB_USERNAME")
        self.password = settings.get("GITHUB_PASSWD")
        self.auth = basic_auth_header(self.username, self.password)
        super().__init__(*args, **kwargs)

    def start_requests(self):
        # _urls = []
        _start_url = "https://api.github.com/users"
        if int(self.since) > 0:
            _start_url = f"{_start_url}?since={self.since}"
        self.start_urls.append(_start_url)
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True)

    def parse(self, response):
        data = json.loads(response.text)
        for row in data:
            _url = row["url"]
            if row["type"].lower() == "user":
                yield scrapy.Request(
                    _url, callback=self.parse_user, headers={"Authorization": self.auth}
                )
        last = data[-1]
        self.since = last["id"]
        next_url = process_url(response.url)
        next_url = f"{next_url}?since={self.since}"
        self.logger.info(next_url)
        yield scrapy.Request(
            next_url, callback=self.parse, headers={"Authorization": self.auth}
        )

    def parse_user(self, response):
        r = dict()
        data = json.loads(response.text)

        if data["followers"] >= 15:
            key_url = f"{response.url}/keys"
            req = requests.get(key_url, auth=(self.username, self.password))
            res = req.json()
            if len(res) >= 1:
                valid_key = True
            else:
                valid_key = False

            r.update(
                {
                    "login": data["login"],
                    "name": data["name"],
                    "followers": data["followers"],
                    "email": data["email"],
                    "company": data["company"],
                    "location": data["location"],
                    "gh_url": data["url"],
                    "has_key": valid_key,
                    "created_at": data["created_at"],
                }
            )
            return r
