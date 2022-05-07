from team.teaminfo import *

red_team = ""
def set_red_info(red_info):
    global red_team
    red_team=red_info


def get_red_info():
  global red_team
  for key, value in teamList.items():
      if key == red_team[:len(red_team)-1]:
          return value