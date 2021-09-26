import bpy
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