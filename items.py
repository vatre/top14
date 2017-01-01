# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Club(scrapy.Item):
    '''
        Identifiant du club
        Correspond au numéro de ligne dans le tableau bilan de la page wikipedia
        sur le championnat français au moment de l'initialisation
    '''
    id = scrapy.Field()
    '''
        Nom du club comme présenté sur sa page wikipedia
    '''
    nom = scrapy.Field()
    '''
        Url de la page wikipedia du club
    '''
    url = scrapy.Field()
