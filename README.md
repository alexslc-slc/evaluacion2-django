# Registro de Empleados

Aplicación CRUD desarrollada con Django y MySQL para la gestión de empleados y departamentos.

## Características

- **Modelo Relacional**: Dos tablas relacionadas mediante clave foránea (Empleados → Departamentos)
- **CRUD Completo**: Crear, Leer, Actualizar y Eliminar para ambas tablas
- **Manejo de Imágenes**: Subida y visualización de fotos para empleados y departamentos
- **Interfaz Simple**: Templates con diseño limpio y navegación intuitiva

## Modelos

### Departamento
| Campo | Tipo |
|-------|------|
| id | BigAutoField (PK) |
| nombre | CharField(100) |
| ubicacion | CharField(200) |
| descripcion | TextField |
| foto | ImageField |

### Empleado
| Campo | Tipo |
|-------|------|
| id | BigAutoField (PK) |
| nombres | CharField(100) |
| apellidos | CharField(100) |
| cargo | CharField(100) |
| foto | ImageField |
| departamento | ForeignKey → Departamento |

## Requisitos

- Python 3.12+
- MySQL 8.0+
- Pillow (para manejo de imágenes)

## Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/alexslc-slc/registro_empleados.git
cd registro_empleados

# Instalar dependencias
pip install -r requirements.txt

# Crear base de datos MySQL
mysql -u root -e "CREATE DATABASE registro_empleados CHARACTER SET utf8mb4;"

# Configurar variables de entorno (opcional)
export DATABASE_URL=mysql://usuario:password@localhost:3306/registro_empleados

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

## Despliegue

La aplicación está preparada para desplegarse en Railway, Render u otras plataformas:

- `Procfile` incluido para Heroku/Railway
- `whitenoise` configurado para archivos estáticos
- `dj-database-url` para configuración de BD mediante variable de entorno
- Variable `DATABASE_URL` para conexión a la base de datos

## Tecnologías

- Django 6.0
- MySQL 8.0
- Pillow
- Gunicorn
- WhiteNoise
