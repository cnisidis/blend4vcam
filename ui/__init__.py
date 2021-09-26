import bpy

class Blend4vcamProperties(bpy.types.PropertyGroup):
    blend4vcam_filepath             : bpy.props.StringProperty( 'Filepath', description="Define path for exported files", default="", subtype = "DIR_PATH", maxlen=1024)
    blend4vcam_selected_only        : bpy.props.BoolProperty('Selected Only', description="Export only selected cameras", default = True )
    blend4vcam_multiple_files       : bpy.props.BoolProperty('Multiple Files',description="If more than one cameras are selected, export them in separate files", default = True)
    blend4vcam_write_to_textblock   : bpy.props.BoolProperty('Write To TextBlock', description="Write Camera Data in a Textblock instead of exporting it as a file (useful for debugging or packaging)", default = False)
 
class Blend4v_PT_Panel(bpy.types.Panel):
    bl_idname = "Blend4v_PT_Panel"
    bl_label = "CAMERA to VVVV (XML)"
    bl_category = "vvvv | VL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):

        layout = self.layout
        row = layout.row()
        subrow = layout.row(align=True)
        subrow.prop(context.scene.blend4vcam, name="blend4vcam_filepath")
        subrow = layout.row(align=True)
        subrow.prop(context.scene.blend4vcam, name="blend4vcam_selected_only")
        subrow = layout.row(align=True)
        subrow.prop(context.scene.blend4vcam, name="blend4vcam_multiple_files")
        subrow = layout.row(align=True)
        subrow.prop(context.scene.blend4vcam, name="blend4vcam_write_to_textblock")
        subrow = layout.row(align=True)
        subrow.operator("blend4vcam.export")
        #layout.menu("OBJECT_MT_select_test", text="Presets", icon="SCENE")
