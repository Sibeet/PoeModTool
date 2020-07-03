from mwclient import Site
from enum import Enum
import json

GenerationType = {
    'PREFIX' : 1, 
    'SUFFIX' : 2
}

def get_connection():
    site = Site('pathofexile.gamepedia.com', path='/')
    return site

def get_mod_group_by_type(item_tag, site, domain_type):
    result = site.api(
        'cargoquery',
        tables = 'spawn_weights, mods',
        join_on = 'spawn_weights._pageID = mods._pageID',
        fields = 'mods.mod_group, spawn_weights.tag, mods.generation_type',
        where = F'mods.generation_type = {domain_type} AND spawn_weights.tag = "{item_tag}"',
        group_by = 'mods.mod_group',
        limit = 10000
    )
    return result

def get_armour_list(item_tag, site):
    result = site.api(
            'cargoquery', 
            tables = 'armours, items', 
            join_on = 'armours._pageName = items._pageName', 
            fields = 'name',
            where = F'items.rarity = "normal" AND items.class_id = "{item_tag}"',
            limit = 10000
            )
    
    return result

def get_tag_modifier(item_tag, site):
    prefix_group = get_mod_group_by_type(item_tag, site, GenerationType['PREFIX'])
    suffix_group = get_mod_group_by_type(item_tag, site, GenerationType['SUFFIX'])
    return [prefix_group, suffix_group]


site = get_connection()
armour_list = get_armour_list('gloves', site)
tag_modifier = get_tag_modifier('gloves', site)