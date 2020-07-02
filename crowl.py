import sys
from selenium import webdriver
from enum import Enum

item = {
    'Onehand' : {
        'Claws' : 'Claw',
        'Daggers' : 'Dagger',
        'Wands' : 'Wand',
        'OneHandSwords' : 'One%20Hand%20Sword',
        'ThrustingOneHandSwords' : 'Thrusting%20One%20Hand%20Sword',
        'OneHandAxes' : 'One%20Hand%20Axe',
        'OneHAndMaces' : 'One%20Hand%20Mace',
        'Sceptres' : 'Sceptre',
        'RuneDaggers' : 'Rune%20Dagger'
    },

    'Twohand' : {
        'Bows' : 'Bow',
        'Staves' : 'Staff',
        'TwoHandSwords' : 'Two%20Hand%20Sword',
        'TwoHAndAxes' : 'Two%20Hand%20Axe',
        'TwoHandMaces' : 'Two%20Hand%20Mace',
        'FishingRods' : 'FishingRod',
        'Warstaves' : 'Warstaff'
    },

    'Flasks' : {
        'LifeFlasks' : 'LifeFlask',
        'ManaFlasks' : 'ManaFlask',
        'HybridFlasks' : 'HybridFlask',
        'UtilityFlasks' : 'UtilityFlask',
        'CriticalUtilityFlasks' : 'UtilityFlaskCritical'
    },

    'Armourstat' : {
        'Str' : 'str_armour',
        'Dex' : 'dex_armour',
        'Int' : 'int_armour',
        'StrDex' : 'str_dex_armour',
        'StrInt' : 'str_int_armour',
        'DexInt' : 'dex_int_armour',
    },

    'Armourcategory' : {
        'Gloves' : 'Gloves',
        'Boots' : 'Boots',
        'BodyArmours' : 'Body_Armour',
        'Helmets' : 'Helmet',
        'Shields' : 'Shield'
    },

    'Jewellery' :{
        'Amulets' : 'Amulet',
        'Rings' : 'Ring',
        'UnsetRing' : 'Ring&an=unset_ring',
        'Belts' : 'Belt'
    },

    'Jewel' : {
        'Crimson' : 'Crimson+Jewel',
        'Viridian' : 'Viridian+Jewel',
        'Cobalt' : 'Cobalt+Jewel',
        'Prismatic' : 'Prismatic+Jewel',
        'MurderousEye' : 'Murderous+Eye+Jewel',
        'SearchingEye' : 'Searching+Eye+Jewel',
        'HypnoticEye' : 'Hypnotic+Eye+Jewel',
        'GhastlyEye' : 'Ghastly+Eye+Jewel',
        'Timeless' : 'Timeless+Jewel',
        'LargeCluster' : 'Large+Cluster+Jewel',
        'MediumCluster' : 'Medium+Cluster+Jewel',
        'SmallCluster' : 'Small+Cluster+Jewel'
    }
}

def get_connection():
    chromedriver = "./chromedriver.exe"

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('disable-gpu')

    driver = webdriver.Chrome(chromedriver, options=option)
    return driver

def get_modifier(driver, item_category, item_type, item_stat):
    if item_category == 'Armours':
        driver.get(F'https://poedb.tw/us/mod.php?cn={item["Armourcategory"][item_type]}&an={item["Armourstat"][item_stat]}')
    elif item_category == 'Jewel':
        driver.get(F'https://poedb.tw/us/mod.php?cn=BaseItemTypes&an={item["Jewel"][item_type]}')
    else:
        driver.get(F'https://poedb.tw/us/mod.php?cn={item[item_category][item_type]}')

    return 0

driver = get_connection()
canvas = get_modifier(driver, 'Armours', 'Gloves', 'Dex')