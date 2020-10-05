def on_mes_broadcast_general_id_remote_control_evt_pause():
    music.stop_melody(MelodyStopOptions.ALL)
control.on_event(EventBusSource.MES_BROADCAST_GENERAL_ID,
    EventBusValue.MES_REMOTE_CONTROL_EVT_PAUSE,
    on_mes_broadcast_general_id_remote_control_evt_pause)

def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
    music.play_melody("E B E F B A E C5 ", 120)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
    music.stop_melody(MelodyStopOptions.ALL)
    music.play_melody("E B E F A G E C ", 120)
    bluetooth.start_button_service()
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_mes_broadcast_general_id_alert_evt_play_sound():
    music.set_volume(127)
control.on_event(EventBusSource.MES_BROADCAST_GENERAL_ID,
    EventBusValue.MES_ALERT_EVT_PLAY_SOUND,
    on_mes_broadcast_general_id_alert_evt_play_sound)

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
