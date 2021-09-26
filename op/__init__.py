import bpy
import bpy.app.handlers
import sys
import os
# ------------------------------------------------------------------------
#    operators
# ------------------------------------------------------------------------

class Blend4vcam_OT_Operator(bpy.types.Operator):

    #@persistent
    def setDataPath():
        if bpy.data.is_saved:
            blendfilepath = bpy.path.native_pathsep(bpy.data.filepath)
        else:
            return 0
        return blendfilepath

    bl_idname = "blend4vcam.export"
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
            blendfilepath = self.setDataPath()
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
        context = bpy.context
        

        '''TODO Export file or Multiple Files exp.files()
        '''


        return {'FINISHED'}