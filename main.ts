control.onEvent(EventBusSource.MES_BROADCAST_GENERAL_ID, EventBusValue.MES_REMOTE_CONTROL_EVT_PAUSE, function () {
    music.stopMelody(MelodyStopOptions.All)
})
bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
    music.playMelody("E B E F B A E C5 ", 120)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
    music.stopMelody(MelodyStopOptions.All)
    music.playMelody("E B E F A G E C ", 120)
    bluetooth.startButtonService()
})
control.onEvent(EventBusSource.MES_BROADCAST_GENERAL_ID, EventBusValue.MES_ALERT_EVT_PLAY_SOUND, function () {
    music.setVolume(127)
})
basic.showLeds(`
    # . # . #
    # . # . #
    # # # . #
    # . # . #
    # . # . #
    `)
bluetooth.startButtonService()
basic.forever(function () {
	
})
