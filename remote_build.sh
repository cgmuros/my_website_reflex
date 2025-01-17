python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
# API_URL=https://mywebsitereflex-production.up.railway.app 
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -rf frontend.zip
deactivate