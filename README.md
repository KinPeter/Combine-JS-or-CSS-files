# Combine JS / CSS  

This tiny Python program is designed to combine or *merge* together several text files into one, kind of *bundle file*. It's especially useful for client side JavaScript (where `import` and `require()` do not work) and for CSS files. Now you can easily write your code into separate files or *modules* and combine them into one final file for production.


### Usage: 

- First, in your main file, create a comment where you list all the relative pathes of the files you want to include in the bundle between `/*@include:` and `@end*/` tags, separated by commas, as in this example:  
    *(Important: please do not use linebreaks or other characters in the listing.)*  
    `/*@include: ./modules/data.js, ./modules/lang.js, ./modules/page.js @end*/`  

- Next, start the program with adding the full path to your main file as a `-f` or `--file` parameter, just as below:     
    `> python combine.py -f "C:\Projects\Work\Your_App\filename.js"`

- The program will create a new file with the name of **"filename.bundle.js"** in the same  directory where the main file is located.

*Please note, unless you modify the code, in the new bundle file the included files will come first (in the order as you listed them in the comment), and the main file will be at the bottom.*