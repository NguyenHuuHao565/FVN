################################################################################
## BLACK SHORE MAIN MENU
################################################################################

screen main_menu():

    tag menu

    add Solid("#090909")

    text "BLACK\nSHORE":
        xpos 120
        ypos 120

        size 130

        color "#ECE7DF"

    vbox:

        xpos 1450
        ypos 250

        spacing 18

        textbutton "Continue":
            action Continue()

        textbutton "New Case":
            action Start()

        textbutton "Load":
            action ShowMenu("load")

        textbutton "Settings":
            action ShowMenu("preferences")

        textbutton "Exit":
            action Quit(confirm=True)
            
style blackshore_button is default

style blackshore_button_text:
    size 36
    color "#B9B4AD"
    hover_color "#FFFFFF"