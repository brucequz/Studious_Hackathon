# Python Project Template

This is a python project template using fastAPI and jinja2 - so it's more or less a backend application that can also serve rendered html

The project uses a python virtual environment to create a consistent dev environment

## Getting Started

1. [Install](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) python3 (I use python 3.8.5), pip, and virtualenv.
2. Create a new python environment

```bash
python3 -m venv env
source env/bin/activate
```

3. Install the dependencies in `requirements.txt`

```bash
pip install -r requirements.txt
```

4. Run the server using: `uvicorn main:app --reload`

5. Navigate to [localhost:8000](localhost:8000) in your browser!

6. For more, look at the documentation for [fastAPI](https://fastapi.tiangolo.com/) and [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/).
