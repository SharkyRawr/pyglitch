import os, sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem, QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtGui import QPixmap


"""
from PyQt5 import uic
uic.compileUiDir('ui')
"""
from ui.glitch import Ui_MainWindow


def glitch_file(path, num=1):
    with open(path, 'rb') as f:
        bytes = bytearray(f.read())
        for i in range(num):
            bytes[random.randint(0, len(bytes) - 1)] = random.randint(0, 255)
        return bytes

# Evil evil hack!! FIXME
__main = None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.actionOpen.triggered.connect(self.file_open)
        self.actionMake_animation.triggered.connect(self.tools_makeanimation)

        self.cmdRndGlitch.clicked.connect(self.random_glitch)
        self.cmdSave.clicked.connect(self.save)
        self.sliderNumGlitch.valueChanged.connect(self.numglitch_changed)

        def on_dragenter(self, event):
            #print(event.mimeData().text(), event.mimeData().hasUrls())
            if event.mimeData().hasUrls():
                if not 'file:///' in event.mimeData().text()[:8]:
                    event.ignore()
                    return
                event.accept()
                return
            event.ignore()

        def on_dragdrop(self, event):
            if event.mimeData().hasUrls():
                fileurl = event.mimeData().text()
                if not 'file:///' in fileurl[:8]: return
                print("Dragdrop", fileurl)
                try:
                    filename = fileurl[8:]
                    __main.file_open_readfile(filename)
                except Exception as ex:
                    print(ex)
        
        # Jesus such hackiness... i love it! ♥ >:3
        from types import MethodType
        setattr(self.imgInput, "dragEnterEvent", MethodType(on_dragenter, self.imgInput))
        setattr(self.imgInput, "dropEvent", MethodType(on_dragdrop, self.imgInput))
        self.imgInput.setAcceptDrops(True)
        
        # Worst of the worst -.- HACK FUCKME.. err.. FIXME
        global __main
        __main = self

    def tools_makeanimation(self):
        print("make_animation")
        if not hasattr(self, 'inputfilename'):
            QMessageBox.critical(self, "Error", "Load an image first!",
                                 QMessageBox.Ok)
            return

        numframes, result = QInputDialog.getInt(self, "Make animation", "Number of frames:", 15, min=2, max=1000)
        if result is not True:
            return

        dlg = QFileDialog(self, "Select output directory for frames:")
        dlg.setFileMode(QFileDialog.Directory)
        if not dlg.exec(): return

        outdir = dlg.selectedFiles()[0]
        print("Outdir", outdir)

        def tryload(data):
            pm = QPixmap()
            success = pm.loadFromData(data)
            if success: return pm
            return None

        for i in range(numframes):
            framename = os.path.join(outdir, "frame_%04d.png" % (i,))

            pm = None
            while True:
                pm = tryload(glitch_file(self.inputfilename, self.sliderNumGlitch.value()))
                if pm is None: continue
                else: break

            pm.save(framename, "png")
            QApplication.processEvents()


    def save(self):
        if not hasattr(self, 'inputfilename'):
            QMessageBox.critical(self, "Error", "Glitch an image first!",
                                 QMessageBox.Ok)
            return
        savename, type = QFileDialog.getSaveFileName(self, "Save glitched file", filter="JPEG (*.jpg);;PNG (*.png)")
        if savename:
            if 'JPEG' in type:
                savetype = 'jpg'
            else:
                savetype = 'png'
            print(savename)
            self.glitchmap.save(savename, savetype, 100)

    def numglitch_changed(self, value):
        self.txtGlitch.setText("%d %s" % (value,
                                          'byte' if value == 1 else 'bytes'))

    def file_open_readfile(self, path):
        self.inputfilename = path
        scene = QGraphicsScene()
        pm = None
        try:
            pm = QPixmap()
            pm.load(self.inputfilename)
        except Exception as ex:
            print(ex)
            QMessageBox.critical(self, "Error", "Unable to load image: %s\n%s" % (self.inputfilename,str(ex)),
                                    QMessageBox.Ok)
            return
        scene.addPixmap(pm)
        self.imgInput.setScene(scene)

    def file_open(self):
        print("open!")
        dlg = QFileDialog(self)
        dlg.setFileMode(QFileDialog.ExistingFile)
        dlg.setNameFilters(["Images (*.jpg)"])
        if(dlg.exec()):
            print("ok:", dlg.selectedFiles()[0])
            self.file_open_readfile(dlg.selectedFiles()[0])

    def random_glitch(self):
        if not hasattr(self, 'inputfilename'):
            QMessageBox.critical(self, "Error", "Load an image first!",
                                 QMessageBox.Ok)
            return

        scene = QGraphicsScene()
        bytes = None


        tries = 1
        maxtry = 3

        pm = QPixmap()
        while True:
            bytes = glitch_file(self.inputfilename, self.sliderNumGlitch.value())
            success = pm.loadFromData(bytes)
            if success: break
            else:
                print("Glitch was too strong!")
                print("Trying again %d / %d" % (tries, maxtry))
                tries += 1
                bytes = glitch_file(self.inputfilename, self.sliderNumGlitch.value())
                if tries > maxtry:
                    QMessageBox.critical(self, "Error",
                                         "Glitching was too strong, unable to load image.\nYou can try again or you may need to lower the glitching-slider if this keeps happening.",
                                         QMessageBox.Ok)
                    break


        self.glitchbytes = bytes
        self.glitchmap = pm
        scene.addPixmap(pm)
        self.imgOutput.setScene(scene)



def main():
    app = QApplication(sys.argv)

    from PyQt5.QtCore import QThreadPool

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()