# author: Alexander Bigel
# Panel with copy and paste object coordinates.
# The script is not installing automaticly as blender addon.  
# Script need to run from the scripting layout in blender.


 

import bpy
from bpy.props import *
import math


bl_info={
    "name": "Copy and paste object coordinates",
    "description":" Panel tool on VIEW_3D which help copy and paste active object coordinates",
    "version":"1.0",
    "category": "3D View",
    "location": "View3D > User Interface > Copy object coordinates",
    "warning": "",  
    "wiki_url": "",  
    "tracker_url": "", 
    "author": "Alexander Bigel"
}
A
def initCopyPastePanelProperties(scn):
    """defien properties for panel"""
    bpy.types.Scene.CopyPastePanelLocationBool=BoolProperty(
    name="Location",
    description="True or False?",
    default=True)
    scn['CopyPastePanelLocationBool']=True
    
    bpy.types.Scene.CopyPastePanelRotationBool=BoolProperty(
    name="Rotation",
    description="True or False?",
    default=True)
    scn['CopyPastePanelRotationBool']=True

    bpy.types.Scene.CopyPastePanelLocationX=FloatProperty(
    name="Float",
    description="Object Location X",
    default=0)
    
    bpy.types.Scene.CopyPastePanelLocationY=FloatProperty(
    name="Float",
    description="Object Location Y",
    default=0)
    
    bpy.types.Scene.CopyPastePanelLocationZ=FloatProperty(
    name="Float",
    description="Object Location Z",
    default=0)
    
    bpy.types.Scene.CopyPastePanelRotationX=FloatProperty(
    name="Float",
    description="Object Rotation X",
    default=0)
    
    bpy.types.Scene.CopyPastePanelRotationY=FloatProperty(
    name="Float",
    description="Object Rotation Y",
    default=0)
    
    bpy.types.Scene.CopyPastePanelRotationZ=FloatProperty(
    name="Float",
    description="Object Rotation Z",
    default=0)

def delCopyPastePanelProperties():
    del bpy.types.Scene.CopyPastePanelLocationBool
    del bpy.types.Scene.CopyPastePanelRotationBool
    
    del bpy.types.Scene.CopyPastePanelLocationX
    del bpy.types.Scene.CopyPastePanelLocationY
    del bpy.types.Scene.CopyPastePanelLocationZ
    
    del bpy.types.Scene.CopyPastePanelRotationX
    del bpy.types.Scene.CopyPastePanelRotationY
    del bpy.types.Scene.CopyPastePanelRotationZ

class OBJECT_OT_CoordActionPanelButton(bpy.types.Operator):
    """Reaction on button, print information about object in blender coordinates"""
    bl_idname="coordactionpanelbutton.button"
    bl_label="Button"
    number = bpy.props.IntProperty()
    
    def execute(self,context):
        if(self.number==1):
            myobj=bpy.context.active_object
            scn=context.scene
            if(scn['CopyPastePanelLocationBool']==True):
                scn['CopyPastePanelLocationX']=myobj.location.x
                scn['CopyPastePanelLocationY']=myobj.location.y 
                scn['CopyPastePanelLocationZ']=myobj.location.z
            if(scn['CopyPastePanelRotationBool']==True):
                scn['CopyPastePanelRotationX']=math.degrees(myobj.rotation_euler[0])
                scn['CopyPastePanelRotationY']=math.degrees(myobj.rotation_euler[1])
                scn['CopyPastePanelRotationZ']=math.degrees(myobj.rotation_euler[2])
        if(self.number==2):
            myobj=bpy.context.active_object
            for item in bpy.context.selectable_objects:  
                item.select = False 
            myobj.select=True
            scn=context.scene
            if(scn['CopyPastePanelLocationBool']==True):
                myobj.location.x=scn['CopyPastePanelLocationX']
                myobj.location.y =scn['CopyPastePanelLocationY']
                myobj.location.z=scn['CopyPastePanelLocationZ']
            if(scn['CopyPastePanelRotationBool']==True):
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=False) #apply rotation
                t_rot=(math.radians(scn['CopyPastePanelRotationX']),
                       math.radians(scn['CopyPastePanelRotationY']),
                       math.radians(scn['CopyPastePanelRotationZ']))
                myobj.rotation_mode='XYZ'
                myobj.rotation_euler=(t_rot)                
        return{'FINISHED'}    

    

class CoordinatesCopierPanel(bpy.types.Panel):
    """ Coordinates copier panel"""
    bl_label="Copy object coordinates"
    bl_space_type="VIEW_3D"
    bl_region_type="TOOLS"
    #bl_context="objectmode"
        
    def draw(self, context):
        layout=self.layout
        scn=context.scene
        
        row=layout.row()
        #box=row.box()
        col=row.column()
        col.label(text="Copy, paste location and rotation")
        col.operator("coordactionpanelbutton.button",text="Copy").number=1
        row=col.row()
        row.prop(scn,"CopyPastePanelLocationBool")
        row.prop(scn,"CopyPastePanelRotationBool")  
        
        split = layout.split()

        col = split.column()
        sub = col.column(align=True)
        sub.label(text="Location:")
        sub.prop(scn, "CopyPastePanelLocationX", text="X")
        sub.prop(scn, "CopyPastePanelLocationY", text="Y")
        sub.prop(scn, "CopyPastePanelLocationZ", text="Z")

        split = layout.split()

        col = split.column()
        sub = col.column(align=True)
        sub.label(text="Rotation:")
        sub.prop(scn, "CopyPastePanelRotationX", text="X")
        sub.prop(scn, "CopyPastePanelRotationY", text="Y")
        sub.prop(scn, "CopyPastePanelRotationZ", text="Z")
       
        row=layout.row()
        col.operator("coordactionpanelbutton.button",text="Paste").number=2
       
def register():
    initCopyPastePanelProperties(bpy.context.scene)
    bpy.utils.register_class(OBJECT_OT_CoordActionPanelButton)
    bpy.utils.register_class(CoordinatesCopierPanel)
    #bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_CoordActionPanelButton)
    bpy.utils.unregister_class(CoordinatesCopierPanel)
    delCopyPastePanelProperties()
if __name__== "__main__":
    register()

#bpy.utils.register_module(__name__)    
