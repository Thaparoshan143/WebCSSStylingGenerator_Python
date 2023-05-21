<h2>CSS Styling Generator</h2>

This is designed to work with CSS, where some of the boiler plate for CSS are automatically generated for user as per the given information including:
    <li>CSS File Name</li>
    <li>CSS File Containing Directory</li>

<h3>How this works: </h3>
    <li>The file name UserSelection.txt contains the information of the file name selected for styling along with directory name in bottom</li>
    <li>If UserSelection.txt doesn't exist it creates one inside CSS_Styling_Generator folder with default file name of uni.css and default path from os.getcwd() (i.e directory at which script runs)</li>
    <li>It gives you with the Menu Option to start generating styling, change file name, change dir path</li>
        #Note: file name and dir path can be changed from file itself if not wanted from program.
    <li>File Name selected will be opened on append mode so, every styling generated from here will be appended in bottom</li>

<h3>Features Available till now/working with: </h3>
    <li>
        Pseudo Class Generator
            <li>Takes the class name from user in format (given below)</li>
            <li>pseudo -className-, where - in front and back means generate both before and after pseduo for given class</li>
            <li>pseudo -className, generates only before and pseudo className-, generates only after ... </li>
            <li>Generates the default class styling along with pseudo styling</li>
    </li>

<h3>Other features will be added soon</h3>