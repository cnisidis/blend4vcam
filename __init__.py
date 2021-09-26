bl_info = {
    "name": "blend4vcam",
    "description": "vvvv - blender camera exchange toolset",
    "author": "cnisidis http://nisidis.com",
    "version": (0, 1, 2),
    "blender": (2, 93, 0),
    "location": "",
    "warning": "WIP", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "support": "TESTING",
    "category": "Tools"
}

import bpy

from ui import Blend4vcamProperties, Blend4v_PT_Panel
from op import Blend4vcam_OT_Operator

from . import exporter as exp
from . import importer as imp



classes = (
    Blend4vcam_OT_Operator,
    Blend4v_PT_Panel,
    Blend4vcamProperties
)

register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
   
    register_classes()
    bpy.types.Scene.blend4vcam =  bpy.props.PointerProperty(type=Blend4vcamProperties)
    #bpy.app.handlers.load_post.append(setDataPath)
    #bpy.app.handlers.load_post.append(defineContext)

def unregister():
    unregister_classes()
    del bpy.types.Scene.blend4vcam

# if __name__ == "__main__":
#     register()
