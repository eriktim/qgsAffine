from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import Ui_ui

from qgis.core import *
from qgis.gui import *

#from ui_control import ui_Control
import resources

class qgsAffine(QDialog, Ui_ui):

    def __init__(self, iface):
        self.iface = iface
        QDialog.__init__(self, iface.mainWindow())
        self.setupUi(self)
        
    def initGui(self):
        # create action that will start plugin configuration
        self.action = QAction(QIcon(":qgsAffine.png"), "Affine (Rotation, Translation, Scale)", self.iface.mainWindow())
        self.action.setWhatsThis("Configuration for test plugin")
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
    
        # add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)

        #add to Vector menu
        nextAction = self.iface.mainWindow().menuBar().actions()[3].menu().actions()[3]
        self.iface.mainWindow().menuBar().actions()[3].menu().insertAction(nextAction,self.action)
        if hasattr(self.iface, "addPluginToVectorMenu"):
            self.iface.addPluginToVectorMenu("&Geoprocessing Tools", self.action)
        else:
            self.iface.addPluginToMenu("&Geoprocessing Tools", self.action)
        #self.action.setEnabled(False)
        
        
        #INSERT EVERY SIGNAL CONECTION HERE!
        QObject.connect(self.pushButtonRun,SIGNAL("clicked()"),self.affine)
        QObject.connect(self.pushButtonInvert,SIGNAL("clicked()"),self.invert)


    def unload(self):
        # remove the plugin menu item and icon
        if hasattr(self.iface, "addPluginToVectorMenu"):
            self.iface.removePluginVectorMenu("&Geoprocessing Tools", self.action)
        else:
            self.iface.removePluginMenu("&Geoprocessing Tools", self.action)
        self.iface.removeToolBarIcon(self.action)
    
    
    def run(self):
        # create and show a configuration dialog or something similar
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint  # QgisGui.ModalDialogFlags
        self.comboBoxLayer.clear()
        for item in self.listlayers(0):
            self.comboBoxLayer.addItem(item)
        
        self.show()
    
    def listlayers(self,layertype):
        layersmap=QgsMapLayerRegistry.instance().mapLayers()
        layerslist=[]
        for (name,layer) in layersmap.iteritems():
            if (layertype==layer.type()):
                layerslist.append(layer.name())
        return layerslist
    
    def getLayerByName(self,layername):
        layersmap=QgsMapLayerRegistry.instance().mapLayers()
        for (name,layer) in layersmap.iteritems():
            if (layername==layer.name()):
                return layer
    #Now these are the SLOTS
    def affine(self):
        self.a=float(self.lineEditA.text())
        self.b=float(self.lineEditB.text())
        self.tx=float(self.lineEditTx.text())
        self.c=float(self.lineEditC.text())
        self.d=float(self.lineEditD.text())
        self.ty=float(self.lineEditTy.text())
        self.doaffine()
        
    def invert(self):
        try:
            # matrix form: x' = A x + b
            # --> x = A^-1 x' - A^-1 b
            # A^-1 = [d -b; -c a] / det A
            # only valid if det A = a d - b c != 0
            det = self.a*self.d - self.b*self.c
            if not det:
                print "Transformation is not invertable"
                return
            a=self.d/det
            b=-self.b/det
            c=-self.c/det
            d=self.a/det
            tx=-a*self.tx-b*self.ty
            ty=-c*self.tx-d*self.ty
            self.lineEditA.setText(str(a))
            self.lineEditB.setText(str(b))
            self.lineEditC.setText(str(c))
            self.lineEditD.setText(str(d))
            self.lineEditTx.setText(str(tx))
            self.lineEditTy.setText(str(ty))
            self.affine()
            #print "ok"
        except:
            print "Nothing to invert"
    
    def doaffine(self):
	warn=QgsMessageViewer()
        vlayer=self.getLayerByName(self.comboBoxLayer.currentText())
        if (self.radioButtonWholeLayer.isChecked()):
            vlayer.removeSelection()
            vlayer.invertSelection()
        featids=vlayer.selectedFeaturesIds()
        provider=vlayer.dataProvider()
        result={}
        features={}
        if (vlayer.geometryType()==2):
            start=1
        else:
            start=0
        print vlayer.name()
        if (not vlayer.isEditable()):
	    warn.setMessageAsPlainText("Layer not in edit mode.")
	    warn.showMessage()
	else:
	    for fid in featids:
		features[fid]=QgsFeature()
                if not vlayer.getFeatures( QgsFeatureRequest().setFilterFid( fid ) ).nextFeature( features[fid] ):
                    continue;
		result[fid]=features[fid].geometry()
		i=start
		vertex=result[fid].vertexAt(i)
		while (vertex!=QgsPoint(0,0)):
                    # matrix form: x' = A x + b
                    # x' = a x + b y + tx
                    # y' = c x + d y + ty
		    newx=self.a*vertex.x()+self.b*vertex.y()+self.tx
		    newy=self.c*vertex.x()+self.d*vertex.y()+self.ty
		    #geom.
		    #print vertex.x(), vertex.y(), newx, newy
		    vlayer.moveVertex(newx,newy,fid,i)
		    #print vertex.x,vertex.y,newx,newy,fid,i
		    i+=1
		    vertex=result[fid].vertexAt(i)
	    #vlayer.commitChanges()
	    #vlayer.updateExtents()
	    #vlayer.updateGeometryValues(result)
	    
	    self.iface.mapCanvas().zoomToSelected()
        #self.iface.mapCanvas().refresh()
        #print "ok"
