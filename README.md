# Combine JS / CSS  

This tiny Python program is designed to combine or *merge* together several text files into one, kind of *bundle file*. It's especially useful for client side JavaScript (where `import` and `require()` do not work) and for CSS files. Now you can easily write your code into separate files or *modules* and combine them into one final file for production.

### Modes: 
There are two modes to chose from: **Single** mode and **Watch** mode.
- **Single mode** simply loads and combines your files once then exits the program. To combine again, you have to start it again.
- **Watch mode** will keep on running and waiting for any file changes. Once you edit and save any of the listed files, the program detects it and automatically creates the new bundle for you. *(To use watch mode, you have to add the `-w` or `--watch` parameter when you start the program.)*


### Usage: 

- First, in your main file, create a comment where you list all the relative pathes of the files you want to include in the bundle between `/*@include:` and `@end*/` tags, separated by commas, as in this example:  
    *(Important: please do not use linebreaks or other characters in the listing.)*  
    `/*@include: ./modules/data.js, ./modules/lang.js, ./modules/page.js @end*/`  

- Next, start the program with adding the full path to your main file as a `-f` or `--file` parameter, just as below:     
    `> python combine.py -f "C:\Projects\Work\Your_App\filename.js"`

- Without the Watch mode turned on, the program will create a new file with the name of **"filename.bundle.js"** in the same  directory where the main file is located.

- For **Watch mode** use the `-w` or `--watch` parameter, so the program will keep running and recreates the bundle file whenever you make any changes to any listed file. Example:  
    `> python combine.py -w -f "C:\Projects\Work\Your_App\filename.js"`

*Please note:*
- *Unless you modify the code, in the new bundle file the included files will come first (in the order as you listed them in the comment), and the main file will be at the bottom.*
- *In watch mode the program checks for changes every 2 seconds, thus please avoid saving different files more often than that, otherwise you risk the program missing one of the changes.*