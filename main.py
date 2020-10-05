def Symbols():
    basic.show_icon(IconNames.EIGTH_NOTE)
    for index in range(4):
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        basic.show_leds("""
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            # . . . .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            # . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            """)
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . . #
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    for index2 in range(4):
        basic.show_leds("""
            . # # # .
            # # # . .
            # # . . #
            # # # . .
            . # # # .
            """)
        basic.show_leds("""
            . # # # .
            # # # . .
            # # . # .
            # # # . .
            . # # # .
            """)
        basic.show_leds("""
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            """)

def on_bluetooth_connected():
    basic.clear_screen()
    basic.show_icon(IconNames.YES)
    music.play_melody("E B E F B A E C5 ", 120)
    while True:
        Symbols()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.clear_screen()
    basic.show_icon(IconNames.NO)
    music.stop_melody(MelodyStopOptions.ALL)
    music.play_melody("E B E F A G E C ", 120)
    bluetooth.start_button_service()
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_string("Hello! The Temperature is")
    basic.show_number(input.temperature())
    basic.show_string("C")
input.on_button_pressed(Button.B, on_button_pressed_b)

device_name = "Aris's Speaker"

basic.show_string(control.device_name())
for index3 in range(4):
    basic.show_leds("""
        # . # . #
        # . # . #
        # # # . #
        # . # . #
        # . # . #
        """)
    basic.show_icon(IconNames.HAPPY)
    basic.show_leds("""
        # . # . #
        # . # . #
        # # # . #
        # . # . #
        # . # . #
        """)
bluetooth.start_button_service()

def on_forever():
    pass
basic.forever(on_forever)
