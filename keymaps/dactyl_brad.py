import board
from storage import getmount
from supervisor import runtime

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.tapdance import TapDance
from kmk.modules.oneshot import OneShot
from kmk.scanners import DiodeOrientation


kb = KMKKeyboard()

# Fix my abysmal wiring job and set up the splits
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
if side == SplitSide.RIGHT:
    print("Initialising RIGHT side")
    kb.col_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP5,
        board.GP4,
    )
    kb.row_pins = (
        board.GP10,
        board.GP13,
        board.GP11,
        board.GP12,
        board.GP14,
        board.GP15,
    )
    kb.diode_orientation = DiodeOrientation.COL2ROW
    split = Split(
        split_flip=True,
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
        board.GP9,
    )
    kb.diode_orientation = kb.diode_orientation = DiodeOrientation.COL2ROW
    split = Split(
        split_flip=False,
        split_side=side,
        split_type=SplitType.UART,
        split_target_left=runtime.usb_connected,
        data_pin=board.GP17,
        data_pin2=board.GP16,
        uart_flip=False,
    )
kb.modules.append(split)

kb.modules.append(CapsWord())
kb.modules.append(Layers())
kb.modules.append(TapDance())
kb.modules.append(OneShot())


ABSENT = KC.NO
UNBOUND = KC.NO

NAV_FN = KC.TD(KC.TT(1), UNBOUND, KC.TO(0))
SYM = KC.TD(KC.TT(2), NAV_FN)
NUMPAD = KC.TT(3)
NUM_SYM = KC.TD(KC.TT(4), NUMPAD, KC.TO(0))

REDO = KC.LCTRL(KC.Y)
UNDO = KC.LCTRL(KC.Z)
CUT = KC.LCTRL(KC.X)
COPY = KC.LCTRL(KC.C)
PASTE = KC.LCTRL(KC.V)

RCTRL_EQ = KC.HT(KC.EQUAL, KC.RCTRL)
BSPC_KW = KC.HT(KC.BSPACE, KC.LCTRL(KC.BSPACE), prefer_hold=False, tap_time=150)
RSFT_CW = KC.TD(KC.RSHIFT, KC.CW)
LSFT_CW = KC.TD(KC.LSHIFT, KC.CW)


kb.keymap = [
    # Native Colemak
    [
        KC.GRAVE,  KC.N1,   KC.N2,       KC.N3,       KC.N4,     KC.N5,            KC.N6,     KC.N7,      KC.N8,       KC.N9,          KC.N0,       KC.EQUAL,
        KC.ESC,    KC.Q,    KC.W,        KC.F,        KC.P,      KC.B,             KC.J,      KC.L,       KC.U,        KC.Y,           KC.SCOLON,   KC.MINUS,
        KC.TAB,    KC.A,    KC.R,        KC.S,        KC.T,      KC.G,             KC.M,      KC.N,       KC.E,        KC.I,           KC.O,        KC.QUOTE,
        LSFT_CW,   KC.Z,    KC.X,        KC.C,        KC.D,      KC.V,             KC.K,      KC.H,       KC.COMMA,    KC.DOT,         KC.SLASH,    RSFT_CW,
        ABSENT,    ABSENT,  KC.LBRACKET, KC.RBRACKET, BSPC_KW,   KC.SPACE,         KC.ENTER,  KC.DELETE,  KC.LPRN,     KC.RPRN,        ABSENT,      ABSENT,
        ABSENT,    ABSENT,  KC.LALT,     KC.LWIN,     KC.LCTRL,  NAV_FN,           NUM_SYM,   RCTRL_EQ,   KC.RALT,     KC.RWIN,        ABSENT,      ABSENT,
    ],

    # Function and Nav Layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.PGUP,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.F12,  KC.F7,        KC.F8,       KC.F9,     KC.PSCR,            KC.TRNS,   KC.HOME,    KC.UP,       KC.END,         KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.F11,  KC.F4,        KC.F5,       KC.F6,     KC.SLCK,            KC.CW,     KC.LEFT,    KC.DOWN,     KC.RIGHT,       KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.F10,  KC.F1,        KC.F2,       KC.F3,     KC.PAUSE,           KC.INS,    KC.TRNS,    KC.PGDN,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ],

    # Symbol Layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.LCBR,   KC.LPRN,    KC.ASTR,     KC.AMPR,        KC.RCBR,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.PLUS,   KC.CIRC,    KC.PERCENT,  KC.DLR,         KC.COLN,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.PIPE,   KC.HASH,    KC.AT,       KC.EXLM,        KC.TILD,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ],

    # Numpad Layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.LBRC, KC.P7,        KC.P8,       KC.P9,     KC.RBRC,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.SCLN, KC.P4,        KC.P5,       KC.P6,     KC.EQUAL,           KC.EQUAL,  KC.PLUS,    KC.MINUS,    KC.ASTR,        KC.SLASH,    KC.TRNS,
        KC.TRNS,  KC.NLCK, KC.P1,        KC.P2,       KC.P3,     KC.BSLASH,          KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.DOT,       KC.P0,       KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ],

    # Number/Symbol layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.SLASH, KC.EXLM, KC.AT,        KC.HASH,     KC.DLR,    KC.PERCENT,         KC.CIRC,   KC.AMPR,    KC.ASTR,     KC.LPRN,        KC.RPRN,     KC.MINUS,
        KC.BSLASH,KC.N1,   KC.N2,        KC.N3,       KC.N4,     KC.N5,              KC.N6,     KC.N7,      KC.N8,       KC.N9,          KC.N0,       KC.PLUS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.EQUAL,  KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ]
]


if __name__ == "__main__":
    kb.go()
