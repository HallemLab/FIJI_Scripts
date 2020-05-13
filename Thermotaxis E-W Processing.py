import os
from ij import IJ
from ij import WindowManager
from ij.io import DirectoryChooser
from ij.io import FileSaver
from ij.gui import GenericDialog
from ij.plugin import FolderOpener
from ij.plugin import ZProjector
from ij.plugin import ImageCalculator
from os import path

dc = DirectoryChooser("Choose a folder")
folder = dc.getDirectory()

if folder is None:
	print "User canceled the dialog!"
else:
	print "Selected folder:", folder

def getOptions():
	gd = GenericDialog("Options")
	gd.addCheckbox("Process_Right_Camera?", True)
	gd.addCheckbox("Process_Left_Camera?", True)
	gd.addNumericField("CamRScale: ", 214, 0)
	gd.addNumericField("CamLScale: ", 202, 0)
	gd.addNumericField("BackgroundWindowStart: ", 0, 0)
	gd.addNumericField("BackgroundWindowEnd: ", 600, 0)
	gd.addNumericField("GridSize: ", 10000, 0)
	gd.addNumericField("TranslateR: ", 0, 0)
	gd.addNumericField("TranslateL: ", 0, 0)
	gd.showDialog()
	#
	if gd.wasCanceled():
		print "User canceled dialog!"
		return
	# Read out the options
	runCamR = gd.getNextBoolean()
	runCamL = gd.getNextBoolean()
	CamRScale = gd.getNextNumber()
	CamLScale = gd.getNextNumber()
	BackgroundWindowStart = gd.getNextNumber()
	BackgroundWindowEnd = gd.getNextNumber()
	GridSize = gd.getNextNumber()
	TranslateR = gd.getNextNumber()
	TranslateL = gd.getNextNumber()
	return runCamR, runCamL, CamRScale, CamLScale, BackgroundWindowStart, BackgroundWindowEnd, GridSize, TranslateR, TranslateL # a tuple with the parameters

options = getOptions()
if options is not None:
	runCamR, runCamL, CamRScale, CamLScale, BackgroundWindowStart, BackgroundWindowEnd, GridSize, TranslateR, TranslateL = options # unpack each parameter
	print runCamR, runCamL, CamRScale, CamLScale, BackgroundWindowStart, BackgroundWindowEnd, GridSize, TranslateR, TranslateL

if runCamR:
	impR1 = FolderOpener.open(folder,"file=CamR sort")
	UID = impR1.title	
	filepath = folder.strip(UID+'/')

	projectR = ZProjector(impR1)
	projectR.setMethod(ZProjector.AVG_METHOD)
	projectR.setImage(impR1)
	projectR.setStartSlice(int(BackgroundWindowStart))
	projectR.setStopSlice(int(BackgroundWindowEnd))
	projectR.doProjection()
	projectionR = projectR.getProjection()

	impR2 = ImageCalculator().run("Subtract create stack",impR1, projectionR)
	IJ.run(impR2, "Enhance Contrast","saturated=0.4 process_all")
	IJ.run(impR2, "Set Scale...", "distance="+str(CamRScale)+" known=1 unit=cm")
	IJ.run(impR2, "Grid...", "grid=Lines area="+str(GridSize)+" color=Cyan")
	IJ.run(impR2, "Translate...", "x="+str(TranslateR)+" y=0 interpolation=None stack")

	savepath = path.join(folder, UID + "_CR.tif")
	print savepath	
	fs = FileSaver(impR2)
	if fs.saveAsTiffStack(savepath):
		print("Files saved succesfully")
else:
	print "No CamR Images to Open"

if runCamL:
	impL1 = FolderOpener.open(folder,"file=CamL sort")
	UID = impL1.title	
	filepath = folder.strip(UID+'/')

	projectL = ZProjector(impL1)
	projectL.setMethod(ZProjector.AVG_METHOD)
	projectL.setImage(impL1)
	projectL.setStartSlice(int(BackgroundWindowStart))
	projectL.setStopSlice(int(BackgroundWindowEnd))
	projectL.doProjection()
	projectionR = projectL.getProjection()

	impL2 = ImageCalculator().run("Subtract create stack",impL1, projectionR)
	IJ.run(impL2, "Enhance Contrast","saturated=0.4 process_all")
	IJ.run(impL2, "Set Scale...", "distance="+str(CamLScale)+" known=1 unit=cm")
	IJ.run(impL2, "Grid...", "grid=Lines area="+str(GridSize)+" color=Cyan")
	IJ.run(impL2, "Translate...", "x="+str(TranslateL)+" y=0 interpolation=None stack")
	IJ.run(impL2, "Flip Vertically","stack")
	IJ.run(impL2, "Flip Horizontally","stack")

	savepath = path.join(folder, UID + "_CL.tif")
	print savepath	
	fs = FileSaver(impL2)
	if fs.saveAsTiffStack(savepath):
		print("Files saved succesfully")
else:
	print "No CamL Images to Open"
	