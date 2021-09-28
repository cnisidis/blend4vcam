import bpy
import bpy.app.handlers
import os
from . Export import Exporter
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
    bl_options = {'REGISTER'}
    '''
    create a text block in text editor, if the block already exists then update it, if otherwise (false) create a new one
    '''
    def CreateOrOpenTextBlock(self, update_block=True):
        text_block_name = 'test'
        text_block = None
        if update_block:
            #check if this TBlock exists
            try:
                print("Updating New Text Block ..")
                text_block = bpy.data.texts[text_block_name]
                print("New Text Block Updated")
                #update existed block
            except KeyError:
                #else call self with update False
                self.CreateOrOpenTextBlock(update_block = False)
        else:
            #create new block
            print("Creating new Text Block ...")
            text_block = bpy.data.texts.new(text_block_name)
            print("new text block created: " + text_block_name)
            #assign id to this block
            
        

    blendfilepath = None
    exporter = Exporter()
    
    #b4vc
    
    #@persistent
    def setDataPath(self):
        if bpy.data.is_saved:
            self.blendfilepath = bpy.path.native_pathsep(bpy.data.filepath)
        else:
            self.blendfilepath = None
            self.CreateOrOpenTextBlock()



    def execute(self, context):


        scene           = context.scene
        blend4vcam      = scene.blend4vcam
        custompath      = blend4vcam.string_filepath
        bselectedOnly   = blend4vcam.bool_selected_only
        bTextBlock      = blend4vcam.bool_write_to_textblock
        bMultipleF      = blend4vcam.bool_multiple_files
        
        # print the values to the console
        print("Blend - 4v Camera Exporting ...")
        print("Slected Only:", bselectedOnly)
        print("Multiple Files:", bMultipleF)
        print("WriteToTextBlock:", bTextBlock)
        #Exporter check
        self.exporter.isAlive()

        #check if camera is selected

        #check if textblock is selected
        if bTextBlock == True:
            self.CreateOrOpenTextBlock()
        
        #check custom path
        if custompath=="" or custompath == None:
            self.setDataPath()
            if self.blendfilepath == None:
                self.report({'WARNING'},"Blend File must be saved")
                return {'FINISHED'}
            print(self.blendfilepath)
        
        elif os.path.isdir(custompath):
            self.blendfilepath = custompath
        else:
            print(custompath+' it is not a valid path')
            print(repr(custompath))
            print(os.path.isdir(repr(custompath)))
            return {'CANCELLED'}
        
        
        '''
            TODO Export file or Multiple Files exp.files()
        '''
        
        
       
        return {'FINISHED'}

    