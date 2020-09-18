
import bpy
from bpy.types import Operator

class HOTKEYSAMPLE_MT_mergecenter(Operator):
    bl_idname = "hotkeysample.mergecenter"
    bl_label = "merge center"
     
    def execute(self, context):
    
    	#ここにコマンドを書く
        bpy.ops.mesh.merge(type='CENTER')
        return {'FINISHED'}  
    
classes = (
    HOTKEYSAMPLE_MT_mergecenter,
)

addon_keymap = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    active_keyconfig = wm.keyconfigs.active

    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        #typeに押すキー alt,shift,ctrlを使いたい場合はTrueにする
        kmi = km.keymap_items.new(idname='hotkeysample.mergecenter', type='W', value='PRESS', alt=True , shift = True ,ctrl = False)
        addon_keymap.append((km, kmi))



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    for km,kmi in addon_keymap:
        km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()