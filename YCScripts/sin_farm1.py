"""Script to farm sins via reincarnation in Your Chronicle

Will only use Slime Jelly farm to graduate. Uses macro recording as reference
"""

from PIL import ImageGrab
import pyautogui as ag
import pygetwindow as gw
from pynput import keyboard

MAIN_TAB = (95, 294)
ACTIVE = (200, 80, 80)
AVAILABLE = (120, 118, 118)
AVAILABLE_UPGRADE = [(115, 115, 115), (120, 120, 120)]
UNAVAILABLE = (82, 82, 82)
EMPTY = (70, 70, 70)
ACTION_TAB = (150, 150, 150)

SLOTH_TAB = (878, 195)
SLOTH_CLOSE = (983, 263)
SLOTH_CLOSE_COLOR = (213, 214, 213)
SLOTH_CLOSE_COLOR_HOVER = (204, 205, 204)
SLOTH_UNAVAILABLE = (41, 41, 41)
SLOTH_AVAILABLE = (54, 54, 54)
SLOTH_REMOVE = (1012, 422)
SLOTH_REMOVE_COLORS = [
    (245, 245, 245), # Regular
    (235, 235, 235), # Regular hover
    (143, 143, 143), # Unavailable
    (138, 138, 138), # Unavailable hover
    (187, 187, 187), # Full capacity
    (180, 180, 180)  # Full capacity hover
]
SLOTH_DUNGEON = (910, 310)
SLOTH_LOOP = (960, 310)
SLOTH_OTHER = (1010, 310)

PARTY_TAB = (94, 320)
PARTY_TOP_SCROLL = (743, 403)
PARTY_REMOVE_5 = (706, 488)
PARTY_SHORTCUT_3 = (200, 351)

RITUAL_TAB = (94, 342)
RITUAL_RANK = (520, 350)
RITUAL_RANK_UNAVAILABLE = (179, 179, 179)
RITUAL_RANK_AVAILABLE = (213, 214, 213)
RITUAL_RANK_AVAILABLE_HOVER = (204, 205, 204)

ROUTINE_TAB = (94, 365)
GREED_TAB = (196, 488)
ENVY_TAB = (192, 533)

DUNGEON_1 = (820, 323)
DUNGEON_2 = (820, 357)
DUNGEON_3 = (820, 400)

REINCARNATE_CONFIRM = [
    (555, 575),
    (555, 606),
    (555, 555)
]
REINCARNATE_CONFIRM_COLOR = (226, 226, 226)

ag.PAUSE = 0.3

def get_pixel(x, y):
    screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    return screenshot.getpixel((0,0))

def enter_dungeon(x, y):
    # Enter dungeon without changing screen
    ag.keyDown('shift')
    ag.leftClick(x, y)
    ag.keyUp('shift')

def rank_up():
    ag.leftClick(RITUAL_TAB)
    ag.leftClick(RITUAL_RANK)
    ag.leftClick(MAIN_TAB)

def sloth(x, y):
    ag.moveTo(x, y)
    ag.press('q')

def activate_screen():
    """Set screen placement and size
    """
    # resize window
    win = gw.getWindowsWithTitle('YourChronicle')[0]
    win.activate()
    win.moveTo(10, 140)
    win.resizeTo(1060, 680)

def clear_sloth():
    # Empty sloth
    if get_pixel(*SLOTH_CLOSE) != SLOTH_CLOSE_COLOR:
        ag.leftClick(*SLOTH_TAB)
    ag.leftClick(*SLOTH_DUNGEON)
    while get_pixel(*SLOTH_REMOVE) in SLOTH_REMOVE_COLORS:
        ag.leftClick(*SLOTH_REMOVE)
    ag.leftClick(*SLOTH_LOOP)
    while get_pixel(*SLOTH_REMOVE) in SLOTH_REMOVE_COLORS:
        ag.leftClick(*SLOTH_REMOVE)
    ag.leftClick(*SLOTH_OTHER)
    while get_pixel(*SLOTH_REMOVE) in SLOTH_REMOVE_COLORS:
        ag.leftClick(*SLOTH_REMOVE)

def typefield(string: str):
    for char in string:
        ag.keyDown(char)
        ag.keyUp(char)

