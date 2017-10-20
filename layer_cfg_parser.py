from cfg import cfgs
import arcpy
from datafram_cfg_parser import datafram_cfg
def layer_cfg():
    cfg = cfgs()
    df,mxd = datafram_cfg()
    name = cfg.get('layer','name')
    path = cfg.get('layer','path')
    symbology_valueField = cfg.get('layer','symbology_valueField')
    symbologyType =cfg.get('layer','symbologyType')
    symbology_numClasses = cfg.get('layer','symbology_numClasses')
    lyr= arcpy.mapping.ListLayers(mxd,name,df)[0]
    lyrfile = arcpy.mapping.Layer(path)
    arcpy.mapping.UpdateLayer(df,lyr,lyrfile,True)
    if  lyr.symbologyType == symbologyType:
        lyr.symbology.valueField = symbology_valueField
        lyr.symbology.numClasses = symbology_numClasses
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        mxd.save()
        print "finshed layer update"
    return mxd
if __name__ =='__main__':
    layer_cfg()





