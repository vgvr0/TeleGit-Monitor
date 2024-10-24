# 🤖 TeleGit Monitor

Monitorea tus repositorios favoritos de GitHub directamente desde Telegram. Recibe notificaciones instantáneas sobre nuevos commits, mantente al día con los cambios y nunca te pierdas una actualización importante.

![GitHub last commit](https://img.shields.io/github/last-commit/tuusuario/telegit-monitor)
![GitHub issues](https://img.shields.io/github/issues/tuusuario/telegit-monitor)
![GitHub pull requests](https://img.shields.io/github/issues-pr/tuusuario/telegit-monitor)
![License](https://img.shields.io/github/license/tuusuario/telegit-monitor)

## 🚀 Características

- 📱 Integración perfecta con Telegram
- 🔔 Notificaciones en tiempo real de nuevos commits
- 📋 Gestión sencilla de suscripciones a repositorios
- 🔒 Configuración segura mediante variables de entorno
- 🌐 Soporte para múltiples repositorios por usuario

## 📋 Requisitos Previos

- Python 3.8+
- Token de Bot de Telegram
- Token de GitHub
- Las siguientes dependencias:
  ```
  python-telegram-bot
  PyGithub
  python-dotenv
  ```

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/telegit-monitor.git
cd telegit-monitor
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno:
```bash
cp .env.example .env
# Edita .env con tus tokens
```

## 🚀 Uso

1. Inicia el bot:
```bash
python telegit.py
```

2. En Telegram, usa los siguientes comandos:
- `/start` - Inicia el bot y muestra la ayuda
- `/watch usuario/repo` - Sigue un repositorio
- `/unwatch usuario/repo` - Deja de seguir un repositorio
- `/list` - Muestra los repositorios que sigues

## 📝 Ejemplo de Configuración

```env
TELEGRAM_TOKEN=tu_token_de_telegram
GITHUB_TOKEN=tu_token_de_github
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request


## 🌟 Agradecimientos

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [PyGithub](https://github.com/PyGithub/PyGithub)

## 📊 Roadmap

- [ ] Soporte para notificaciones de Issues
- [ ] Filtros por tipo de commit
- [ ] Panel de estadísticas del repositorio
- [ ] Soporte para múltiples idiomas
- [ ] Integración con GitHub Actions

## ⚠️ Notas de Seguridad

- Nunca compartas tus tokens
- Usa variables de entorno para las credenciales
- Revisa periódicamente los permisos de GitHub
