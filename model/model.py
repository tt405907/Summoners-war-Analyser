import json
import operator
import pandas as pd
from model.configs import DICT_TYPE_RUNES_NAME, DICT_CARAC_NAME, DICT_PROC_TYPE_NAME
from model.rune import Rune


class Model:

    def __init__(self):
        self.runes = []

    def process_json_file(self, json_path):
        # Loading file
        json_file = None
        try:
            file = open(json_path, encoding="utf8")
            json_file = json.load(file)
        except FileNotFoundError:
            # TODO : Message to user
            print(f"Sorry, the file {json_path} does not exist.")
        runes_from_character = []
        for i in range(len(json_file["unit_list"])):
            runes_from_character += json_file["unit_list"][i]["runes"]
        self.extraction_data_from_runes(json_file["runes"])
        self.extraction_data_from_runes(runes_from_character)

    def extraction_data_from_runes(self, list_runes):
        for i in range(len(list_runes)):
            self.runes.append(Rune(list_runes[i]['rune_id'],
                                   list_runes[i]['slot_no'],
                                   list_runes[i]['upgrade_curr'],
                                   list_runes[i]['pri_eff'],
                                   list_runes[i]['prefix_eff'],
                                   list_runes[i]['sec_eff'],
                                   list_runes[i]['extra'],
                                   list_runes[i]['class'],
                                   list_runes[i]['sell_value'],
                                   list_runes[i]['set_id']))
        self.runes = list(reversed(sorted(self.runes, key=operator.attrgetter("effi_real"))))

    def apply_filter(self, rune_type, efficency, efficency_selection):
        self.runes = list(reversed(sorted(self.runes, key=operator.attrgetter(efficency_selection))))
        res = []
        for rune in self.runes:
            rune_effi = rune.effi_real if efficency_selection == "effi_real" else rune.effi_stats
            if DICT_TYPE_RUNES_NAME[rune.set_id] == rune_type and rune_effi * 100 > float(efficency[:-1]):
                res.append(rune)
            elif rune_type == "All" and rune_effi * 100 > float(efficency[:-1]):
                res.append(rune)
        return res

    def process_power_bi_file(self):
        df = pd.DataFrame(columns=['id', 'slot', 'upgrade_current', 'primary', 'inate', 'sub1', 'sub2', 'sub3', 'sub4',
                                   'rarity', 'nb_stars', 'type', "grind", "effi_stats", "effi_real"])
        index = 0
        for rune in self.runes:
            id_ = rune.id
            slot = rune.slot
            upgrade_current = rune.upgrade_current
            primary = DICT_CARAC_NAME[rune.primary[0]]
            inate = DICT_CARAC_NAME[rune.inate[0]] if rune.inate[0] else None
            sub1 = DICT_CARAC_NAME[rune.subs[0][0]] if len(rune.subs) > 0 else None
            sub2 = DICT_CARAC_NAME[rune.subs[1][0]] if len(rune.subs) > 1 else None
            sub3 = DICT_CARAC_NAME[rune.subs[2][0]] if len(rune.subs) > 2 else None
            sub4 = DICT_CARAC_NAME[rune.subs[3][0]] if len(rune.subs) > 3 else None
            rarity = DICT_PROC_TYPE_NAME[rune.extra]
            nb_stars = rune.nb_stars
            type = DICT_TYPE_RUNES_NAME[rune.set_id]
            grind = int(rune.grindable * 10000)/100
            effi_stats = int(rune.effi_stats * 10000)/100
            effi_real = int(rune.effi_real * 10000)/100
            df.loc[index] = [id_, slot, upgrade_current, primary, inate, sub1, sub2, sub3, sub4,
                             rarity, nb_stars, type, grind, effi_stats, effi_real]
            index +=1
        with open('outputs/power_bi_data.csv', "w") as f:
            df.to_csv(f)
