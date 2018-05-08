bl_info = {
    "name": "blend4vcam",
    "description": "vvvv - blender camera exchange toolset",
    "author": "cnisidis http://nisidis.com",
    "version": (0, 0, 1),
    "blender": (2, 70, 0),
    "location": "3D View > Tools",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

import bpy
import sys
import os


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
#import . exporter

if "bpy" in locals():
    import imp
    imp.reload(exporter)
    print("Reloaded multifiles")
else:
    from . import exporter
    print("Imported multifiles")

class Blend4vcamSettings(PropertyGroup):

    blend4vcam_filepath = StringProperty(
        name="Filepath",
        description="Set the absolute path for files to be exported",
        default="//",
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

        # print the values to the console
        print("Blend - 4v Camera Exporting ...")
        print("Slected Only:", blend4vcam.blend4vcam_selected_only)
        print("Multiple Files:", blend4vcam.blend4vcam_multiple_files)

        exp.GetCameras()
        exp.GetCameraData()


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
    bl_label = "Blend - 4v Camera"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
    bl_context = "objectmode"
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
        layout.operator("wm.blend4vcam")
        #layout.menu("OBJECT_MT_select_test", text="Presets", icon="SCENE")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.blend4vcam = PointerProperty(type=Blend4vcamSettings)

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.blend4vcam

if __name__ == "__main__":
    register()
