::[Bat To Exe Converter]
::
::fBE1pAF6MU+EWHreyHcjLQlHcBeDMH21OpEZ++Pv4Pq7kU4UUewlfc/W37CHI+gWqnDNSaYsxHFTltgDAns=
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAhVQBKNAE+/Fb4I5/jH3OmOp0MHUaIyfYvS2byLYNU61nXlZ50k2GlVlvcPAx9dQgGuehoklWdBuWq5PsSTvUHoSUfp
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdFy5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpSI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFAhVQBKNAE+/Fb4I5/jH3O+Tt11TUfo6GA==
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
@echo on

REM Imposta il percorso della cartella di installazione di Python
set PYTHON_INSTALL_DIR=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310


REM Imposta il percorso della cartella contenente i file whl
set WHL_DIR=Parkinson\code\setup

REM Installa Python
echo Installing Python 3.10.8...
start /wait Parkinson\code\setup\python-3.10.8-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 TargetDir=%PYTHON_INSTALL_DIR%
echo Python installation completed.

echo Installing Visual c++...
Parkinson\code\setup\VC_redist.x64.exe /install /quiet /norestart
echo  Visual c++ installation completed.

echo Upgrading pip...
python.exe -m pip install --upgrade pip
REM Installa i file whl
echo Installing Python packages...
%PYTHON_INSTALL_DIR%\Scripts\pip.exe install -r %WHL_DIR%\requirements.txt

echo Python packages installation completed.
