from poetry_data.data import getData
from drawbot_skia.drawbot import newPage, text, saveImage

poetry = getData("poetry")
fireballs = getData("fireballs")

w, h = 742.5, 1050
newPage(w, h)

result = set();

for poetryVar in poetry:
    # poetryName = poetryVar["text"].split("\n")[0]
    authorName = poetryVar["author"]
    for fireballVar in fireballs:
        if fireballVar["lon"] != None and fireballVar["lat"] != None:
            if fireballVar["date"].date() == poetryVar["date"].date():
                if fireballVar["date"].date() not in result:
                    result.add(fireballVar["date"].date())
                    lon = float(fireballVar["lon"]) * 9
                    lat = float(fireballVar["lat"]) * 9
                    text(authorName, (lat, lon))

saveImage("result.pdf")

w, h = 742.5, 1050
newPage(w, h)
result1 = set()

for poetryVar in poetry:
    poetryName = poetryVar["text"].split("\n")[0]
    for fireballVar in fireballs:
        if fireballVar["lon"] != None and fireballVar["lat"] != None:
            if fireballVar["date"].date() == poetryVar["date"].date():
                if fireballVar["date"].date() not in result1:
                    result1.add(fireballVar["date"].date())
                    lon = float(fireballVar["lon"]) * 9
                    lat = float(fireballVar["lat"]) * 9
                    text(poetryName, (lat, lon))

saveImage("result1.pdf")