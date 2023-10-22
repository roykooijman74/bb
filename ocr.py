import pyautogui
import pytesseract
from PIL import Image

# Take a screenshot of the primary display
screenshot = pyautogui.screenshot()

# Convert the screenshot to grayscale
screenshot_gray = screenshot.convert('L')

# Use OCR to extract text from the screenshot
text = pytesseract.image_to_string(screenshot_gray)

# Print the extracted text
print(text)

SMURF_COORDINATES = [
    [960, 540, 1920, 1080, "supersmurf"],
    [2880, 540, 3840, 1080, "minismurf"],
    [0, 0, 960, 540, "smurf1"],
    [960, 0, 1920, 540, "smurf2"],
    [0, 540, 960, 1080, "smurf3"],
    [1920, 0, 2880, 540, "smurf4"],
    [2880, 0, 3840, 540, "smurf5"],
    [1920, 540, 2880, 1080, "smurf6"],
    [3840, 0, 4800, 540, "smurf7"],
    [4800, 0, 5760, 540, "smurf8"],
    [3840, 540, 4800, 1080, "smurf9"],
    [4800, 540, 5760, 1080, "smurf0"]
]
DIAMS_COORDINATES = [
    [746, 62, 823, 78, 'smurf4'],
    [1706, 62, 1783, 78, 'smurf5'],
    [746, 602, 823, 618, 'smurf6'],
    [1706, 602, 1783, 618, 'minismurf'],

    [2666, 62, 2743, 78, 'smurf7'],
    [3626, 62, 3703, 78, 'smurf8'],
    [2666, 602, 2743, 618, 'smurf9'],
    [3626, 602, 3703, 618, 'smurf0'],

    [4586, 62, 4663, 78, 'smurf7'],
    [5546, 62, 5623, 78, 'smurf8'],
    [4586, 602, 4663, 618, 'smurf9'],
    [5546, 602, 5623, 618, 'smurf0']
    ]
    
    screenshot = pyautogui.screenshot(region=(2666, 62, 2743, 78))
    
    
    C:\Program Files\Tesseract-OCR
    
    
    PATH=C:\Program Files (x86)\VMware\VMware Player\bin\;C:\Program Files\Python311\Scripts\;C:\Program Files\Python311\;C:\Program Files\ImageMagick-7.1.0-Q16-HDRI;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\Calibre2\;C:\ProgramData\chocolatey\bin;C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\;C:\tools\BCURRAN3;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files (x86)\dotnet\;C:\Program Files\PuTTY\;C:\Program Files (x86)\Windows Live\Shared;C:\Program Files\Microsoft VS Code\bin;C:\Program Files\nodejs\;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;C:\HashiCorp\Vagrant\bin;C:\Program Files\Git\cmd;C:\Program Files\PowerShell\7\;C:\Users\Roy\scoop\shims;C:\Users\Roy\AppData\Local\Programs\Python\Python39\Scripts\;C:\Users\Roy\AppData\Local\Programs\Python\Python39\;C:\Users\Roy\AppData\Local\Programs\Python\Python38\Scripts\;C:\Users\Roy\AppData\Local\Programs\Python\Python38\;C:\Users\Roy\AppData\Local\Microsoft\WindowsApps;C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.4\bin;C:\Users\Roy\AppData\Local\GitHubDesktop\bin;C:\ProgramData\Stress.portable;;C:\Users\Roy\AppData\Local\Microsoft\WindowsApps;C:\Program Files (x86)\Nmap;C:\Program Files\Oracle\VirtualBox;C:\Users\Roy\AppData\Roaming\npm;C:\Program Files\Tesseract-OCR
    
    
   smurf4 
>>> screenshot = pyautogui.screenshot(region=(770, 62, 58, 20)).convert('L')
>>> screenshot.show()
>>> print(pytesseract.image_to_string(screenshot))
1573

    smurf5

>>> screenshot = pyautogui.screenshot(region=(1810, 62, 48, 15)).convert('L')
>>> print(pytesseract.image_to_string(screenshot))
1146

>>>



Smurf 1: (-1920, 0), 882 x 511
Smurf 2: (-882, 0), 882 x 511
Smurf 3: (-1920, 508), 882 x 511
A Supersmurf: (-883, 507), 882 x 511

Smurf 4: (0, 0), 882 x 511
Smurf 5: (1039, 0), 882 x 511
Smurf 6: (0, 508), 882 x 511
B MiniSmurf: (1038, 508), 882 x 511

Smurf 7: (1920, 0), 882 x 511
Smurf 8: (2960, 0), 882 x 511
Smurf 9: (1921, 508), 882 x 511
Smurf 0: (2957, 508), 882 x 511





[-1920, 0, 882 x 511, "Smurf 1"]
Smurf 2: (-882, 0), 882 x 511
Smurf 3: (-1920, 508), 882 x 511
A Supersmurf: (-883, 507), 882 x 511

Smurf 4: (0, 0), 882 x 511
Smurf 5: (1039, 0), 882 x 511
Smurf 6: (0, 508), 882 x 511
B MiniSmurf: (1038, 508), 882 x 511

Smurf 7: (1920, 0), 882 x 511
Smurf 8: (2960, 0), 882 x 511
Smurf 9: (1921, 508), 882 x 511
Smurf 0: (2957, 508), 882 x 511



SMURFWINDOWS=[
 [-1920, 0, 882, 511, 'Smurf 1'],
 [-882, 0, 882, 511, 'Smurf 2'],
 [-1920, 508, 882, 511, 'Smurf 3'],
 [-883, 507, 882, 511, 'A Supersmurf'],
 [0, 0, 882, 511, 'Smurf 4'],
 [1039, 0, 882, 511, 'Smurf 5'],
 [0, 508, 882, 511, 'Smurf 6'],
 [1038, 508, 882, 511, 'B MiniSmurf'],
 [1920, 0, 882, 511, 'Smurf 7'],
 [2960, 0, 882, 511, 'Smurf 8'],
 [1921, 508, 882, 511, 'Smurf 9'],
 [2957, 508, 882, 511, 'Smurf 0']
]


 
