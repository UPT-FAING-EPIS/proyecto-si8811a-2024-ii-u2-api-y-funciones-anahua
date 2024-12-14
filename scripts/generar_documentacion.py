#python -m venv env
#.\env\Scripts\activate
#pip install pdoc
#
#pip install -r ../fast-point-api/requirements.txt
#pip freeze > requirements.txt
#pip install -r requirements.txt
#
#
# python generar_documentacion.py
#
import subprocess
import os

def generar_documentacion():

    docs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generar_documentacion", "docs")
    os.makedirs(docs_dir, exist_ok=True)

    try:
        # HTML
        subprocess.run(
            ["pdoc", "--output-dir", docs_dir, "../fast-point-api/fast_point_api"],
            check=True,
        )
        print(f"Documentación HTML generada en: {docs_dir}")

        # Markdown
        subprocess.run(
            ["pdoc", "--output-dir", docs_dir, "--template", "markdown", "../fast-point-api/fast_point_api"],
            check=True,
        )
        print(f"Documentación Markdown generada en: {docs_dir}")

    except subprocess.CalledProcessError as e:
        print(f"Error al generar la documentación: {e}")

if __name__ == "__main__":
    generar_documentacion()

