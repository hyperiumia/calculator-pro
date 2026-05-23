# Calculator Pro

Calculadora profesional con interfaz grafica moderna, modo cientifico, historial persistente y temas claro/oscuro.

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-31%20passed-brightgreen.svg)](tests/)

---

## Descripcion

**Problema que resuelve:** Las calculadoras del sistema son basicas. Las web te rastrean. Necesitas una herramienta profesional, local y rapida.

**Como lo resuelve:** Interfaz grafica moderna con CustomTkinter, modo cientifico (trigonometria, logaritmos, raices, factoriales), historial de calculos, memoria (M+/M-/MR/MC), temas claro/oscuro, y atajos de teclado.

**Para quien es:** Desarrolladores, estudiantes, ingenieros, y cualquier persona que necesite una calculadora potente sin abrir el navegador.

---

## Modos

### Modo GUI (default)
```bash
python main.py
```

### Modo CLI
```bash
python main.py calc '2+3*4'
python main.py calc 'sqrt(144)'
python main.py calc 'sin(pi/2)'
python main.py calc '(100+50)*0.12'
```

---

## Funcionalidades

### Modo Basico
- Suma, resta, multiplicacion, division
- Parentesis para agrupar
- Porcentaje
- Cambio de signo (+/-)
- Borrar ultimo digito (backspace)

### Modo Cientifico
- Trigonometria: sin, cos, tan, asin, acos, atan
- Logaritmos: log (base 10), ln (natural)
- Potencias: x^2, x^3, x^n, 10^x
- Raiz cuadrada
- Factorial (n!)
- Inverso (1/x)
- Constantes: pi, e
- Referencia al resultado anterior (Ans)

### Memoria
- M+: agregar valor a memoria
- M-: restar valor de memoria
- MR: recuperar valor de memoria
- MC: limpiar memoria

### Interfaz
- Tema claro y oscuro
- Panel de historial (ultimas 8 operaciones)
- Atajos de teclado (numeros, Enter, Escape, Backspace)
- Display adaptativo (ajusta tamano de fuente)

---

## Atajos de Teclado

| Tecla | Accion |
|-------|--------|
| 0-9 | Ingresar numero |
| + - * / | Operaciones |
| . | Decimal |
| ( ) | Parentesis |
| Enter / = | Calcular |
| Backspace | Borrar ultimo |
| Escape | Limpiar todo |
| % | Porcentaje |

---

## Decisiones Tecnicas

| Decision | Alternativas | Eleccion | Razon |
|----------|-------------|----------|-------|
| GUI | Tkinter, CustomTkinter, PyQt | CustomTkinter | Moderno, simple, activo |
| Motor | eval propio, AST, sympy | eval con sandbox | Flexible, soporta funciones |
| CLI | argparse, click | argparse | Modulo estandar |
| Terminal | print, rich | rich | Para modo CLI solo |

Ver `docs/adr/001-gui-choice.md` para analisis detallado.

---

## Estructura del Proyecto

```
calculator-pro/
  main.py            # Punto de entrada
  src/
    engine.py        # Motor de calculo (basic + scientific)
    gui.py           # Interfaz grafica con CustomTkinter
    cli.py           # Modo CLI con Rich
    config.py        # Temas, fuentes, constantes
  tests/
    test_engine.py       # 27 tests del motor
    test_cli_parser.py   # 4 tests del CLI parser
  docs/adr/
    001-gui-choice.md
  README.md
  requirements.txt
  .gitignore
  LICENSE
```

---

## Tests

```bash
pytest tests/ -v
```

---

## Stack

Python 3.12 | CustomTkinter | rich | argparse | pytest

---

## Posibles Mejoras

- Graficador de funciones (matplotlib integrado)
- Conversion de unidades (temperatura, peso, distancia)
- Historial persistente en SQLite
- Modo programador (hex, oct, bin)
- Calculo de expresiones simbolicas (sympy)
- Exportar historial a CSV

---

## Licencia

MIT License

---

## Autor

**Patricio Tirado** - [Hyperium IA](https://www.hyperiumia.com)

[![GitHub](https://img.shields.io/badge/GitHub-hyperiumia-black.svg?style=flat&logo=github)](https://github.com/hyperiumia)
[![Website](https://img.shields.io/badge/Web-hyperiumia.com-FF6B00.svg?style=flat&logo=google-chrome&logoColor=white)](https://www.hyperiumia.com)