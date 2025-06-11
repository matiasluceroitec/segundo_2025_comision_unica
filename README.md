# segundo_2025_comision_unica

## Clonar el repositorio

```bash
git clone https://github.com/tecnologo/segundo_2025_comision_unica.git
```

## Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Iniciar la base de datos

```bash
flask db init
flask db migrate
flask db upgrade
```

## Iniciar el servidor

```bash
flask run
```

## Acceder a la aplicacion

Abrir el navegador y acceder a `http://localhost:5000`

## A tener en cuenta
### Es necesario activar XAMPP previo a iniciar el servidor
```bash
sudo /opt/lampp/lampp start
```
