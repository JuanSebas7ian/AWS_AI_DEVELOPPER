# Bedrock Agent Action Group - Task Manager

Action group para Amazon Bedrock Agent Builder que permite gestionar tareas.

## Archivos

- `lambda_function.py`: Función Lambda que maneja las operaciones
- `openapi_schema.json`: Esquema OpenAPI que define las funciones
- `deployment.py`: Script para desplegar en AWS

## Funciones Disponibles

### addTask
Añade una nueva tarea con nombre y prioridad.
- **taskName** (requerido): Nombre de la tarea
- **priority** (opcional): Prioridad 1-5 (default: 3)

### getTasks
Obtiene todas las tareas actuales.

### removeTask
Elimina una tarea por ID.
- **taskId** (requerido): ID de la tarea a eliminar

## Configuración

1. Actualizar `deployment.py` con:
   - ARN del rol de Lambda
   - ID del agente de Bedrock

2. Ejecutar despliegue:
```bash
python deployment.py
```

## Uso en Bedrock Agent

El agente podrá usar comandos como:
- "Añade una tarea llamada 'Revisar código' con prioridad 1"
- "Muestra todas mis tareas"
- "Elimina la tarea con ID 123"