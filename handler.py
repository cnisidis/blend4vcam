reports =[];

class b4vReport(bpy.type.Operator):
    bl_idname = 'render.b4vError'
    bl_label = 'blend4vcam:'
    bl_options = {'REGISTER', 'UNDO'}

    message =''
    type=''

    def execute(self, context):
        self.report({self.type}), self.message)
        reports.append(self.type, self.message)
        return {'FINISHED'}
