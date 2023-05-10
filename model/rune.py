from model.configs import PROC_CARAC, PROC_CARAC_MAX, DICT_CARAC, DICT_TYPE_RUNES, DICT_PATH_RUNES, \
    DICT_EXTRA, DICT_MEULE_ANTIQUE, QualityType, DICT_MEULE_LEG


class Rune:

    def __init__(self, id, slot, upgrade_current, primary, inate, subs, extra, nb_stars, sell_value, set_id):
        """
        :param id: id of the rune
        :param slot: slot of runes (1,2,3,4,5,6)
        :param upgrade_current: current upgrade of the runes
        :param primary: primary stats
        :param inate: inate stats
        :param subs:  subs stats
        :param extra: Type of rune (purple, rare, legend ..)
        :param nb_stars: number of stars of the rune
        :param set_id Type de la rune (Voliente,amelio, ...)
        """
        self.id = id
        self.slot = slot
        self.upgrade_current = upgrade_current
        self.primary = self.convert_stats(primary)
        self.inate = self.convert_stats(inate)
        self.subs = self.apply_conversion(subs)
        self.extra = self.get_type(extra)
        self.nb_stars = nb_stars
        self.sell_value = sell_value
        self.set_id = DICT_TYPE_RUNES[set_id]
        self.path = DICT_PATH_RUNES[self.set_id][self.slot] + '.png'
        self.grindable = 0
        self.grindable_real = 0
        self.effi_stats = self.get_effi_stats()
        self.effi_real = self.get_effi_real()

    def apply_conversion(self, subs):
        for i in range(0, len(subs)):
            subs[i] = self.convert_stats(subs[i])
        return subs

    def convert_stats(self, liste):
        try:
            liste[0] = DICT_CARAC[liste[0]]
        except KeyError:
            liste = [0, 0]
        finally:
            return liste

    def get_type(self, extra):
        return DICT_EXTRA[int(extra)]

    def get_effi_real(self):
        ratio_start = 0
        ratio_inate = 0
        list_grinds = []
        num_inate = self.inate[1]
        if num_inate != 0:
            denum_inate = PROC_CARAC[self.inate[0]][self.nb_stars % 10][1]
            ratio_inate = num_inate / denum_inate
        for i in range(0, len(self.subs)):
            rune_type = self.subs[i][0]
            meule = self.subs[i][3] if self.subs[i][3] > 0 else 0
            meule_max = DICT_MEULE_ANTIQUE[rune_type] if self.subs[i][3] > 0 else 0
            num = int(self.subs[i][1]) + meule
            start_proc = PROC_CARAC_MAX[rune_type][self.nb_stars % 10][1]
            procs = (PROC_CARAC[rune_type][self.nb_stars % 10][1] * 4)
            denum_start = procs + start_proc + meule_max
            ratio_start += num / denum_start
            # grind
            if meule_max:
                if self.extra in [QualityType.BLANCHE, QualityType.MAGIC, QualityType.RARE, QualityType.HERO, QualityType.LEGEND]:
                    meule_max = DICT_MEULE_LEG[rune_type] if self.subs[i][3] > 0 else 0
                list_grinds.append(meule/meule_max)
        self.grindable = sum([(1/len(list_grinds))*x for x in list_grinds])
        effi = ((8/9) * ratio_start) + ((1/9) * ratio_inate)
        return effi/1.7905240443809867

    def get_effi_stats(self):
        ratio_start = 0
        ratio_inate = 0
        num_inate = self.inate[1]
        if num_inate != 0:
            denum_inate = PROC_CARAC[self.inate[0]][self.nb_stars % 10][1]
            ratio_inate = num_inate / denum_inate
        for i in range(0, len(self.subs)):
            rune_type = self.subs[i][0]
            num = int(self.subs[i][1])
            start_proc = PROC_CARAC_MAX[rune_type][self.nb_stars % 10][1]
            procs = (PROC_CARAC[rune_type][self.nb_stars % 10][1] * 4)
            denum_start = procs + start_proc
            ratio_start += num / denum_start
        effi = ((8/9) * ratio_start) + ((1/9) * ratio_inate)
        return effi/1.6220612672225576

    def get_obvious_proc(self, stats):
        return 0

    def __repr__(self):
        return '{' + 'id : ' + str(self.id) + \
               ', sell_value : ' + str(self.sell_value) +\
               ', efficisty : ' + str(self.effi_stats) + \
               ', set_id : ' + str(self.set_id) + \
               ', extra : ' + str(self.extra) + \
               ', primary : ' + str(self.primary) + \
               ', inate : ' + str(self.inate) + \
               ', subs : ' + str(self.subs) + \
               ', extra : ' + str(self.extra) + \
               '}'
