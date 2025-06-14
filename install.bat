@echo off
echo Creating virtual environment...
python -m venv qrng-env
echo Activating environment...
call qrng-env\Scripts\activate
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
echo.
echo Setup complete! To start the app, run:
echo.
echo qrng-env\Scripts\activate
echo python app.py
pause