import arcpy
from layer_cfg_parser import layer_cfg
mxd =layer_cfg()
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    print "Exporting page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
    arcpy.mapping.ExportToPNG(mxd, r"E:\jilin_carto\output" + str(pageNum) + ".png")
del mxd