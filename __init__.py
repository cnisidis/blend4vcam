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
# from bpy.utils import register_module, unregister_module


from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       PropertyGroup
                       )
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

class Blend4vcamSettings(PropertyGroup):

    blend4vcam_filepath = StringProperty(
        name="Filepath",
        description="Define path for exported files",
        default="",
        subtype = "DIR_PATH",
        maxlen=1024,
    )
    blend4vcam_selected_only = BoolProperty(
        name="Selected Only",
        description="Export only selected cameras",
        default = True
    )
    blend4vcam_multiple_files = BoolProperty(
        name="Multiple Files",
        description="If more than one cameras are selected, export them in separate files",
        default = True
    )
    blend4vcam_write_to_textblock = BoolProperty(
        name="Write To TextBlock",
        description="Write Camera Data in a Textblock instead of exporting it as a file (useful for debugging or packaging)",
        default = False
    )
    # blend4vcam_export_path = StringProperty(
    #   name = "Export Path",
    #   default = default_path,
    #   description = "Define path to export",
    #   subtype = "DIR_PATH"
    # )
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


class OBJECT_PT_Blend4vcam(Panel):
    bl_idname = "OBJECT_PT_Blend4vcam"
    bl_label = "CAMERA to VVVV (XML)"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "vvvv | VL"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        blend4vcam = scene.blend4vcam

        #layout.prop(mytool, "my_bool")
        #layout.prop(mytool, "my_enum", text="")
        #layout.prop(mytool, "my_int")
        layout.prop(blend4vcam, "blend4vcam_filepath")
        layout.prop(blend4vcam, "blend4vcam_selected_only")
        layout.prop(blend4vcam, "blend4vcam_multiple_files")
        layout.prop(blend4vcam, "blend4vcam_write_to_textblock")
        layout.operator("wm.blend4vcam")
        #layout.menu("OBJECT_MT_select_test", text="Presets", icon="SCENE")

'''
REGISTER CLASSES + TYPES
'''

classes = (
    OP_blend4vcam_Export,
    OBJECT_PT_Blend4vcam,
    Blend4vcamSettings,
    Blend4vcamBasicMenu

)
register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
   
    register_classes()
    bpy.utils.register_module(__name__)
    bpy.types.Scene.blend4vcam = PointerProperty(type=Blend4vcamSettings)
    bpy.app.handlers.load_post.append(setDataPath)
    bpy.app.handlers.load_post.append(defineContext)

def unregister():
   
    unregister_classes()
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.blend4vcam

# if __name__ == "__main__":
#     register()
