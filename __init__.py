bl_info = {
    "name": "Blender Addon Template",
    "blender": (4, 0, 0),
    "category": "Object",
    "version": (0, 0, 0),
    "author": "{Your Name}",
    "description": "",
}

from . import operators
from . import ui_panel
from . import draw_aabb
from . import gizmo_group

def register():
    pass

def unregister():
    pass
