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

def get_base_list(item_tag, site):
    result = site.api(
        'cargoquery',
        tables = 'armours, items',
        join_on = 'armours._pageName = items._pageName',
        fields = 'name',
        where = F'items.rarity = "normal" AND items.class_id = "{item_tag}"',
        )
    return result

def get_all_tag_group(item_tag_group, site):
    tag_group_json = site.api(
        'cargoquery',
        tables = 'spawn_weights, mods',
        join_on = 'spawn_weights._pageID = mods._pageID',
        fields = 'spawn_weights.tag',
        where = F'mods.generation_type = 1 AND spawn_weights.tag like "%{item_tag_group}%"',
        group_by = 'spawn_weights.tag'
    )

    tag_group_list = []
    for i, val in enumerate(tag_group_json['cargoquery']):
        tag_group_list.append(tag_group_json['cargoquery'][i]['title']['tag'])

    return tag_group_list

def get_mod_group_from_tag(item_tag, site):
    '''
    return list
    0 - prefix mod group
    1 - suffix mod group
    '''

    prefix_mod_group_json = site.api(
        'cargoquery',
        tables = 'spawn_weights, mods',
        join_on = 'spawn_weights._pageID = mods._pageID',
        fields = 'mods.mod_group',
        where = F'mods.generation_type = 1 AND spawn_weights.tag = "{item_tag}"',
        group_by = 'mods.mod_group'
    )
    suffix_mod_group_json = site.api(
        'cargoquery',
        tables = 'spawn_weights, mods',
        join_on = 'spawn_weights._pageID = mods._pageID',
        fields = 'mods.mod_group',
        where = F'mods.generation_type = 2 AND spawn_weights.tag = "{item_tag}"',
        group_by = 'mods.mod_group'
    )

    suffix_mod_group_list = []
    prefix_mod_group_list = []

    for i, val in enumerate(prefix_mod_group_json['cargoquery']):
        prefix_mod_group_list.append(prefix_mod_group_json['cargoquery'][i]['title']['mod group'])

    for i, val in enumerate(suffix_mod_group_json['cargoquery']):
        suffix_mod_group_list.append(suffix_mod_group_json['cargoquery'][i]['title']['mod group'])

    return [prefix_mod_group_list, suffix_mod_group_list]


def get_mod_by_group(tag_group_list, site):
    tag_group_list
    

site = get_connection()