#Blender 3D editor toolbar panel with buttons.
#Buttons print information of the objects for my game in console.
#If you have questions call me in Skype alexander.bigel


import bpy

import math

class OBJECT_OT_Sniper3dInfoButton(bpy.types.Operator):
    """Reaction on button, print information about object in blender coordinates"""
    bl_idname="sniper3d.infobutton"
    bl_label="Button"
    number = bpy.props.IntProperty()
    
    def execute(self,context):
        if(self.number==1):
            print('\n\n=================')
            myobj=bpy.context.active_object
            print('Blender space info Object name:',myobj.name)
            pX=myobj.location.x
            pY=myobj.location.y
            pZ=myobj.location.z
            aX=math.degrees(myobj.rotation_euler[0])
            aY=math.degrees(myobj.rotation_euler[1])
            aZ=math.degrees(myobj.rotation_euler[2])
            print('{')
            print('     "id":"',myobj.name,',')
            print('     "objectid":',myobj.name,',')
            print('     "lights":[1],')
            print('     "position":{')
            print('         "x":',round(pX,5),',')
            print('         "y":',round(pY,5),',')
            print('         "z":',round(pZ,5),)
            print('     },')
            print('     "rotation":{"x":',round(aX,5),
            ',"y":',round(aY,5),
            ',"z":',round(aZ,5),'}')
            print('}')            
        if(self.number==2):
            print('\n\n----------------')
            myobj=bpy.context.active_object
            print('Sniper3D space info Object name:',myobj.name)
            pX=myobj.location.x
            pY=myobj.location.y
            pZ=myobj.location.z
            aX=math.degrees(myobj.rotation_euler[0])
            aY=math.degrees(myobj.rotation_euler[1])
            aZ=math.degrees(myobj.rotation_euler[2])
            ppY=0-pY
            print("{")
            print('     "id":"',myobj.name,',')
            print('     "objectid":',myobj.name,',')
            print('     "lights":[1],')
            print('     "position":{')
            print('         "x":',round(pX,5),',')
            print('         "y":',round(pZ,5),',')
            print('         "z":',round(ppY,5),)
            print('     },')
            print('     "rotation":{"x":',round(aX,5),
            ',"y":',round(aZ,5),
            ',"z":',round(aY,5),'}')   
            print('}')
        if(self.number==3):
            print('\n\n=================')
            myobj=bpy.context.active_object
            print('Blender space info Object name:',myobj.name)
            pX=myobj.location.x
            pY=myobj.location.y
            pZ=myobj.location.z
            aX=math.degrees(myobj.rotation_euler[0])
            aY=math.degrees(myobj.rotation_euler[1])
            aZ=math.degrees(myobj.rotation_euler[2])
            print('"position":{')
            print('    "x":',round(pX,5),',')
            print('    "y":',round(pY,5),',')
            print('    "z":',round(pZ,5),)
            print('},')
            print('     "rotation":{"x":',round(aX,5),
            ',"y":',round(aY,5),
            ',"z":',round(aZ,5),'}')
        if(self.number==4):
            print('\n\n----------------')
            myobj=bpy.context.active_object
            print('Sniper3D space info Object name:',myobj.name)
            pX=myobj.location.x
            pY=myobj.location.y
            pZ=myobj.location.z
            aX=math.degrees(myobj.rotation_euler[0])
            aY=math.degrees(myobj.rotation_euler[1])
            aZ=math.degrees(myobj.rotation_euler[2])
            ppY=0-pY
            print('"position":{')
            print('    "x":',round(pX,5),',')
            print('    "y":',round(pZ,5),',')
            print('    "z":',round(ppY,5),)
            print('},')
            print('"rotation":{"x":',round(aX,5),
            ',"y":',round(aZ,5),
            ',"z":',round(aY,5),'}')
        if(self.number==10):
            print('\n\n\n\n\n****************   TARGETS   ****************')
            print('Export targets')
            myobj=bpy.context.active_object
            self.exportTarget(myobj)
            for obj in bpy.context.selected_objects:
                self.exportTarget(obj)
        if(self.number==11):
            print("\n\n\n\n**************** TARGTES CSV ***************")
            myobj=bpy.context.active_object
            self.exportTargetInfoCSV(myobj)
            for obj in bpy.context.selected_objects:
                self.exportTargetInfoCSV(obj)
        if(self.number==20):
            print("\n\n\n\n**************** COLLISION SHAPE ***************")
            myobj=bpy.context.active_object
            self.exportCollisionShape(myobj)
        return{'FINISHED'}    
    def exportTarget(self,obj):
        print('/* ',obj.name,'  */')
        print('{')
        print('    "id": ,')
        print('    "targetid": ,')
        print('    "difficulty":1,')
        print('    "lights":[1],')
        pX=obj.location.x
        pY=obj.location.y
        pZ=obj.location.z
        aX=math.degrees(obj.rotation_euler[0])
        aY=math.degrees(obj.rotation_euler[1])
        aZ=math.degrees(obj.rotation_euler[2])
        ppY=0-pY
        print('    "position":{')
        print('        "x":',round(pX,5),',')
        print('        "y":',round(pZ,5),',')
        print('        "z":',round(ppY,5),)
        print('    },')
        print('    "rotation":{"x":',round(aX,5),
        ',"y":',round(aZ,5),
        ',"z":',round(aY,5),'}')
        print('},')
        return{'FINISHED'}
    def exportTargetInfoCSV(self,obj):
        data=obj.name+';'
        data+=(str(obj.location.x)+';')
        data+=(str(obj.location.y)+';')
        data+=(str(obj.location.z)+';')
        #print(obj.name,',',obj.location.x,',',obj.location.y,',',obj.location.z,',')
        print(data)
        return{'FINISHED'}
    def exportCollisionShape(self,obj):
        print('/* ',obj.name,' */')
        print('{')
        print('    "comment": "',obj.name,'",')
        print('    "id": ,')
        print('    "type":"btBoxShape",')
        print('    "btBoxShape":{')
        print('       "boxHalfExtents":{')
        print('           "x":',round(obj.scale.x,5),',')
        print('           "y":',round(obj.scale.z,5),',')
        print('           "z":',round(obj.scale.y,5))
        print('       }')
        print('    }')
        print('}')
        return('FINISH')
        

