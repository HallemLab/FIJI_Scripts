//User Inputs
call("java.lang.System.gc");
Folderpath="C:/Users/hallemlab/Documents/Astra"
UID="200121_06"

// How many frames should be used for background subtraction?
	BackgroundWindowStart="0"
	BackgroundWindowStop="180"

	
// How many images do you want to process? (This should probably match the total number of images in your experiment, but it doesn't have it.)
	NumImages="180" //number of images to import


setOption("BlackBackground", true);

//Program Generated Variables
	filepath="" + Folderpath + "/" + UID 
	avgfile= "AVG_" + filepath

// Process Camera Images
call("java.lang.System.gc");
	
		run("Image Sequence...", "open=["+filepath+ "] number="+NumImages+" sort"); //Import Sequences
			call("java.lang.System.gc");
		run("Invert","stack");
			call("java.lang.System.gc");
		run("Z Project...", "start="+BackgroundWindowStart+ " stop="+BackgroundWindowStop+" projection=[Average Intensity]"); // Take Average of Image Sequence
			call("java.lang.System.gc");
		imageCalculator("Subtract create stack", filepath, avgfile); // Subtract Average from Every Image in Stack
			setBatchMode(true); 
				selectWindow(filepath); 
				run("Close");
				selectWindow("AVG_"+filepath);
				run("Close"); 
			setBatchMode(false); 
			call("java.lang.System.gc");
		run("Enhance Contrast", "saturated=0.4 process_all"); //Readjust Contrast
			call("java.lang.System.gc");
		run("Save", "save=[" + Folderpath + "/" + UID + "_processed.tif]"); //Save Image
		close();	
	




