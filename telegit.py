import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from github import Github
import datetime

class GitHubMonitorBot:
    def __init__(self, telegram_token, github_token):
        self.updater = Updater(token=telegram_token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.github = Github(github_token)
        
        # Registrar comandos
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('watch', self.watch_repo))
        self.dispatcher.add_handler(CommandHandler('unwatch', self.unwatch_repo))
        self.dispatcher.add_handler(CommandHandler('list', self.list_repos))
        
        # Almacenamiento de suscripciones (en producción usar una base de datos)
        self.subscriptions = {}  # {chat_id: [repo_names]}
        
    def start(self, update, context):
        """Iniciar el bot y mostrar comandos disponibles"""
        welcome_message = """
        ¡Bienvenido al Monitor de GitHub! 🚀
        
        Comandos disponibles:
        /watch username/repo - Seguir un repositorio
        /unwatch username/repo - Dejar de seguir un repositorio
        /list - Ver repositorios seguidos
        """
        update.message.reply_text(welcome_message)
    
    def watch_repo(self, update, context):
        """Agregar un repositorio a la lista de seguimiento"""
        if not context.args:
            update.message.reply_text("❌ Por favor especifica el repositorio (ejemplo: /watch usuario/repo)")
            return
            
        repo_name = context.args[0]
        chat_id = update.effective_chat.id
        
        try:
            # Verificar si el repositorio existe
            repo = self.github.get_repo(repo_name)
            
            if chat_id not in self.subscriptions:
                self.subscriptions[chat_id] = []
            
            if repo_name not in self.subscriptions[chat_id]:
                self.subscriptions[chat_id].append(repo_name)
                update.message.reply_text(f"✅ Ahora siguiendo: {repo_name}")
            else:
                update.message.reply_text("Ya estás siguiendo este repositorio")
                
        except Exception as e:
            update.message.reply_text(f"❌ Error: No se pudo encontrar el repositorio {repo_name}")
    
    def unwatch_repo(self, update, context):
        """Dejar de seguir un repositorio"""
        if not context.args:
            update.message.reply_text("❌ Por favor especifica el repositorio (ejemplo: /unwatch usuario/repo)")
            return
            
        repo_name = context.args[0]
        chat_id = update.effective_chat.id
        
        if chat_id in self.subscriptions and repo_name in self.subscriptions[chat_id]:
            self.subscriptions[chat_id].remove(repo_name)
            update.message.reply_text(f"✅ Ya no sigues: {repo_name}")
        else:
            update.message.reply_text("No estabas siguiendo este repositorio")
    
    def list_repos(self, update, context):
        """Listar repositorios seguidos"""
        chat_id = update.effective_chat.id
        
        if chat_id not in self.subscriptions or not self.subscriptions[chat_id]:
            update.message.reply_text("No estás siguiendo ningún repositorio")
            return
            
        repos = "\n".join([f"• {repo}" for repo in self.subscriptions[chat_id]])
        update.message.reply_text(f"Repositorios seguidos:\n{repos}")
    
    def check_updates(self):
        """Verificar actualizaciones en los repositorios (ejecutar periódicamente)"""
        for chat_id, repos in self.subscriptions.items():
            for repo_name in repos:
                try:
                    repo = self.github.get_repo(repo_name)
                    # Obtener commits recientes
                    recent_commits = repo.get_commits(since=datetime.datetime.now() - datetime.timedelta(hours=1))
                    
                    for commit in recent_commits:
                        message = f"""
                        📢 Nuevo commit en {repo_name}
                        
                        Autor: {commit.author.name if commit.author else 'Desconocido'}
                        Mensaje: {commit.commit.message}
                        URL: {commit.html_url}
                        """
                        self.updater.bot.send_message(chat_id=chat_id, text=message)
                        
                except Exception as e:
                    print(f"Error checking {repo_name}: {str(e)}")
    
    def start_polling(self):
        """Iniciar el bot"""
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    # Configurar tokens desde variables de entorno
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
    
    if not TELEGRAM_TOKEN or not GITHUB_TOKEN:
        print("❌ Por favor configura TELEGRAM_TOKEN y GITHUB_TOKEN en las variables de entorno")
        exit(1)
    
    bot = GitHubMonitorBot(TELEGRAM_TOKEN, GITHUB_TOKEN)
    bot.start_polling()
