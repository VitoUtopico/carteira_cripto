from carteira_cripto.ext.commands.commands import createdb,\
                                                  dropdb,\
                                                  populatedb
                                                

def init_app(app):
    commands = [
        createdb,
        dropdb,
        populatedb
    ]

    for command in commands:
        app.cli.command()(command)
        
    