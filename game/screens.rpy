# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        background Image("gui/ui/MainMenu.png")

    # The main menu buttons.
        xalign 0.0
        yalign 0.0

        imagebutton auto "gui/mm/start_%s.png" xpos 1391 ypos 40 focus_mask True action Start()
        imagebutton auto "gui/mm/load_%s.png" xpos 1391 ypos 215 focus_mask True action ShowMenu("load")
        imagebutton auto "gui/mm/prefs_%s.png" xpos 1391 ypos 390 focus_mask True action ShowMenu('preferences')
        imagebutton auto "gui/mm/help_%s.png" xpos 1391 ypos 565 focus_mask True action ShowMenu ("help")
        imagebutton auto "gui/mm/quit_%s.png" xpos 1391 ypos 740 focus_mask True action Quit(confirm=True)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.


    # The various buttons.

    hbox:
        style_group "navigation"

        xalign 0
        yalign 1.0

        imagebutton auto "gui/nv/rtn_%s.png" xpos 1494 ypos -891 focus_mask True action Return()
        imagebutton auto "gui/nv/prefs_%s.png" xpos 1193 ypos -763 focus_mask True action ShowMenu('preferences')
        imagebutton auto "gui/nv/save_%s.png" xpos 892 ypos -635 focus_mask True action ShowMenu('save')
        imagebutton auto "gui/nv/load_%s.png" xpos 591 ypos -507 focus_mask True action ShowMenu("load")
        imagebutton auto "gui/nv/mm_%s.png" xpos 290 ypos -379 focus_mask True action MainMenu()
        imagebutton auto "gui/nv/help_%s.png" xpos -11 ypos -251 focus_mask True action ShowMenu ("help")
        imagebutton auto "gui/nv/quit_%s.png" xpos -312 ypos -123 focus_mask True action Quit(confirm=True)



init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    add "gui/ui/SaveScreen.png" xalign 1.0 yalign 1.0

        # The buttons at the top allow the user to pick a
        # page of files.
    
    $ firstNum = 1379

    imagebutton auto "gui/sv/auto_%s.png" xpos 735 ypos 20 focus_mask True action FilePage("auto")
    imagebutton auto "gui/sv/quick_%s.png" xpos 896 ypos 20 focus_mask True action FilePage("quick")
    imagebutton auto "gui/sv/prev_%s.png" xpos 1057 ypos 20 focus_mask True action FilePagePrevious()
    imagebutton auto "gui/sv/next_%s.png" xpos 1218 ypos 20 focus_mask True action FilePageNext()

    for i in range(1, 10):
        imagebutton auto "gui/sv/" + str(i) +"_%s.png":
            xpos (int(firstNum)+((i-1)*59)) 
            ypos 20 
            focus_mask True 
            action FilePage(i)

    $ columns = 2
    $ rows = 6

        # Display a grid of file slots.
    grid columns rows:
        xalign 0
        yalign 0
        xsize 1760
        ysize 750
        xpos 68
        ypos 139

        xfill True

        style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
        for i in range(1, columns * rows + 1):

                # Each file slot is a button.
            button:
                action FileAction(i)

                xfill True

                xalign 0
                yalign 0
                xsize 673
                ysize 102
                xpos ((i*15)*(i%2))+((45+(i*15))*((i+1)%2))
                ypos (i-((i+1)%2))*14

                background Frame("gui/sv/SlotBG_idle.png", 4, 4, 4, 4)
                idle_background Frame("gui/sv/SlotBG_hover.png", 4, 4, 4, 4)
                hover_background Frame("gui/sv/SlotBG_idle.png", 4, 4, 4, 4)

                has hbox

                add FileScreenshot(i)

                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("Empty Slot."))
                $ save_name = FileSaveName(i)

                text "[file_name]. [file_time!t]\n[save_name!t]"

                key "save_delete" action FileDelete(i)

### Menu Buttons For Save Screen ###

    imagebutton auto "gui/nv/mm_%s.png" xpos 1260 ypos 969 focus_mask True action MainMenu()
    imagebutton auto "gui/nv/rtn_%s.png" xpos 1571 ypos 969 focus_mask True action Return()



screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker

    hbox:
        xpos 20
        ypos 10
        
        text "SAVE GAME" font "LSANS.ttf" size 64 color "000000ff"

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker

    hbox:
        xpos 20
        ypos 10
        
        text "LOAD GAME" font "LSANS.ttf" size 64 color "000000ff"

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

##############################################################################
# In Game Menus
#
# This screens sets the Menu layout for Help and Preferences.
# By: Jonathan Oakes (Darth62969, TheWired)

screen InGameMenu ():

#Use the Menu Screen background
    add "gui/ui/MenuScreen.png" xalign 1.0 yalign 1.0
    
# Include the navigation.
    use navigation  
 
##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    
# Include the InGameMenu
    use InGameMenu

# Window Title    
    hbox:
        xpos 100
        ypos 10
        
        text "PREFERENCES" size 64 color "000000ff"

 # Preferances Menu
    viewport id "pref_vp":
        draggable True
        mousewheel True
        xalign 0
        yalign 0
        child_size (1050, 6000)
        xsize 1050
        ysize 828
        xpos 125
        ypos 125
        
        
        grid 1 1:
            style_group "pref"
            xfill True


            vbox:
                spacing 20
                frame:
                    hbox:
                        style_group "pref_left"
                        text "Display" 
                    hbox:
                        style_group "pref_right"
                        xpos 475
                        textbutton _("Window"):

                            action Preference("display", "window")

                        textbutton _("Fullscreen"):

                            action Preference("display", "fullscreen")
                frame:
                    hbox:
                        style_group "pref_left"
                        text "Transitions"
                    hbox:
                        style_group "pref_right"
                        xpos 475
                        textbutton _("All") action Preference("transitions", "all")
                        textbutton _("None") action Preference("transitions", "none")

                frame:
                    hbox:
                        style_group "pref_left"
                        text "Text Speed"
                    hbox:
                        style_group "pref_right"
                        xpos 500
                        bar value Preference("text speed")
    
                frame:
                    hbox:
                        style_group "pref_right"
                        xpos 475
                        textbutton _("Joystick...") action Preference("joystick")
    
                frame:
                    hbox:
                        style_group "pref_left"
                        text "Skip"
                    hbox:
                        style_group "pref_right"
                        xpos 475
                        textbutton _("Seen Messages") action Preference("skip", "seen")
                        textbutton _("All Messages") action Preference("skip", "all")

                frame:
                    hbox:
                        style_group "pref_right"
                        xpos 475
                        textbutton _("Begin Skipping") action Skip()
    
                frame:
                    hbox:
                        style_group "pref_left"
                        text "After Choices"
                    hbox:
                        style_group "pref_right"
                        xpos 475
                        textbutton _("Stop Skipping") action Preference("after choices", "stop")
                        textbutton _("Keep Skipping") action Preference("after choices", "skip")
    
                frame:
                    hbox:
                        style_group "pref_left"
                        text "Auto-Forward Time"
                    hbox:
                        style_group "pref_right"
                        xpos 475
                        spacing 25
                        textbutton _("Wait for Voice"):
                            action Preference("wait for voice", "toggle")
                        bar:
                            value Preference("auto-forward time") 
                            xsize 225
                            yalign 0.5

                frame:
                    hbox:
                        style_group "pref_left"
                        text "Music Volume"
                    hbox:
                        style_group "pref_right"
                        xpos 500
                        bar value Preference("music volume")
    
                frame:
                    hbox:
                        style_group "pref_left"
                        text "Sound Volume"
                    hbox:
                        style_group "pref_right"
                        xpos 500    
                        bar value Preference("sound volume")
                        if config.sample_sound:
                            textbutton _("Test"):
                                action Play("sound", config.sample_sound)
                                style "soundtest_button"
    
                if config.has_voice:
                    frame:
                        hbox:
                            style_group "pref_left"
                            text "Voice Volume"
                        hbox:
                            style_group "pref_right"
                            xpos 475
                            bar value Preference("voice volume")
    
                            textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                            if config.sample_voice:
                                textbutton _("Test"):
                                    action Play("voice", config.sample_voice)
                                    style "soundtest_button"

    vbar:
        value YScrollValue("pref_vp")
        
        left_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        right_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        
        left_gutter 0
        right_gutter 0
        bottom_gutter 0
        top_gutter 0
        
        thumb_offset 0
        
        thumb Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        thumb_shadow Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        
        bar_resizing False
        
        xsize 10
        ysize 878
        xpos 101
        ypos 100

