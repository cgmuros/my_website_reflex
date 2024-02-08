python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
API_URL=https://my-website-reflex.vercel.app/ reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -rf frontend.zip
deactivate