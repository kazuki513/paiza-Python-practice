import datetime

year = date.today().year  # 現在の西暦を取得

if year >= 2019:
    era = "令和"
    era_year = year - 2018
elif year >= 1989:
    era = "平成"
    era_year = year - 1988
else:
    era = "昭和"
    era_year = year - 1925

if era_year == 1:
    print(f"{era}元年")
else:
    print(f"{era}{era_year}年")
