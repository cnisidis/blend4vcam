import bpy
import bpy.app.handlers
import os
# ------------------------------------------------------------------------
#    operators
# ------------------------------------------------------------------------


'''
for persistent data file must be saved
otherwise create a block
'''


class Blend4vcam_OT_Operator(bpy.types.Operator):

    bl_idname = "blend4vcam.export"
    bl_label = "Export"
    '''
    create a text block in text editor, if the block already exists then update it, if otherwise (false) create a new one
    '''
    def CreateTBlock(update_block=True):
        if update_block:
            #check if this TBlock exists
            #update existed block
            #else call self with update False
            pass
        else:
            #create new block
            #assign id to this block
            pass
        pass

    blendfilepath = None
     #b4vc
    scene           = bpy.context.scene
    blend4vcam      = scene.blend4vcam
    custompath      = blend4vcam.string_filepath
    bselectedOnly   = blend4vcam.bool_selected_only
    bTextBlock      = blend4vcam.bool_write_to_textblock
    bMultipleF      = blend4vcam.bool_multiple_files
    #@persistent
    def setDataPath(self):
        if bpy.data.is_saved:
            self.blendfilepath = bpy.path.native_pathsep(bpy.data.filepath)
        else:
            print("A Text Block has been Created")
        return self.blendfilepath


    def execute(self, context):
        
       
        # print the values to the console
        print("Blend - 4v Camera Exporting ...")
        print("Slected Only:", self.bselectedOnly)
        print("Multiple Files:", self.bMultipleF)
        print("WriteToTextBlock:", self.bTextBlock)
        
        if self.custompath=="" or self.custompath == None:
            self.blendfilepath = self.setDataPath()
            if self.blendfilepath == 0:
                self.report({'WARNING'},"Blend File must be saved")
                return {'FINISHED'}
            print(self.blendfilepath)
        elif os.path.isdir(self.custompath):
            self.blendfilepath = custompath
        else:
            print(self.custompath+' it is not a valid path')
            print(repr(self.custompath))
            print(os.path.isdir(repr(self.custompath)))
            return {'CANCELLED'}
        
        
        '''TODO Export file or Multiple Files exp.files()
        '''


        return {'FINISHED'}

    