def greed_basic():
    ag.leftClick(ROUTINE_TAB)
    ag.leftClick(GREED_TAB)
    ag.leftClick(883, 324)
    top = 315
    for i in range(18):
        ag.leftClick(852, top + i * 24)
    ag.leftClick(882, 717)
    ag.leftClick(852, top + 16 * 24)
    ag.leftClick(852, top + 17 * 24)
    ag.leftClick(MAIN_TAB)

def slow_click(x, y):
    ag.moveTo(x, y)
    ag.leftClick(x, y)

def setup():
    """Right after reincarnation, set up allies and sloth
    """
    # Set party to slot 3
    ag.leftClick(*PARTY_TAB)
    ag.leftClick(*PARTY_SHORTCUT_3)

    clear_sloth()

    ag.leftClick(*MAIN_TAB)
    ag.leftClick(199, 295)
    print("Setup complete")

def village1():
    """Make a tent and leave alone.
    """
    # Talk to father
    ag.leftClick(561, 364)
    ag.leftClick(561, 364)
    ag.leftClick(561, 364)

    # Farmwork
    slow_click(429, 343)

    slow_click(561, 364)
    ag.leftClick(561, 364)

    # Enter training room 1
    enter_dungeon(818, 321)

    # Go to Village
    ag.leftClick(560, 386)

    # Study in church
    while get_pixel(563, 415) not in AVAILABLE_UPGRADE:
        ag.sleep(1)
    ag.leftClick(563, 415)

    # Unlock 
    ag.leftClick(820, 358)
    enter_dungeon(820, 358)

    # Add tan pelt to sloth
    sloth(429, 303)

    # Rank up
    rank_up()

    # Do 2 more training rooms
    enter_dungeon(820, 401)
    while get_pixel(820, 444) == EMPTY:
        ag.sleep(1)
    ag.leftClick(820, 444)
    enter_dungeon(820, 444)

    print("Picking flowers")

    # Pick flowers with little girl
    slow_click(564, 499)
    slow_click(564, 499)
    ag.moveTo(DUNGEON_1)
    enter_dungeon(*DUNGEON_1)

def village2():
    # Learn Tactics and Permission to go out
    ag.leftClick(565, 359)
    ag.leftClick(565, 359)

    rank_up()
    ag.sleep(10)

    # Thank You
    slow_click(569, 426)

    greed_basic()

    # Start Leatherwork with Old Lady
    print("Starting leatherwork")
    ag.moveTo(560, 512)
    sloth(560, 512)

    # Get to orc
    enter_dungeon(820, 549)
    while get_pixel(820, 582) == EMPTY:
        ag.sleep(1)
    enter_dungeon(820, 582)

    # Craft durable leather
    sloth(430, 305)

    # Remove tan pelt
    slow_click(*SLOTH_REMOVE)

    # Dim Cave
    while get_pixel(820, 626) == EMPTY:
        ag.sleep(1)
    ag.moveTo(820, 626)
    ag.leftClick(820, 626)
    enter_dungeon(820, 626)

    # Get firewood
    ag.leftClick(193, 318)
    sloth(303, 303)
    ag.leftClick(193, 294)

    # Make tent
    sloth(564, 509)
    print("Tent made")

    # Go to Tamer School
    sloth(685, 401)

    rank_up()

    while get_pixel(685, 401) != EMPTY:
        ag.sleep(1)
    print("School chosen")

    # Talk with Father
    slow_click(568, 361)

    # Sloth Pray
    sloth(429, 463)
    slow_click(*SLOTH_REMOVE)

    # Buy purse
    slow_click(561, 383)

    # Don't play with girl
    slow_click(564, 693)
    sloth(561, 730)

    # Leave alone
    while get_pixel(689, 405) != EMPTY:
        ag.sleep(1)
    sloth(691, 363)
    while get_pixel(691, 363) != EMPTY:
        ag.sleep(1)
    print("Left Village alone")

def forest():
    """Go through forest dungeons and go through.
    """
    clear_sloth()
    ag.leftClick(193, 318)
    sloth(434, 301)
    enter_dungeon(*DUNGEON_1)
    while get_pixel(*DUNGEON_2) == EMPTY:
        ag.sleep(1)
    print("Forest 1 Done")
    ag.leftClick(DUNGEON_2)
    enter_dungeon(*DUNGEON_2)
    while get_pixel(*DUNGEON_3) == EMPTY:
        ag.sleep(1)
    print("Forest 2 Done")
    ag.leftClick(DUNGEON_3)
    enter_dungeon(*DUNGEON_3)
    sloth(695, 321)
    while get_pixel(695, 321) != EMPTY:
        ag.sleep(1)
    print("Forest Done")

