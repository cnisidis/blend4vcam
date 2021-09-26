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
from bpy.app.handlers import persistent
from ui import Blend4vcamProperties, Blend4v_PT_Blend4vcam
# from bpy.utils import register_module, unregister_module

from . import exporter as exp
from . import importer as imp

# if "bpy" in locals():
#     import imp
#     imp.reload(exporter)
#     print("Reloaded multifiles")
# else:
#     from . import exporter
#     print("Imported multifiles")
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
#    operators
# ------------------------------------------------------------------------

class OP_blend4vcam_Export(bpy.types.Operator):
    bl_idname = "wm.blend4vcam"
    bl_label = "Export"

    def execute(self, context):
        scene = context.scene
        #b4vc
        blend4vcam = scene.blend4vcam
        custompath = blend4vcam.blend4vcam_filepath
        bselectedOnly = blend4vcam.blend4vcam_selected_only
        bTextBlock =blend4vcam.blend4vcam_write_to_textblock
        bMultipleF =  blend4vcam.blend4vcam_multiple_files
        # print the values to the console
        print("Blend - 4v Camera Exporting ...")
        print("Slected Only:", bselectedOnly)
        print("Multiple Files:", bMultipleF)
        print("WriteToTextBlock:", bTextBlock)
        if (custompath=="" or custompath == None):
            blendfilepath = setDataPath()
            if blendfilepath == 0:
                self.report({'WARNING'},"Blend File must be saved")
                return {'FINISHED'}
            print(blendfilepath)
        elif (os.path.isdir(custompath)):
            blendfilepath = custompath
        else:
            print(custompath+' it is not a valid path')
            print(repr(custompath))
            print(os.path.isdir(repr(custompath)))
            return {'CANCELLED'}
        context = defineContext()
        if exp.GetCameras(bselectedOnly, context):
            exp.GetCameraData(blendfilepath, bTextBlock, bMultipleF )
        else:
            return {'CANCELLED'}

        '''TODO Export file or Multiple Files exp.files()
        '''


        return {'FINISHED'}

# ------------------------------------------------------------------------
#    menus
# ------------------------------------------------------------------------

class Blend4vcamBasicMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_test"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout



'''
REGISTER CLASSES + TYPES

'''

classes = (
    OP_blend4vcam_Export,
    Blend4v_PT_Blend4vcam,
    Blend4vcamBasicMenu

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
