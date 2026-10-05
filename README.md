# TI-Nspire Stuff

Tools for the **TI-Nspire CX II CAS** calculator.

## Contents

- `hvac/` — HVAC Toolkit, a Python program for the TI-Nspire's Python shell.
  Iterations of the same tool (the ` (1)`, ` (2)` suffixes are Windows
  download-copy artifacts; each file is a distinct version):
  - `hvac.py` — base version: unit converter + formula reference
  - `hvac (1).py`, `hvac (2).py` — early iterations
  - `hvac (3).py` — adds P-T tables (R-410A, R-22, R-134a) with interpolation
  - `hvac(4).py` — P-T tables, menus sized for the 11-line screen
  - `hvac(5).py` — "HVAC PRO TOOLKIT v5": A2L refrigerant support (R-32, R-454B,
    R-1234yf), superheat/subcooling diagnostics, 2026-standards data
  - `# HVAC Toolkit for TI-Nspire CX II CAS.py` — standalone full build
- `myscript/` — `.tns` TI-Nspire document files (binary; open on the calculator
  or in TI-Nspire student/teacher software).
- `archive/` — byte-identical duplicate of `myscript/MyScript (2).tns`
  (kept out of the way, still in git history).

## How to use

1. Connect the calculator via USB and open TI-Nspire Student Software
   (or TI-Nspire CX Student Software).
2. For Python: copy a `hvac/*.py` file to the calculator and run it from the
   Python shell (`menu` → add Python).
3. For documents: drag a `myscript/*.tns` file onto the calculator in the
   software's content pane.

Note: an `ndless-r2021.zip` was previously in this repo and has been removed
(git history).
