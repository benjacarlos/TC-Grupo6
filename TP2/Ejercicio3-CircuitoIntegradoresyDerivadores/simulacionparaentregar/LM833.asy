Version 4
SymbolType CELL
LINE Normal -32 -32 32 0
LINE Normal -32 32 32 0
LINE Normal -32 -32 -32 32
LINE Normal -28 -16 -20 -16
LINE Normal -28 16 -20 16
LINE Normal -24 20 -24 12
LINE Normal 0 -32 0 -16
LINE Normal 0 32 0 16
LINE Normal 4 -20 12 -20
LINE Normal 8 -24 8 -16
LINE Normal 4 20 12 20
WINDOW 0 23 25 Left 2
SYMATTR SpiceModel LM833
SYMATTR Prefix X
SYMATTR Description Trying to be an LM833 op-amp
SYMATTR Value2 Avol=316.2K GBW=15Meg Slew=5Meg
SYMATTR SpiceLine ilimit=25m rail=0 Vos=0 phimargin=60
SYMATTR SpiceLine2 en=0 enk=0 in=0 ink=0 Rin=175K
SYMATTR ModelFile nico/LM833.sub
SYMATTR Value LM833
PIN -32 16 NONE 0
PINATTR PinName In+
PINATTR SpiceOrder 1
PIN -32 -16 NONE 0
PINATTR PinName In-
PINATTR SpiceOrder 2
PIN 0 -32 NONE 0
PINATTR PinName V+
PINATTR SpiceOrder 3
PIN 0 32 NONE 0
PINATTR PinName V-
PINATTR SpiceOrder 4
PIN 32 0 NONE 0
PINATTR PinName OUT
PINATTR SpiceOrder 5
