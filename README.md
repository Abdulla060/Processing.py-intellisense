## What is it?

This is a way of using Python mode for Processing3 with any Python IDE including PyCharm, VS Code, SublimeText...etc.
With full (almost) intellisense/auto-complete for Processing functions. If you are looking for a way to use Processing 
without their IDE then this is for you.

## About this guide
I will try to write this guide with the most amount of detail so that anyone could follow. Unfortunately, Python mode for 
Processing does not use the standard Python interpreter. instead, it relies on the Java implementation of Python named "Jython".
 That is why IDEs like PyCharm need some extra steps to make everything work nicely. this repository includes a version of 
 the command-line version of Processing.py made by [Jonathan Feinberg](https://github.com/jdf/processing.py).

## Prerequisites
1. you need to have java installed preferably version 1.8.202 which can be downloaded from this 
[link](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)

2. Python 3.x im using 3.6 but any version should work just fine. [link](https://www.python.org/downloads/) 

3. your IDE of choice for this guide I will be using PyCharm. But any IDE will work you just need to configure it accordingly.

4. a copy of this repository which you can get by clicking "clone & download" then "Download zip". after you have 
downloaded this zip file you can extract it anywhere you like.

5. you DO NOT need a copy of Processing. This repository comes with the version that you need.

## Setup
The zip file you have extracted contained a folder called "Processing.py-intellisense" this folder will serve as the root for you 
project and all your sketches have to be placed inside of it otherwise stuff won't work as it should.

### Pycharm Setup
this part will guide you through PyCharm setup and how to make the builtin run button work. if you don't want this and only 
here for the intellisense part and don't mind using the command-line to run your sketches then only follow steps 1 and 2 and skip to the command-line section bellow. 

1. Open "Processing.py-intellisense" folder in PyCharm.

2. once you are there you need to create a new virtual environment by clicking `File > Settings > Project: Processing.py-intellisense > Project Interpreter` 
then click on the cogwheel to add a new virtual environment. Make sure that the "Base Interpreter" option is set to python 3.x (your version of Python) then simply click ok.

3. now we need to set up an "external tool" to run our sketches in PyCharm. to do this go to `File > Settings > Tools > External tools` 
and click on the add (+) button. and fill in the fields as follows:

    Name: `Processing-tool`
    
    Program: `$PyInterpreterDirectory$\python.exe`
    
    Arguments: `-c "import os;os.system('java -jar lib\processing-py.jar $FileName$')"`
    
    Working Directory: `$FileDir$`
    
    I suggest you copy and paste everything.

4. go to `Run > Edit Configuration` and click the (+) sign then chose Python to add a new config. and fill the fields as follows:
    
    Name: `Processing.py`
    
    Parameters: `-c ""`
    
    scroll down and in the "Before launch: External tool" section click on the (+) sign to add a new tool > "Run External 
    Tool" a new pop up will appear chose "Processing-tool" Note: you need to highlight the tool not just put the tick in front 
    of it. click ok on everything and now you are almost ready to run your first sketch :D.
    
### command-line
if you don't mind using the terminal to run your sketches and don't want to bother with the setup. you can run your sketch 
using PyCharm builtin terminal using this command: `java -jar lib/processing-py.jar NAME_OF_YOUR_SKETCH.py`

###Creating your fist sketch and enabling intellisense

in order to get intellisense to work, at the beginning of your sketch you need to import the definitions for Processing functions that i have created using these lines of code:
```
if False:
    from lib.Processing3 import *
```
and before anyone asks Yes the `if False` HAS to be there because you can't actually import definition files into normal python files. this is a hack to get the IDE to load the definitions of from a file.
after these two line, you are free to write Processing code as usual. see Example.py.

    
    
    
    


 