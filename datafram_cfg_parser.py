from mxd_cfg_parser import mxd_cfg
from cfg import cfgs
import arcpy
def datafram_cfg():
    cfg = cfgs()
    layname = cfg.get('dataframe','name')
    mxd = mxd_cfg()
    df =arcpy.mapping.ListDataFrames(mxd,layname)[0]
    df.rotation =cfg.get('dataframe','rotation')
    df.scale = cfg.get('dataframe','scale')
    df.displyUnits = cfg.get('dataframe','displyUnits')
    mxd.save()
    print "finshed datafram update"
    return df ,mxd

if __name__ =='__main__':
    datafram_cfg()