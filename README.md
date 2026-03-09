# rag-md-engine

deactivate
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .

which pip
which python

pip install uv
uv init <project-name>
uv venv
uv sync