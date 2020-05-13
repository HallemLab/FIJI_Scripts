//User Inputs
call("java.lang.System.gc");
Folderpath="E:/MLC Tracking/20191115"
UID="20191115_SswtiL3-6_po_PO"

// How many frames should be used for background subtraction?
	BackgroundWindowStart="0"
	BackgroundWindowStop="180"

	
// How many images do you want to process? (This should probably match the total number of images in your experiment, but it doesn't have it.)
	NumImages="180" //number of images to import

setOption("BlackBackground", true);

//Program Generated Variables
	avgfile= "AVG_" + UID
	filepath="" + Folderpath + "/" + UID + "/"

// Process Camera Images
call("java.lang.System.gc");
	
		run("Image Sequence...", "open=["+filepath+ "] number="+NumImages+" sort"); //Import Sequences
			call("java.lang.System.gc");
		run("Z Project...", "start="+BackgroundWindowStart+ " stop="+BackgroundWindowStop+" projection=[Average Intensity]"); // Take Average of Image Sequence
			call("java.lang.System.gc");
		imageCalculator("Subtract create stack", UID, avgfile); // Subtract Average from Every Image in Stack
			setBatchMode(true); 
				selectWindow(UID); 
				run("Close");
				selectWindow("AVG_"+UID);
				run("Close"); 
			setBatchMode(false); 
			call("java.lang.System.gc");
		run("Enhance Contrast", "saturated=0.4 process_all"); //Readjust Contrast
			call("java.lang.System.gc");
		run("Save", "save=[" + Folderpath + "/" + UID + "_processed.tif]"); //Save Image
		close();	
	




