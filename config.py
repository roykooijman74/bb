"""Configuration settings for the daily chores automation"""

# Window configurations
SMURF_WINDOWS = [
    [2560, 0, 790, 460, "Smurf 1"],
    [3414, 0, 790, 460, "Smurf 2"],
    # ... rest of the windows
]

# Coordinate configurations
COORDINATES = {
    'play_button': {'x': 465, 'y': 14},
    'npc_location': {'x': 356, 'y': 257},
    'brown_destroy': {'x': 395, 'y': 202},
    'green_destroy': {'x': 437, 'y': 312},
}

# Image detection configurations
DETECTION_SETTINGS = {
    'confidence_threshold': 0.6,
    'region_adjustment': 3,
}

# Color detection settings
COLOR_VARIANCE = 5 