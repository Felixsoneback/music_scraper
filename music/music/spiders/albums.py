# -*- coding: utf-8 -*-
import scrapy
import re
#import json


class AlbumsSpider(scrapy.Spider):
    name = 'albums'
    start_urls = ['https://www.billboard.com/charts/year-end/2019/top-billboard-200-albums']

    def parse(self, response):
        """
        :param response: Hemsidan i textformat.
        :return:
        """
        album_list = response.xpath("//div[@class='chart-details__item-list']/article")

        for album in album_list:
            rank = album.xpath("./div/div[@class='ye-chart-item__rank']/text()").get()
            rank = rank.strip()

            album_name = album.xpath("./div/div/div[@class='ye-chart-item__title']/text()").get()
            album_name = album_name.strip()

            artist_name = album.xpath("./div/div/div[@class='ye-chart-item__artist']/text()").get()
            artist_name = artist_name.strip()
            if not artist_name:
                artist_name = album.xpath("./div/div/div[@class='ye-chart-item__artist']/a/text()").get().strip()

            year = album.xpath("./div[1]/@data-date").get()

            yield {
                "rank": rank,
                "album": album_name,
                "artist": artist_name,
                "year": year
            }
"""
            data = {}
            data['album_artist'] = []
            data['album_artist'].append({
                "rank": rank,
                "album": album_name,
                "artist": artist_name,
                "year": year
            })
            with open('albums.json', 'w') as f:
                json.dump(data, f)

            with open('albums2', mode='w', encoding='utf-8') as feedsjson:
                entry = {"rank": rank,
                "album": album_name,
                "artist": artist_name,
                "year": year}
                feeds.append(entry)
                json.dump(feeds, feedsjson)
"""

        current_page = response.request.url

        current_year = re.search(r"\d{4}", current_page)
        current_year = current_year.group()
        current_year = int(current_year)

        next_year = current_year - 1

        next_page = re.sub(f'{current_year}', f'{next_year}', current_page)

        yield response.follow(next_page, self.parse)