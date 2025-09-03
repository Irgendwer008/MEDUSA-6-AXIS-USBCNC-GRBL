with open("dauertest.gcode", "w") as f:
    f.write("""G21 ; millimeters
G90 ; absolute coordinate
G17 ; XY plane
G94 ; units per minute feed rate mode

; Go to zero location
G0 X0 Y0 Z0
""")

    for i in range(1500):
        f.write(f"""
; Cycle #{i}
M3 S{500+i}
; Shape
G1 X10 Y200 Z0 F6000
G3 X10 Y200 Z100 I130 J0 F2700
G3 X10 Y200 Z200 I130 J0 F2700
G3 X10 Y200 Z300 I130 J0 F2700
G1 X0 Y0 Z0 F6000
; Lower
G1 X280
G1 Y400
G1 X0
G1 Y0
G1 Z300
; Upper
G1 X280
G1 Y400
G1 X0
G1 Y0
G1 Z0
; Diagonal
G1 X280 Y400 Z300
G1 X0 Y0 Z0
""")