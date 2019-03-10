# Medicine-Select-System
A simple but useful tool with a GUI for selecting medicines or other goods<br><br>

## Notice
1. This program is written for my girlfriend who was a medicine management in a clinic last year. She can't find the medicine quickly when the nurses carry the drug lists getting into the pharmacy. So I spent half-hour writting the program for her. <br><br>
2. To be honest, this program is so simple and it even can't be called as a "system". But this program helps her a lot and makes her find the medicine quickly. After using it a month, she had remembered all the medicines' location so this program never be used later.(HaHa). Now she change her job and ask me the program again so I upload it to github and hope it can help others. **In addition, just for a commemoration.** <br><br>
3. This program with a simple GUI is easy to use. You'd better make the pictures in their initial position for beautiful appearance unless you want to change it.<br><br>
4. I provide the exe as a sample. In the file "place", each file means a cabinet. In the cabinet file, each txt file means a floor of the cabinet. Input the medicines' or other goods' names in it, and you can use the exe to find the location. You needn't input the location of medicines clearly. You only need to put them in suitable place, and use blank space to separate. In "place" I used some computer courses' names instead because I don't know many medicines' name when I was coding. Remember to change them.<br><br>
5. Maybe you need download pyinstaller to make the program be a exe file.Download the pyinstaller first.<br>
```
conda install pyinstaller
```
For example, pyinstaller is in F:\anaconda\Scripts\. and the code is in C:\Users\Administrator\Desktop\medicine_select\select_hospital.py, then you need to put the icon(myico.ico) in C:\Users\Administrator\, input the command in cmd:<br>
```
F:\anaconda\Scripts\pyinstaller.exe -F -w -i myico.ico C:\Users\Administrator\Desktop\medicine_select\select_hospital.py
```
After that you can find the select_hospital.exe in the C:\Users\Administrator\dist.<br><br> 
6. Of course you can improve the program and make it better, for example user can input the medicine's location or delete it in  exe file rather than in txt file. I don't have power to do it because it isn't my research direction.<br><br>

## License
All is allowable.