init -2:
    style pref_frame:

        background Frame("gui/ui/FrameBox.png", 2, 2, 2, 2)
        xfill True
        ysize 100
        xsize 1050

    style pref_left_hbox:
        xpos 20
        yalign 0.5
    style pref_left_button:
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        left_margin 25
        xalign 0
        xfill True
        xsize 250
        ysize 50
    style pref_left_text:
        color "000000ff"

    style pref_right_hbox:
        yalign 0.5
    style pref_right_button:
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        left_margin 25
        xalign 0
        xfill True
        xsize 250
        ysize 50
    style pref_right_slider:
        left_bar Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        right_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        left_gutter 0
        right_gutter 0
        bottom_gutter 0
        top_gutter 0
        thumb_offset 0
        thumb Image("gui/ui/SliderThing.png")
        thumb_shadow Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        xsize 470

    style pref_hbox:
        xfill True
        
        xsize 1030

        yalign 0.5
        
    style pref_vbox:
        xfill True

    style pref_lable:

        yalign 0.5

    style soundtest_button:
        xalign 1.0

##############################################################################
# Help
#
# Screen that allows the user to view the help menu and credits.
# By: Jonathan Oakes (Darth62969, TheWired)

 
screen help ():
    
    tag menu
    
# Include the InGameMenu
    use InGameMenu


# Window Title    
    hbox:
        xpos 100
        ypos 10
        
        text "HELP" size 64 color "000000ff"
# Help Window    
    viewport id "help_vp":
        draggable True
        mousewheel True
        child_size (1050, 6000)
        xalign 0
        yalign 0
        xsize 1050
        ysize 828
        xpos 125
        ypos 125
        
        
        grid 1 1:
            style_group "help"
            xfill True


            vbox:
                spacing 20
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("CHATACTERS") action ShowMenu("help_characters")
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("CONTROLS") action ShowMenu("help_controls")
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("WORLD") action ShowMenu("help_world")
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("CREDITS") action ShowMenu("help_credits")
    
    vbar:
        value YScrollValue("help_vp")
        
        left_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        right_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        
        left_gutter 0
        right_gutter 0
        bottom_gutter 0
        top_gutter 0
        
        thumb_offset 0
        
        thumb Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        thumb_shadow Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        
        bar_resizing False
        
        xsize 10
        ysize 878
        xpos 101
        ypos 100

init -2:
    style help_frame:

        background Frame("gui/ui/FrameBox.png", 2, 2, 2, 2)
        xfill True
        ysize 100
        xsize 1050

    style help_left_hbox:
        xalign 1.0
        xoffset -20
        yalign 0.5
    style help_left_text:
        color "000000ff"
        text_align 1.0

    style help_right_hbox:
        xpos 20
        yalign 0.5
    style help_right_text:
        color "000000ff"
        text_align 0.0

    style help_vbox:
        xfill True

    style help_lable:

        yalign 0.5

    style help_button:
        xfill True
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        xalign 0

        ysize 50
        xsize 250
        left_margin 25

    style help_slider:
        xmaximum 192
        xalign 0

    style soundtest_button:
        xalign 1.0
        
#################################################
# Characters Info
#
# This is the Help Screen For info on Characters
# Coded By: Jonathan Oakes (Darth62969, TheWired)
# Character Descriptions By: 
 
screen help_characters ():
    
    tag menu
    
# Include the InGameMenu
    use InGameMenu

# Window Title    
    hbox:
        xpos 100
        ypos 10
        
        text "HELP" size 64 color "000000ff"
# Help Window    
    viewport id "help_vp":
        draggable True
        mousewheel True
        child_size (1050, 6000)
        xalign 0
        yalign 0
        xsize 1050
        ysize 828
        xpos 125
        ypos 125
        
        
        grid 1 1:
            style_group "help"
            xfill True
            
            vbox:
                spacing 20
                
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("BACK") action ShowMenu("help")

