import platform


def setWP(filename):
    if platform.system() == 'Windows':
        from ctypes import windll
        SPI_SETDESKWALLPAPER = 20
        windll.user32.SystemParametersInfoW(20, 0, "{0}".format(filename), 0)
    elif platform.system() == 'Linux':
        #from SetUbuntuWP import set_gnome_wallpaper as setWPL
        from os import system as sstm
        #sstm("/usr/bin/gsettings set org.gnome.desktop.background picture-uri {0}".format(filename))
        #print("gsettings set org.gnome.desktop.background picture-uri file:{0}".format(filename))
        # sstm("gsettings set org.gnome.desktop.background picture-uri file:{0}".format(filename)) #GNOME
        # sstm("nohup budgie-wm --replace&") #Для Budgie
        # gnome-shell --replace & disown - Обновить рабочий стол. На Budgie не работало.

        # sstm("kquitapp5 plasmashell")
        # sstm(r"kstart5 plasmashell &") #KDE
        # requires https://github.com/RaitaroH/KDE-Terminal-Wallpaper-Changer installed
        sstm("ksetwallpaper {}".format(filename))


if __name__ == '__main__':
    # is_connected()
    print("I'm here")
