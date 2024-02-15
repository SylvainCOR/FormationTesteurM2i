@echo off
SETLOCAL enabledelayedexpansion

IF NOT EXIST "Phone" mkdir "Phone">NUL

FOR /F "tokens=1,2* delims=, " %%i in ('type android.csv') do (
	set android=%%i
	
	echo !android!,%%j >> Phone/adbDevices.txt
	
	IF NOT EXIST "Phone/!android!" mkdir "Phone/!android!">NUL
	
	FOR /L %%x in (1, 1, 2) do (
		echo Running test_auto number %%x on !android!
		py C:\Users\Administrateur\Desktop\appium_scripts_python\cherche_ville_lettre_par_lettre_OK.py
	) 



DEL Phone\adbDevices.txt


)
