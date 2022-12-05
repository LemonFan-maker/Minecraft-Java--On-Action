
c = get_config()

c.NotebookApp.allow_remote_access = True

c.NotebookApp.allow_root = True

c.NotebookApp.open_browser = False

c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$6tJ8XpDYnhd6mTKtdeNO/g$9JunJXYjsKdfP2LKJYX3t7T08WqSg6jygwxeJaBkyOo'

c.NotebookApp.password_required = True

c.NotebookApp.port = 8837

c.NotebookApp.quit_button = True
