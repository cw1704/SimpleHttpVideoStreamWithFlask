# SimpleHttpVideoStreamWithFlask
It is a simple http service made with flask, to create a http video stream from the device camera.

# Get started
## Environment
For Window:
1. Create a virtual environment
    - `python3 -m venv .venv`
1. Activate the environment 
    - `.venv\Scripts\activate` (use standard terminal instead of powershell)
For Linux:
1. Create virtual environment
    - `python -m venv your-enc-name`
1. Activate the environment
    - `source your-env-name/bin/activate`

## API
### Flask
Reference: https://flask.palletsprojects.com/en/2.3.x/quickstart/
1.  Install Flask
    - `pip install Flask`
1. Test it
    - run `flask --app hello run`
    - open the `localhost:5000` at browser

## Camera reading
Reference: https://pypi.org/project/opencv-python/
### OpenCV
1. Install OpenCV
    - `pip install opencv-python`
2. Test it 
    - `flask --app cv run`

## HTTP streaming 
2. Test it 
    - `flask --app stream run`



