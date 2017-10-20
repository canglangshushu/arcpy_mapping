from cfg import cfgs
import arcpy
def mxd_cfg():
    arcpy.env.workspace = r"C:\Users\11422\Desktop"
    cfg = cfgs()
    path = cfg.get('mxd','mxdpath')
    mxd = arcpy.mapping.MapDocument(path)
    mxd.author = cfg.get('mxd','author')
    mxd.activeView = cfg.get('mxd','activeView')
    mxd.title = cfg.get('mxd','title')
    mxd.credits = cfg.get('mxd','credits')
    mxd.description = cfg.get('mxd','description')
    mxd.hyperlinkBase = cfg.get('mxd','hyperlinkBase')
    mxd.relativePaths = cfg.getboolean('mxd','relativePaths')
    mxd.summary = cfg.get('mxd','summary')
    mxd.tags = cfg.get('mxd','tags')
    mxd.save()
    print "finshed MXD document upgrade"
    return mxd
#if __name__ =='__main__':
    #mxd_cfg()
