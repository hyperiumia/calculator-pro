# ADR-001: CustomTkinter sobre Tkinter y PyQt

**Estado:** Aceptada
**Fecha:** 2026-05-24
**Proyecto:** calculator-pro

## Contexto

La calculadora necesita una interfaz grafica moderna. Python ofrece varias opciones de GUI.

## Opciones Consideradas

### Opcion A: Tkinter (modulo estandar)
- **Pros:** Sin dependencias, integrado en Python
- **Contras:** Aspecto visual de los 90, widgets basicos, dificil de estilizar

### Opcion B: CustomTkinter
- **Pros:** Aspecto moderno (rounded corners, dark mode nativo), API similar a Tkinter, activamente mantenido, temas integrados
- **Contras:** Dependencia externa (~2MB)

### Opcion C: PyQt6 / PySide6
- **Pros:** Muy profesional, widgets avanzados, documentacion extensa
- **Contras:** Pesado (~50MB), licencia GPL o comercial, complejo para una calculadora

## Decision

Se eligio CustomTkinter porque ofrece el mejor balance entre aspecto moderno y simplicidad. La API es casi identica a Tkinter pero con widgets visualmente atractivos.

## Consecuencias

**Positivas:**
- UI moderna sin complejidad de Qt
- Dark/light mode nativo
- Comunidad activa y creciente

**Negativas:**
- Dependencia externa (customtkinter)
- Menos maduro que PyQt