init -2:
    style help_frame:

        background Frame("gui/ui/FrameBox.png", 2, 2, 2, 2)
        xfill True
        ysize 100
        xsize 1050

    style help_left_hbox:
        xalign 1.0
        xoffset -20
        yalign 0.5
    style help_left_text:
        color "000000ff"
        text_align 1.0

    style help_right_hbox:
        xpos 20
        yalign 0.5
    style help_right_text:
        color "000000ff"
        text_align 0.0

    style help_vbox:
        xfill True

    style help_lable:

        yalign 0.5

    style help_button:
        xfill True
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        xalign 0

        ysize 50
        xsize 250
        left_margin 25

    style help_slider:
        xmaximum 192
        xalign 0

###################################################################
# Help Controls
#
# This is the Help Menu for the Controls
# By: Brunn08, Jonathan Oakes (Darth62969, TheWired)

screen help_controls ():
    
    tag menu
    
# Include the InGameMenu
    use InGameMenu

# Window Title    
    hbox:
        xpos 100
        ypos 10
        
        text "HELP" size 64 color "000000ff"
# Help Window    
    viewport id "help_vp":
        draggable True
        mousewheel True
        child_size (1050, 6000)
        xalign 0
        yalign 0
        xsize 1050
        ysize 828
        xpos 125
        ypos 125
        
        
        grid 1 1:
            style_group "help"
            xfill True


            vbox:
                spacing 20
                frame:
                    hbox:
                        style_group "help_right"
                        text "Left click, Enter, Space"
                    hbox:
                        style_group "help_left"
                        text "Advance text"
        

                frame:
                    hbox:
                        style_group "help_right"
                        text "S"
                    hbox:
                        style_group "help_left"
                        text "Take screenshot"
                frame:
                    hbox:
                        style_group "help_right"
                        text "Delete"
                    hbox:
                        style_group "help_left"
                        text "Delete selected save"
                frame:
                    hbox:
                        style_group "help_right"
                        text "F"
                    hbox:
                        style_group "help_left"
                        text "Fullscreen"
                frame:
                    hbox:
                        style_group "help_right"
                        text "A"
                    hbox:
                        style_group "help_left"
                        text "Auto advance"
                frame:
                    hbox:
                        style_group "help_right"
                        text "Mouse wheel up"
                    hbox:
                        style_group "help_left"
                        text "Rewind"
                frame:
                    hbox:
                        style_group "help_right"
                        text "Mouse wheel down"
                    hbox:
                        style_group "help_left"
                        text "Forward"
                frame:
                    hbox:
                        style_group "help_right"
                        text "H"
                    hbox:
                        style_group "help_left"
                        text "Hide text"
                frame:
                    hbox:
                        style_group "help_right"
                        text "Arrow keys"
                    hbox:
                        style_group "help_left"
                        text "Select menu choices"
                frame:
                    hbox:
                        style_group "help_right"
                        text "Tab"
                    hbox:
                        style_group "help_left"
                        text "Toggle skipping"
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("BACK") action ShowMenu("help")
    
    vbar:
        value YScrollValue("help_vp")
        
        left_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        right_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        
        left_gutter 0
        right_gutter 0
        bottom_gutter 0
        top_gutter 0
        
        thumb_offset 0
        
        thumb Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        thumb_shadow Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        
        bar_resizing False
        
        xsize 10
        ysize 878
        xpos 101
        ypos 100


init -2:
    style help_frame:

        background Frame("gui/ui/FrameBox.png", 2, 2, 2, 2)
        xfill True
        ysize 100
        xsize 1050

    style help_left_hbox:
        xalign 1.0
        xoffset -20
        yalign 0.5
    style help_left_text:
        color "000000ff"
        text_align 1.0

    style help_right_hbox:
        xpos 20
        yalign 0.5
    style help_right_text:
        color "000000ff"
        text_align 0.0

    style help_vbox:
        xfill True

    style help_lable:

        yalign 0.5

    style help_button:
        xfill True
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        xalign 0

        ysize 50
        xsize 250
        left_margin 25

    style help_slider:
        xmaximum 192
        xalign 0

########################################################################
# The World screen for the Help Menu
# By: Jonathan Oakes (Darth62969, TheWired)
  
screen help_world ():
    
    tag menu
    
# Include the InGameMenu
    use InGameMenu

# Window Title    
    hbox:
        xpos 100
        ypos 10
        
        text "HELP" size 64 color "000000ff"
