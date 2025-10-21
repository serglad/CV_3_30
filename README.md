# CV_3_30
Perspective correction and text detection using EAST
## Workflow
1) pc.warp_perspective(): Reads the input image, then tries to find document contours. If successful, warps and crops the image, then saves it as "document.jpg". If unsuccessful, copies the original instead
2) td.main(): Detects text on the warped image and overlays boxes over it. The result is then saved as output
## Setup
```bash
# 1) Venv intialization
python3 -m venv .venv
source ./.venv/bin/activate
# 2) Dependencies
pip install -r requirements.txt
# 3) Submodule init
git submodule update --init --recursive
```
## Usage
```bash
python3 PCDetect.py fin fout
fin - name of the input file
fout - output path
```
## Submodules
Perspective correction - https://gitlab.com/NoSignificantWorries/CV-2-25/ <p>
Text detection - https://github.com/Graf-Durka/Text-detection (A forked version is used for modularity:https://github.com/serglad/Text_detection)
</p>
