function Symbols () {
    basic.showIcon(IconNames.EigthNote)
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            `)
        basic.showLeds(`
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            `)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # . . . .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            # . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            `)
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . . #
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . # # # .
            # # # . .
            # # . . #
            # # # . .
            . # # # .
            `)
        basic.showLeds(`
            . # # # .
            # # # . .
            # # . # .
            # # # . .
            . # # # .
            `)
        basic.showLeds(`
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            `)
    }
}
bluetooth.onBluetoothConnected(function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Yes)
    music.playMelody("E B E F B A E C5 ", 120)
    while (true) {
        Symbols()
    }
})
bluetooth.onBluetoothDisconnected(function () {
    basic.clearScreen()
    basic.showIcon(IconNames.No)
    music.stopMelody(MelodyStopOptions.All)
    music.playMelody("E B E F A G E C ", 120)
    bluetooth.startButtonService()
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showString("Hello! The Temperature is")
    basic.showNumber(input.temperature())
    basic.showString("C")
})
music.playMelody("G A F G A F B C5 ", 300)
for (let index = 0; index < 4; index++) {
    basic.showLeds(`
        # . # . #
        # . # . #
        # # # . #
        # . # . #
        # . # . #
        `)
    basic.showIcon(IconNames.Happy)
    basic.showLeds(`
        # . # . #
        # . # . #
        # # # . #
        # . # . #
        # . # . #
        `)
}
bluetooth.startButtonService()
basic.forever(function () {
	
})