# Help Window    
    viewport id "help_vp":
        draggable True
        mousewheel True
        child_size (1050, 6000)
        xalign 0
        yalign 0
        xsize 1050
        ysize 828
        xpos 125
        ypos 125
        
        
        grid 1 1:
            style_group "help"
            xfill True
 
            vbox:
                spacing 20
                
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("BACK") action ShowMenu("help")


init -2:
    style help_frame:

        background Frame("gui/ui/FrameBox.png", 2, 2, 2, 2)
        xfill True
        ysize 100
        xsize 1050

    style help_left_hbox:
        xalign 1.0
        xoffset -20
        yalign 0.5
    style help_left_text:
        color "000000ff"
        text_align 1.0

    style help_right_hbox:
        xpos 20
        yalign 0.5
    style help_right_text:
        color "000000ff"
        text_align 0.0

    style help_vbox:
        xfill True

    style help_lable:

        yalign 0.5

    style help_button:
        xfill True
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        xalign 0

        ysize 50
        xsize 250
        left_margin 25

######################################################################
# Credits For Help Menu
#
# These are the Credits for the Help Menu
# By: Jonathan Oakes (Darth62969, TheWired)

screen help_credits ():
    
    tag menu
    
# Include the InGameMenu
    use InGameMenu

# Window Title    
    hbox:
        xpos 100
        ypos 10
        
        text "HELP" size 64 color "000000ff"
# Help Window    
    viewport id "help_vp":
        draggable True
        mousewheel True
        child_size (1050, 6000)
        xalign 0
        yalign 0
        xsize 1050
        ysize 828
        xpos 125
        ypos 125
        
        
        grid 1 1:
            style_group "help_credits"
            xfill True
 
            vbox:
                spacing 20
                
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Project Lead"
                        hbox:
                            style_group "help_credits_left"
                            text "Rioku"
                     
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Story Lead"
                        hbox:
                            style_group "help_credits_left"
                            text "Rioku"
                
                frame:
                    hbox:
                        style "help_credits_hbox"
                
                        hbox:
                            style_group "help_credits_right"
                            text "Writers:"
                            
                        vbox:
                            style_group "help_credits_left"
                       
                            text "Rioku"
                            text "Vladimito" #ai atsuko common route
                            text "Amy2" #ai
                            text "Mafuyu" #mana
                            text "ChaosBeing" #Hirohito, Takashi
                             
                frame:
                    hbox:
                        style "help_credits_hbox"
                
                        hbox:
                            style_group "help_credits_right"
                            text "Story Development:"
                            
                        vbox:
                            style_group "help_credits_left"
                       
                            text "Rioku"
                            text "Vladimito"
                            text "Amy2"
                            text "Mafuyu"
                            text "ChaosBeing"
                            text "The Wired"
                            text "AngelTheGabriel"

                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Programming Lead"
                        hbox:
                            style_group "help_credits_left"
                            text "TheWired"

                frame:
                    hbox:
                        style "help_credits_hbox"
                
                        hbox:
                            style_group "help_credits_right"
                            text "Programmers:"
                            
                        vbox:
                            style_group "help_credits_left"
                       
                            text "TheWired"
                            text "Xumbra"
                            text "Brunn08"
                            text "Rioku"
                            
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Design Lead - UI"
                        hbox:
                            style_group "help_credits_left"
                            text "TheWired"
                
                frame:
                    hbox:
                        style "help_credits_hbox"
                
                        hbox:
                            style_group "help_credits_right"
                            text "Design - UI:"
                            
                        vbox:
                            style_group "help_credits_left"
                       
                            text "TheWired"
                            text "Brunn08"
                            
                frame:
                    hbox:
                        style "help_credits_hbox"
                
                        hbox:
                            style_group "help_credits_right"
                            text "Editors, SpellCheckers:"
                            
                        vbox:
                            style_group "help_credits_left"
                       
                            text "AngelTheGabriel"
                            text "Amy2"
                            
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Character Design"
                        hbox:
                            style_group "help_credits_left"
                            text "Rioku's Sister"

                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Peacekeeper"
                        hbox:
                            style_group "help_credits_left"
                            text "Rioku"
                 
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Pain in the Ass Stubborn Rock"
                        hbox:
                            style_group "help_credits_left"
                            text "TheWired"
                            
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Code Cleaner, Guide Book"
                        hbox:
                            style_group "help_credits_left"
                            text "Xumbra"

                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Loves Grills as Well as the Kawaiiest Grill of All, Rioku"
                        hbox:
                            style_group "help_credits_left"
                            text "Vladimito"
                    
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Weaboo Beauty"
                        hbox:
                            style_group "help_credits_left"
                            text "Amy2"
    
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "Main Character in Training"
                        hbox:
                            style_group "help_credits_left"
                            text "AngelTheGabriel"
    
                frame:
                    hbox:
                        style "help_credits_hbox"
                        
                        hbox:
                            style_group "help_credits_right"
                            text "The One That Can't make Puns"
                        hbox:
                            style_group "help_credits_left"
                            text "Mafuyu"
    
                frame:
                    hbox:
                        xpos 350
                        yalign 0.5
                        textbutton ("BACK") action ShowMenu("help")

    vbar:
        value YScrollValue("help_vp")
        
        left_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        right_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        
        left_gutter 0
        right_gutter 0
        bottom_gutter 0
        top_gutter 0
        
        thumb_offset 0
        
        thumb Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        thumb_shadow Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        
        bar_resizing False
        
        xsize 10
        ysize 878
        xpos 101
        ypos 100

