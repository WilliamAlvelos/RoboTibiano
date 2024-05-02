import pyautogui as pg 
import time
import keyboard
import constants

def is_battle_empty():
    try:
        location = pg.locateOnScreen("imgs/empty_battle.png", confidence=0.8, region=constants.REGION_BATTLE)
        return True 
    except:
        return False

def go_to_flag(flag, timer):
    if flag == 8:
        pg.press('`');
    print(f'going to flag {flag}')
    print(f'timer {timer}')
    location = pg.locateOnScreen(f'imgs/flag-{flag}.png', confidence=0.8, region=constants.REGION_MAP)
    x, y= pg.center(location)
    pg.moveTo(x, y)
    pg.click()
    pg.sleep(timer)

def check_potions(): 
    if pg.pixelMatchesColor(*constants.POSITION_LIFE_VOID, constants.EMPTY_FIELD, tolerance=20):
        pg.press('l');
    elif pg.pixelMatchesColor(*constants.POSITION_MANA_FULL, constants.EMPTY_FIELD, tolerance=20):
        pg.press('u');
    
    pg.sleep(1);


def check_healing(): 
    if pg.pixelMatchesColor(*constants.POSITION_LIFE_FULL, constants.EMPTY_FIELD, tolerance=20):
        pg.press('f');
    pg.sleep(1);

def check_status(name, delay, x, y, rgb, button_name):
    pg.sleep(delay);
    if pg.pixelMatchesColor(x, y, rgb, tolerance=20):
        pg.press(button_name);

def kill_monsters():
    skillRotation = ['3', '2', '1', '2', '3', '1', '2', '6']

    print("Is battle empty?", is_battle_empty())

    while is_battle_empty():
        print("Luring")
        pg.sleep(2.0);

    print("Kiling monsters")
    while not is_battle_empty():
        pg.press('r');
        for skill in skillRotation:
            if is_battle_empty():
                print("ALL DEAD")
                return True
            else:
                pg.press(skill);
                pg.sleep(2.0);
            

    print("done")
    return True


