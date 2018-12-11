#!/home/simon/anaconda3/bin/python
"""
    author:
    E-mail:
    Date  :
"""

import os
import configparser

CONFIG_FILE = "/home/simon/.config/scripts/theme.ini"


def get_section(config, section):

    """
        Read ini file
    """

    try:
        sec = config.items(section)
    except:
        print("No Section : "+section+" found")
        return None
    return sec


class Theme():
    """
        Theme Class
    """

    sec_Wallp = {}

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        self.sec_Wallp = get_section(config, 'Wallpaper')


    def change_WP(self):
        """
            Change wallpaper
        """

        pwd = None
        for elem in self.sec_Wallp:
            print(elem)
            if elem[0] == 'pwd':
                pwd = elem[1]
                break
        if pwd is None:
            print("No path to Wallpaper found")
            exit(-1)

        os.system("DISPLAY=:0 GSETTINGS_BACKEND=dconf feh --bg-scale\
                        --no-xinerama --randomize "+pwd+"/*")


def main():

    """
        Main function
    """

    theme = Theme()
    theme.change_WP()
    f = open("/home/simon/theme.log","w+")
    f.write("finished")
    f.close()
    
if __name__ == "__main__":
    main()
