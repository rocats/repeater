import opencc

converter = opencc.OpenCC("t2s.json")
print(converter.convert("漢字"))  # 漢字
