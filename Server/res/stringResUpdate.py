import json


def comment(fp):
    fp.write(
        f'###############################################\n'
        f'# This file is auto gen by stringResUpdate.py #\n'
        f'# DO NOT manual modification if not necessary #\n'
        f'###############################################\n\n\n'
    )


def head(fp):
    fp.write(
        f'class R:\n'
        f'    __lang = "en-US"\n\n'
        f'    @classmethod\n'
        f'    def setLang(cls, lang):\n'
        f'        cls.__lang = lang\n\n'
    )


def body(fp, key, value):
    fp.write(
        f'    @classmethod\n'
        f'    @property\n'
        f'    def {key}(cls):\n'
        f'        return {value}[cls.__lang]\n'
        f'\n'
    )


def update(path='string.json'):
    with open(path) as f, open('string.py', 'w') as fp:
        comment(fp)
        head(fp)
        stringRes = json.load(f)
        for key, value in zip(stringRes.keys(), stringRes.values()):
            body(fp, key, value)


if __name__ == '__main__':
    update()