def academy():
    """Farm slime jelly for rank 39, then graduate.
    """
    ag.leftClick(194, 342)

    # Enroll in a Dormitory
    ag.leftClick(562, 323)

    # Adventurers Guild
    ag.leftClick(559, 385)
    ag.leftClick(559, 445)
    ag.leftClick(559, 445)
    ag.leftClick(559, 445)
    sloth(560, 569)
    sloth(561, 486)

    # Hoarder's House
    while get_pixel(*DUNGEON_1) == EMPTY:
        ag.sleep(1)
    enter_dungeon(*DUNGEON_1)
    while get_pixel(*DUNGEON_2) == EMPTY:
        ag.sleep(1)
    ag.leftClick(DUNGEON_2)
    enter_dungeon(*DUNGEON_2)
    while get_pixel(*DUNGEON_3) == EMPTY:
        ag.sleep(1)
    enter_dungeon(*DUNGEON_3)
    sloth(*DUNGEON_3)
    print("Slime Jellies farmed")

    # School and Instructor
    ag.leftClick(567, 324)
    sloth(567, 324)
    ag.sleep(2)
    ag.leftClick(563, 423)
    sloth(565, 380)

    # Graduate
    while get_pixel(696, 318) == EMPTY:
        ag.sleep(1)
    sloth(696, 318)

    rank_up()

    # Optimize for rank
    ag.leftClick(PARTY_TAB)
    ag.leftClick(PARTY_TOP_SCROLL)
    for i in range(6):
        ag.leftClick(PARTY_REMOVE_5)
    ag.leftClick(360, 518)
    typefield("sacre")
    ag.leftClick(701, 715)
    ag.leftClick(701, 691)
    ag.leftClick(701, 668)
    ag.leftClick(701, 641)
    ag.leftClick(701, 619)
    ag.leftClick(701, 597)

    ag.leftClick(ROUTINE_TAB)
    ag.leftClick(193, 296)
    ag.leftClick(818, 366)
    ag.leftClick(MAIN_TAB)

    print("Rank optimized")

    print("Waiting for graduation")
    while get_pixel(684, 505) != EMPTY:
        ag.sleep(10)
        rank_up()
        ag.moveTo(RITUAL_TAB)

def demon():
    """Beat the Demon King and complete ED1
    """
    while get_pixel(684, 505) != EMPTY:
        ag.sleep(10)
        rank_up()
        ag.moveTo(RITUAL_TAB)
    print("Graduated")

    clear_sloth()
    sloth(566, 387)
    sloth(687, 323)
    ag.leftClick(558, 321)
    sloth(687, 323)
    # Go to Demon Kingdom
    ag.leftClick(193, 368)
    enter_dungeon(*DUNGEON_1)
    while get_pixel(564, 423) == EMPTY:
        ag.sleep(1)
    ag.leftClick(564, 423)
    ag.leftClick(564, 423)
    ag.leftClick(564, 423)
    ag.leftClick(564, 423)
    ag.leftClick(564, 423)
    sloth(686, 321)
    print("ED1 Completed")

def reincarnate():
    rank_up()
    # Spend all keys (only 3/5)
    print("Spending 3/5 keys")
    ag.leftClick(193, 389)
    slow_click(304, 550)
    slow_click(306, 593)
    slow_click(306, 628)
    # Buy all Habit Efficiency+
    print("Spending inspiration")
    ag.moveTo(300, 322)
    typefield('aaaaa')

    # Spend all sins on inspiration+
    print("Spending sins")
    ag.leftClick(188, 413)
    ag.moveTo(307, 360)
    ag.press('a')

    print("Reincarnating")
    ag.leftClick(RITUAL_TAB)
    slow_click(776, 545)
    slow_click(644, 416)
    for confirm in REINCARNATE_CONFIRM:
        print(f"Checking confirm spot {confirm}")
        if get_pixel(*confirm) == REINCARNATE_CONFIRM_COLOR:
            slow_click(*confirm)
            print("Confirmed reincarnation")
    
    while get_pixel(410, 670) != EMPTY:
        ag.sleep(5)
        ag.leftClick(410, 670)
    print("Reincarnated")

def main():
    for i in range(3):
        activate_screen()
        setup()
        village1()
        village2()
        forest()
        academy()
        demon()
        # reincarnate()

if __name__ == "__main__":
    main()