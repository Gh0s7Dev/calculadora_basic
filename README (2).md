# Calculadora Básica en Python

Programa de consola muy simple que realiza las cuatro operaciones
aritméticas básicas: suma, resta, multiplicación y división.

## Cómo ejecutarlo

```bash
python3 calculadora.py
```

## Cómo ejecutar las pruebas y el linter

```bash
pip install -r requirements-dev.txt
black --check calculadora.py test_calculadora.py   # formateador
flake8 calculadora.py test_calculadora.py           # linter
pytest -v                                           # pruebas unitarias
```

---

## Prácticas de calidad integradas

### 1. Coding Standards (linter y formateador)

Se configuró **flake8** (linter) y **black** (formateador automático) para
el proyecto:

- `black` reescribe automáticamente el código para que siga un formato
  consistente (indentación, comillas, longitud de línea, etc.), sin
  necesidad de discutirlo manualmente.
- `flake8` revisa el código en busca de errores de estilo, variables no
  usadas, líneas demasiado largas y otras malas prácticas, usando la
  configuración definida en el archivo `.flake8`.

**Problema que evita:** evita los errores de estilo y la inconsistencia
en el código cuando varias personas trabajan en el mismo proyecto. Sin un
estándar, cada quien escribe con su propio criterio y el código se vuelve
difícil de leer y mantener. Automatizar esta revisión también evita que
el equipo pierda tiempo discutiendo estilo en cada revisión manual.

### 2. Pull Request y Code Review

Se simuló el flujo de trabajo típico de un equipo de desarrollo:

1. Se creó la rama `feature/pruebas-unitarias` a partir de `master`.
2. En esa rama se agregaron las pruebas unitarias (`test_calculadora.py`).
3. Se documentó el cambio en `PR_DESCRIPTION.md`, como se haría en un
   Pull Request real (por ejemplo, en GitHub).
4. Se realizó una **auto-revisión de código** documentada en
   `REVIEW.md`, revisando cobertura de pruebas, manejo de errores,
   nombres de funciones y estilo, antes de aprobar el cambio.
5. Una vez aprobado, la rama se fusionó (merge) a `master`.

> Nota: este flujo se hizo con git local para fines de la práctica. En un
> proyecto real, estos mismos pasos se harían subiendo la rama a un
> repositorio remoto (por ejemplo, GitHub) y abriendo el Pull Request
> desde ahí, donde un compañero de equipo dejaría los comentarios de
> revisión antes de aprobar el merge.

**Problema que evita:** evita que código sin revisar ni probar llegue
directamente a la rama principal. El Code Review permite detectar errores,
malas prácticas o casos no contemplados (como la división entre cero)
antes de integrarlos, en lugar de descubrirlos después en producción.

---

## Relación con lo discutido en clase

Ambas prácticas están relacionadas con la idea de **integración
continua** y evitar el llamado **"Big Bang"** de integración, donde todo
el código se junta de golpe al final del proyecto:

- Usar un **linter/formateador** desde el inicio evita que se acumulen
  pequeños errores de estilo que después son costosos de corregir en
  bloque, y hace que el código de distintas personas sea consistente
  cuando se integra.
- Hacer **Pull Requests pequeños con Code Review** permite integrar
  cambios de forma frecuente e incremental, en vez de acumular grandes
  cantidades de código sin revisar. Esto reduce el retrabajo, porque los
  errores se detectan cuando el cambio es pequeño y fácil de corregir,
  en lugar de cuando ya está mezclado con el resto del sistema.

En conjunto, estas prácticas ayudan a que el software se mantenga con
buena calidad de forma constante, en lugar de intentar "arreglarlo todo"
justo antes de una entrega.
