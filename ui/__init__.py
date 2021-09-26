class Blend4vcamProperties(PropertyGroup):

    blend4vcam_filepath : bpy.props.StringProperty(
        name="Filepath",
        description="Define path for exported files",
        default="",
        subtype = "DIR_PATH",
        maxlen=1024,
    )
    blend4vcam_selected_only = bpy.props.BoolProperty(
        name="Selected Only",
        description="Export only selected cameras",
        default = True
    )
    blend4vcam_multiple_files = bpy.props.BoolProperty(
        name="Multiple Files",
        description="If more than one cameras are selected, export them in separate files",
        default = True
    )
    blend4vcam_write_to_textblock = bpy.props.BoolProperty(
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