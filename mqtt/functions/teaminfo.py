teamCode = [
    "03 F4 A9 94",
    "83 96 24 A7",
    "03 0D BF 12",
    "73 CA 7C 94",
    "E3 08 75 94",
    "53 51 AA 94",
    "C3 19 74 94",
    "D3 0D 8B 94",
    "A3 87 73 94",
    "F3 7D F4 A8",
    "C3 29 66 12",
    "33 6D B6 12",
    "F3 5F 08 A7",
    "13 CC 36 A7",
    "43 9A 63 12",
    "E3 37 6C 12",
    "43 6C 6E 12",
    "D3 57 74 12",
    "53 73 B6 12",
    "43 6E 3C A7",
    "33 66 B6 12",
    "83 4D B5 12",
    "E3 72 6E 12",
    "83 A0 77 12",
    "E3 03 B8 12",
    "D3 14 B0 12",
    "A3 C7 AC 12",
    "53 AF 38 A7",
    "13 C0 74 12",
    "F4 08 D7 2B",
    "13 11 D7 2B",
    "D2 97 D7 2B",
    "11 08 D7 2B"

]
teamData = ""


def setInfo(payload):
    global teamData
    if payload != "":
        teamData = payload
        return teamData


def getInfo():

    global teamData
    if teamData == "":
        return None
    else:
        return teamData
