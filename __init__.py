bl_info = {
    "name": "blend4vcam",
    "description": "vvvv - blender camera exchange toolset",
    "author": "cnisidis http://nisidis.com",
    "version": (0, 0, 2),
    "blender": (2, 93, 0),
    "location": "",
    "warning": "WIP", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "support": "TESTING",
    "category": "Tools"
}

import bpy
import sys
import os
from ui import Blend4vcamProperties, Blend4v_PT_Blend4vcam
from op import OP_blend4vcam_Export

from . import exporter as exp
from . import importer as imp

@persistent
def setDataPath():
    if bpy.data.is_saved:
        blendfilepath = bpy.path.native_pathsep(bpy.data.filepath)
    else:
        return 0
    return blendfilepath

@persistent
def defineContext():
    return bpy.context




# ------------------------------------------------------------------------
#    menus
# ------------------------------------------------------------------------

# class Blend4vcamBasicMenu(bpy.types.Menu):
#     bl_idname = "OBJECT_MT_select_test"
#     bl_label = "Select"

#     def draw(self, context):
#         layout = self.layout



'''
REGISTER CLASSES + TYPES

'''

classes = (
    OP_blend4vcam_Export,
    Blend4v_PT_Blend4vcam,
    #Blend4vcamBasicMenu

)
register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
   
    register_classes()
    # bpy.types.Scene.blend4vcam = PointerProperty(type=Blend4vcamProperties)
    bpy.types.Scene.blend4vcam =  bpy.props.PointerProperty(type=Blend4vcamProperties)
    bpy.app.handlers.load_post.append(setDataPath)
    bpy.app.handlers.load_post.append(defineContext)

def unregister():
   
    unregister_classes()
    del bpy.types.Scene.blend4vcam

# if __name__ == "__main__":
#     register()
