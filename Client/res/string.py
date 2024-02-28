###############################################
# This file is auto gen by stringResUpdate.py #
# DO NOT manual modification if not necessary #
###############################################


class R:
    __lang = "en-US"

    @classmethod
    def setLang(cls, lang):
        cls.__lang = lang

    @classmethod
    @property
    def bubble(cls):
        return {'en-US': 'Bubble', 'zh-CN': 'Bubble'}[cls.__lang]

    @classmethod
    @property
    def login(cls):
        return {'en-US': 'Login', 'zh-CN': '登录'}[cls.__lang]

