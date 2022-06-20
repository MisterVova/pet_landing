class Node:
    def __init__(self, key, parent):
        self.key = key
        self.child_dict = dict()
        self.child_list = dict()
        self.parent = parent
        self.is_list = False
        self.value = None

    def is_list(self):
        return self.is_list_key(self.key)

    @staticmethod
    def is_list_key(key):
        if f"{key}" == "":
            return True

        if f"{key}".isdigit():
            return True

        if "[" in key:
            return True

        return False

    @staticmethod
    def get_key_from_list_key(key):
        return f"{key}".replace("[", "").replace("]", "")

    def add_value(self, lst_key: list, value):
        if len(lst_key) == 0:
            self.value = value
            return

        key = lst_key.pop(0)
        child = self.get_child_by_key(key=key)
        child.add_value(lst_key, value)

    def get_child_by_key(self, key):
        if self.is_list_key(key):
            self.is_list = True

        if not self.is_list_key(key):
            if not (key in self.child_dict.keys()):
                self.child_dict[key] = Node(key=key, parent=self)
            return self.child_dict[key]

        key_l = self.get_key_from_list_key(key)

        if not key_l:
            key_l = len(self.child_list)

        if not f"{key_l}".isdigit():
            return self.get_child_by_key(key_l)

        key_l = int(f"{key_l}")
        if not (key_l in self.child_list.keys()):
            self.child_list[key_l] = Node(key=key_l, parent=self)
        return self.child_list[key_l]

    def get_dict(self):
        if (len(self.child_dict) + len(self.child_list)) == 0:
            return self.value
        dct = {}
        lst = []

        if len(self.child_list) != 0:
            keys = [*self.child_list.keys()]
            keys.sort()
            for k in keys:
                lst.append(self.child_list[k].get_dict())

        if len(self.child_dict) != 0:
            keys = [*self.child_dict.keys()]
            keys.sort()
            for k in keys:
                dct.update({k: self.child_dict[k].get_dict()})

        ret = dict()

        if self.value != None:
            ret["value"] = self.value

        if (len(ret) != 0) or (len(dct) * len(lst)) != 0:
            ret["MIX"] = True
            if len(dct):
                ret["dct"] = dct
            if len(lst):
                ret["lst"] = lst

        else:
            if len(dct):
                ret = dct
            if len(lst):
                ret = lst

        # rett = {
        #     "key": self.key,
        #     "dct_s": len(self.child_dict),
        #     "lst_s": len(self.child_list),
        #     "is_list": self.is_list,
        #     "dct": dct,
        #     "lst": lst,
        #     "value": self.value,
        #     "ret": ret
        # }
        return ret
