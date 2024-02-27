import board
from storage import getmount
from supervisor import runtime

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation


kb = KMKKeyboard()
kb.modules.append(CapsWord())
kb.modules.append(Layers())
kb.modules.append(TapDance())

# Fix my abysmal wiring job and set up the splits
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
if side == SplitSide.RIGHT:
    print("Initialising RIGHT side")
    kb.row_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP5,
        board.GP4,
    )
    kb.col_pins = (
        board.GP10,
        board.GP13,
        board.GP11,
        board.GP12,
        board.GP14,
        board.GP15,
    )
    kb.diode_orientation = DiodeOrientation.COL2ROW
    split = Split(
        split_flip=False,
        split_side=side,
        split_type=SplitType.UART,
        split_target_left=not runtime.usb_connected,
        data_pin=board.GP17,
        data_pin2=board.GP16,
        uart_flip=False,
    )
else:
    print("Initialising LEFT side")
    kb.col_pins = (
        board.GP5,
        board.GP4,
        board.GP1,
        board.GP3,
        board.GP2,
        board.GP0,

    )
    kb.row_pins = (
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11,
        board.GP10,
        board.GP9
    )
    kb.diode_orientation = kb.diode_orientation = DiodeOrientation.COL2ROW
    split = Split(
        split_side=side,
        split_type=SplitType.UART,
        split_target_left=runtime.usb_connected,
        data_pin=board.GP17,
        data_pin2=board.GP16,
        uart_flip=False,
    )
kb.modules.append(split)

ABSENT = KC.NO
UNBOUND = KC.NO
TO_QWERTY = KC.TD(UNBOUND, KC.DF(0))
TO_COLEMAK = KC.TD(UNBOUND, KC.DF(1))
kb.keymap = [
    # QWERTY
    [
        KC.GRAVE,  KC.N1,   KC.N2,       KC.N3,       KC.N4,    KC.N5,            KC.N6,     KC.N7,     KC.N8,        KC.N9,          KC.N0,       KC.EQUAL,
        KC.TAB,    KC.Q,    KC.W,        KC.E,        KC.R,     KC.T,             KC.Y,      KC.U,      KC.I,         KC.O,           KC.P,        KC.MINUS,
        KC.CW,     KC.A,    KC.S,        KC.D,        KC.F,     KC.G,             KC.H,      KC.J,      KC.K,         KC.L,           KC.SCOLON,   KC.QUOTE,
        KC.LSHIFT, KC.Z,    KC.X,        KC.C,        KC.V,     KC.B,             KC.N,      KC.M,      KC.COMMA,     KC.DOT,         KC.SLASH,    UNBOUND,
        ABSENT,    ABSENT,  KC.LBRACKET, KC.RBRACKET, KC.ENTER, KC.SPACE,         KC.BSPACE, KC.DELETE, UNBOUND,      UNBOUND,        ABSENT,      ABSENT,
        ABSENT,    ABSENT,  KC.LWIN,     TO_COLEMAK,  KC.LALT,  KC.LCTRL,         KC.RCTRL,  KC.RSHIFT, KC.RALT,      KC.RGUI,        ABSENT,      ABSENT,
    ],

    # Native Colemak
    [
        KC.GRAVE,  KC.N1,   KC.N2,       KC.N3,       KC.N4,    KC.N5,            KC.N6,     KC.N7,      KC.N8,       KC.N9,          KC.N0,       KC.EQUAL,
        KC.TAB,    KC.Q,    KC.W,        KC.F,        KC.P,     KC.B,             KC.J,      KC.L,       KC.U,        KC.Y,           KC.SCOLON,   KC.MINUS,
        KC.CW,     KC.A,    KC.R,        KC.S,        KC.T,     KC.G,             KC.M,      KC.N,       KC.E,        KC.I,           KC.O,        KC.QUOTE,
        KC.LSHIFT, KC.Z,    KC.X,        KC.C,        KC.D,     KC.V,             KC.K,      KC.H,       KC.COMMA,    KC.DOT,         KC.SLASH,    UNBOUND,
        ABSENT,    ABSENT,  KC.LBRACKET, KC.RBRACKET, KC.ENTER, KC.SPACE,         KC.BSPACE, KC.DELETE,  UNBOUND,     UNBOUND,        ABSENT,      ABSENT,
        ABSENT,    ABSENT,  KC.LWIN,     TO_QWERTY,   KC.LALT,  KC.LCTRL,         KC.RCTRL,  KC.RSHIFT,  KC.RALT,     KC.RGUI,        ABSENT,      ABSENT,
    ],

    # Numpad and Function
    [
        KC.NO,     UNBOUND, UNBOUND,     UNBOUND,     UNBOUND,  UNBOUND,          UNBOUND,   KC.NUMLOCK, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS, UNBOUND,
        KC.NO,     KC.F9,   KC.F10,      KC.F11,      KC.F12,   UNBOUND,          UNBOUND,   KC.KP_7,    KC.KP_8,     KC.KP_9,        KC.KP_PLUS,  UNBOUND,
        KC.NO,     KC.F5,   KC.F6,       KC.F7,       KC.F8,    UNBOUND,          UNBOUND,   KC.KP_4,    KC.KP_5,     KC.KP_6,        KC.KP_PLUS,  UNBOUND,
        KC.NO,     KC.F1,   KC.F2,       KC.F3,       KC.F4,    UNBOUND,          UNBOUND,   KC.KP_1,    KC.KP_2,     KC.KP_3,        KC.KP_ENTER, UNBOUND,
        ABSENT,    ABSENT,  UNBOUND,     UNBOUND,     UNBOUND,  UNBOUND,          UNBOUND,   KC.KP_0,    KC.KP_0,     KC.KP_DOT,      ABSENT,      ABSENT,
        ABSENT,    ABSENT,  UNBOUND,     UNBOUND,     UNBOUND,  UNBOUND,          UNBOUND,   UNBOUND,    UNBOUND,     UNBOUND,        ABSENT,      ABSENT,
    ],
]


if __name__ == "__main__":
    kb.go()