class SniperObjectInfoPanel(bpy.types.Panel):
    """ Sniper scene information panel"""
    bl_label="Sniper Scene Information"
    bl_space_type="VIEW_3D"
    bl_region_type="TOOLS"
    #bl_context="objectmode"
    
    def draw(self, context):
        layout=self.layout
        
        #row=layout.row()
        #row.label(text="Print Full Blender Space Info")
        #row=layout.row()
        #row.operator("sniper3d.infobutton",text="Full Obj Blender space info").number=1
        
        row=layout.row()
        col = layout.column(align=True)
        col.label(text="Print full reference")
        col.label(text="Sniper3D Space Info")
        col.operator("sniper3d.infobutton",text="Full obj Sniper3D space info").number=2

        row=layout.row()
        col = layout.column(align=True)
        col.label(text="Print Sniper3D Space Info")
        col.label(text="Coordinates only")
        col.operator("sniper3d.infobutton",text="Pos obj Sniper3D space info").number=4
        
        row=layout.row()
        col = layout.column(align=True)
        col.label(text="Print Blender Space Info")
        col.label(text="Coordinates only")
        col.operator("sniper3d.infobutton",text="Pos Obj Blender space info").number=3
        
        row=layout.row()
        col=layout.column(align=True)
        col.label(text="Export Selected Targets")
        col.operator('sniper3d.infobutton',text='Export Selected Sniper Targets').number=10
        
        row=layout.row()
        col=layout.column(align=True)
        col.label(text="Export CSV Targets")
        col.operator('sniper3d.infobutton',text='Export CSV Targets Info').number=11
        
        ow=layout.row()
        col=layout.column(align=True)
        col.label(text="Export Collision btBoxShape")
        col.operator('sniper3d.infobutton',text='Export Collision btBoxShape Info').number=20
        
        
        
def register():
    bpy.utils.register_class(OBJECT_OT_Sniper3dInfoButton)
    bpy.utils.register_class(SniperObjectInfoPanel)
    #bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_class(SniperObjectInfoPanel)
    
if __name__== "__main__":
    register()

#bpy.utils.register_module(__name__)    

     


