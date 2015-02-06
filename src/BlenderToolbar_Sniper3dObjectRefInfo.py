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
            for obj in bpy.context.selected_objects:
                self.exportCollisionShape(obj)
        if(self.number==21):
            print("\n\n\n\n**************** SCENE RIGID BODIES ***************")
            myobj=bpy.context.active_object
            self.exportRigidBodies(myobj)
            for obj in bpy.context.selected_objects:
                self.exportRigidBodies(obj)
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
        print('},')
        return('FINISH')
    def exportRigidBodies(self,obj):
        print('/* ',obj.name,' */')
        print('{')
        print('    "btbodyid": ,')
        print('    "score":0,')
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
        ',"z":',round(aY,5),'},')
        print('    "collisionshapeid": ,')
        print('    "mass":0,')
        print('    "inertia":{"x":0,"y":0,"z":0}')
        print('},')
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
        #col = layout.column(align=True)
        box=row.box()
        box.label(text="Print Sniper3D Space Info")
        box.operator("sniper3d.infobutton",text="Sniper3D space Full OBJ Info").number=2
        box.operator("sniper3d.infobutton",text="Sniper3D space Coordinates only").number=4
        box.label(text="Print Blender Space Info")
        box.operator("sniper3d.infobutton",text="Blender space info Pos coordinates only").number=3
        
        row=layout.row()
        #col=layout.column(align=True)
        box=row.box()
        box.label(text="Export Collision btBoxShapes and")
        box.label(text="RigidBodies in Sniper3D space")
        box.operator('sniper3d.infobutton',text='Export Collision btBoxShapes').number=20
        #box.label(text='Export Scene3D rigid bodies')
        box.operator('sniper3d.infobutton',text='Export Scene3D Rigid Bodies').number=21
        
        row=layout.row()
        box=row.box()
        box.label(text="Targets Info")
        box.operator('sniper3d.infobutton',text='Export Selected Sniper Targets').number=10
        box.operator('sniper3d.infobutton',text='Export CSV Targets Info').number=11
        
def register():
    bpy.utils.register_class(OBJECT_OT_Sniper3dInfoButton)
    bpy.utils.register_class(SniperObjectInfoPanel)
    #bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_class(SniperObjectInfoPanel)
    
if __name__== "__main__":
    register()

#bpy.utils.register_module(__name__)    

     


