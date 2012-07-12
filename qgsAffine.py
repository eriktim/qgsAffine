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
        QObject.connect(self.pushButton,SIGNAL("clicked()"),self.affine)
        QObject.connect(self.pushButton_2,SIGNAL("clicked()"),self.undo)


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
        self.comboBox.clear()
        for item in self.listlayers(0):
            self.comboBox.addItem(item)
        
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
        self.a=float(self.lineEdit.text())
        self.b=float(self.lineEdit_4.text())
        self.c=float(self.lineEdit_5.text())
        self.d=float(self.lineEdit_3.text())
        self.e=float(self.lineEdit_2.text())
        self.f=float(self.lineEdit_6.text())
        self.doaffine()
        
    def undo(self):
        try:
            #print self.a, self.b, self.c,self.d,self.e,self.f
            self.a=1/self.a
            self.b=-self.b
            self.c=-self.c
            self.d=-self.d
            self.e=1/self.e
            self.f=-self.f
            #print "ok"
            self.doaffine()
        except:
            print "Nothing to undo"
    
    def doaffine(self):
	warn=QgsMessageViewer()
        vlayer=self.getLayerByName(self.comboBox.currentText())
        if (self.radioButton_2.isChecked()):
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
		vlayer.featureAtId(fid,features[fid])
		result[fid]=features[fid].geometry()
		i=start
		vertex=result[fid].vertexAt(i)
		while (vertex!=QgsPoint(0,0)):
		    newx=self.a*vertex.x()+self.b*vertex.y()+self.c
		    newy=self.d*vertex.x()+self.e*vertex.y()+self.f
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
