README - Calculadora Básica

Programa de consola que hace las cuatro operaciones básicas: suma, resta, multiplicación y división.

Cómo ejecutarlo
bash
python3 calculadora.py

Cómo correr las pruebas y el linter
bash
pip install -r requirements-dev.txt
black --check calculadora.py test_calculadora.py
flake8 calculadora.py test_calculadora.py
pytest -v

Prácticas de calidad aplicadas

1. Linter y formateador (black + flake8)
Se usan para mantener el código ordenado y con un estilo consistente. Esto evita errores de formato y hace que el código sea más fácil de leer entre varias personas.

2. Pull Request y Code Review
Se creó una rama con las pruebas nuevas, se documentó el cambio y se hizo una revisión antes de fusionarlo a la rama principal. Esto evita que se integre código sin revisar y ayuda a detectar errores a tiempo.

Relación con lo visto en clase

Estas prácticas ayudan a evitar el "Big Bang" de integración, donde todo el código se junta de golpe al final. Al usar linter y hacer revisiones frecuentes, los errores se detectan pronto y se reduce el retrabajo.