init -2:
    style help_credits_frame:

        background Frame("gui/ui/FrameBox.png", 2, 2, 2, 2)
        xfill True
        
        xsize 1050

        yminimum 100
        ymaximum 500
        
        ypadding 30
        
    style help_credits_fixed:
        xfill True
    
        xsize 1050
           
        fit_first True
 
    style help_credits_left_hbox:
        xalign 1.0
        xoffset -20

    style help_credits_left_vbox:
        xalign 1.0
        xoffset -20
        yalign 0.5

    style help_credits_left_text:
        color "000000ff"
        text_align 1.0
        xanchor 1.0
        xalign 1.0

    style help_credits_right_hbox:
        xpos 20

    style help_credits_right_text:
        color "000000ff"
        text_align 0.0
        xmaximum 0.5

    style help_credits_vbox:
        xfill True
        
    style help_credits_hbox:
        xfill True
        
        xsize 1030

        yalign 0.5
        
    style help__credits_lable:
        yalign 0.5

    style help_credits_button:
        xfill True
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        xalign 0

        ysize 50
        xsize 250
        left_margin 25


 
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"
        
    frame:
        
        background Image("gui/ui/YesNoFrame.png")
        
        xsize 960
        ysize 360
        xpos 490
        ypos 180
            
        label _(message):
            xalign 0.5
            yalign 0.25
            text_size 38

        hbox:

            xalign 0.5
            ypos 252
            spacing 100

            imagebutton auto "gui/yn/yes_%s.png" focus_mask True action yes_action
            imagebutton auto "gui/yn/no_%s.png" focus_mask True action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5 


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        xalign 0
        yalign 1.0
        
        imagebutton auto "gui/qm/qload_%s.png" xpos 20 ypos -115 focus_mask True action QuickLoad()
    
    hbox:
        xalign 0
        yalign 1.0
        
        imagebutton auto "gui/qm/qsave_%s.png" xpos 20 ypos -50 focus_mask True action QuickSave()    
    
    hbox:
        xalign 0
        yalign 1.0
        
        imagebutton auto "gui/qm/prefs_%s.png" xpos 1675 ypos -115 focus_mask True action ShowMenu('preferences')
    hbox: 
        xalign 0
        yalign 1.0

        imagebutton auto "gui/qm/save_%s.png" xpos 1805 ypos -180 focus_mask True action ShowMenu('save')
        imagebutton auto "gui/qm/load_%s.png" xpos 1580 ypos -180 focus_mask True action ShowMenu('load')
    hbox:
        xalign 0
        yalign 1.0

        imagebutton auto "gui/qm/quit_%s.png" xpos 1700 ypos -50 focus_mask True action Quit(confirm=True)


    hbox: 
        xalign 0
        yalign 1.0

        imagebutton auto "gui/qm/auto_%s.png" xpos 20 ypos -180 focus_mask True action Preference("auto-forward", "toggle")
        imagebutton auto "gui/qm/skip_%s.png" xpos 54 ypos -180 focus_mask True action Skip()
        

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

