#even though we don't have any templates, let's compile anyway.
python code/web/template.py --compile ./code/templates

gcloud config set project  [YOUR_PROJECT_ID]
gcloud app deploy ./code
