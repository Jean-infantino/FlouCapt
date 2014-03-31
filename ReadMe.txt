Utilization guide : 

1) Launch a terminal and take position in the application directory.
2) You may have to change the adress of the IP camera in order to use yours. It is possible by editing the file "Camera_adress" at the application root.
3) In the terminal, launch the following command : 'python FlouCapt.py'.
4) Then, open FlouCapt.html which is located in the 'web' folder.
5) You can now observe the running application.


Setup and upkeep guide :

1) Download the archive of the FlouCapt application on GitHub (Jean Infantino/FlouCapt)
2) Decompress it to the place of your choice

Additionnal configuration :
To change the time between two captures by the camera, change in the FlouCapt.py file the parameter of the sleep function (in second) and in the index.js file the FadingBtxTwoImg constant.
To change the image transition time on the website, modify in the index.js file the FadingTimeImages constant.
In order to change the duration of the advertisement (presence, absence), modify the constant TimeWithAd and TimeWithoutAd.
You can change the advertisement by putting an image in 'img/ads/' and renaming it 'ad1.png'.