from team.teaminfo import *


blue_team = ""


def set_blue_info(blue_info):
    global blue_team
    blue_team = blue_info


def get_blue_info():
    global blue_team
    for key, value in teamList.items():
        if key == blue_team[:len(blue_team)-1]:
            return value
