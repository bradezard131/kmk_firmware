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
kb.modules.append(CapsWord())
kb.modules.append(Layers())
kb.modules.append(TapDance())
kb.modules.append(OneShot())

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


ABSENT = KC.NO
UNBOUND = KC.NO

WIN_NAV = KC.LT(1, KC.LWIN)
FN_RCTRL = KC.HT(KC.OS(KC.MO(2)), KC.RCTRL)
SYM_RALT = KC.HT(KC.OS(KC.MO(3)), KC.RALT)
NUMPAD = KC.TG(4)

REDO = KC.LCTRL(KC.Y)
UNDO = KC.LCTRL(KC.Z)
CUT = KC.LCTRL(KC.X)
COPY = KC.LCTRL(KC.C)
PASTE = KC.LCTRL(KC.V)


kb.keymap = [
    # Native Colemak
    [
        KC.GRAVE,  KC.N1,   KC.N2,       KC.N3,       KC.N4,     KC.N5,            KC.N6,     KC.N7,      KC.N8,       KC.N9,          KC.N0,       KC.EQUAL,
        NUMPAD,    KC.Q,    KC.W,        KC.F,        KC.P,      KC.B,             KC.J,      KC.L,       KC.U,        KC.Y,           KC.SCOLON,   KC.MINUS,
        UNBOUND,   KC.A,    KC.R,        KC.S,        KC.T,      KC.G,             KC.M,      KC.N,       KC.E,        KC.I,           KC.O,        KC.QUOTE,
        KC.LSHIFT, KC.Z,    KC.X,        KC.C,        KC.D,      KC.V,             KC.K,      KC.H,       KC.COMMA,    KC.DOT,         KC.SLASH,    KC.RSHIFT,
        ABSENT,    ABSENT,  KC.LBRACKET, KC.RBRACKET, KC.BSPACE, KC.SPACE,         KC.ENTER,  KC.DELETE,  KC.LPRN,     KC.RPRN,        ABSENT,      ABSENT,
        ABSENT,    ABSENT,  KC.LALT,     WIN_NAV,     KC.LCTRL,  KC.TAB,           KC.ESC,    FN_RCTRL,   SYM_RALT,    KC.RWIN,        ABSENT,      ABSENT,
    ],

    # Nav Layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            REDO,      PASTE,      COPY,        CUT,            UNDO,        KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.CW,     KC.LEFT,    KC.DOWN,     KC.UP,          KC.RIGHT,    KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.INS,    KC.HOME,    KC.PGDN,     KC.PGUP,        KC.END,      KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ],

    # Function Layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.F12,  KC.F7,        KC.F8,       KC.F9,     KC.PSCR,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.F11,  KC.F4,        KC.F5,       KC.F6,     KC.SLCK,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.F10,  KC.F1,        KC.F2,       KC.F3,     KC.PAUSE,           KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.SEL,    KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ],

    # Symbol Layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.LCBR, KC.AMPR,      KC.ASTR,     KC.LPRN,   KC.RCBR,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.COLN, KC.DLR,       KC.PERCENT,  KC.CIRC,   KC.PLUS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TILD, KC.EXLM,      KC.AT,       KC.HASH,   KC.PIPE,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.LPRN,   KC.RPRN,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.UNDS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ],

    # Num Layer
    [
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.TRNS,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.LBRC, KC.N7,        KC.N8,       KC.N9,     KC.RBRC,            KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.SCLN, KC.N4,        KC.N5,       KC.N6,     KC.EQUAL,           KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.GRV,  KC.N1,        KC.N2,       KC.N3,     KC.BSLASH,          KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.DOT,    KC.N0,              KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,      KC.TRNS,     KC.TRNS,   KC.MINUS,           KC.TRNS,   KC.TRNS,    KC.TRNS,     KC.TRNS,        KC.TRNS,     KC.TRNS,
    ],
]


if __name__ == "__main__":
    kb.go()
