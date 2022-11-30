import typer
import time
from rich.progress import track
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
import git
import os

app = typer.Typer()

@app.command()
def test_connect(name: str):
    print(f"Hello {name}")    


@app.command()
def init_angular():
    typer.echo('    ___                      __              ______                     __      __     ')
    typer.echo('   /   |  ____  ____ ___  __/ /___ ______   /_  __/__  ____ ___  ____  / /___ _/ /____ ')
    typer.echo('  / /| | / __ \/ __ `/ / / / / __ `/ ___/    / / / _ \/ __ `__ \/ __ \/ / __ `/ __/ _ ')
    typer.echo(' / ___ |/ / / / /_/ / /_/ / / /_/ / /       / / /  __/ / / / / / /_/ / / /_/ / /_/  __/')
    typer.echo('/_/  |_/_/ /_/\__, /\__,_/_/\__,_/_/       /_/  \___/_/ /_/ /_/ .___/_/\__,_/\__/\___/ ')

    typer.echo('Initialized Angular template ...')
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing to clone the template script...", total=None)
        time.sleep(5)
        if os.path.isdir('/tmp/angular-socle'):
            typer.echo('\n\nThe folder /tmp/angular-socle already exists\n')
            os.system('rm -rf /tmp/angular-socle\n')
            time.sleep(5)
            typer.echo('\nThe folder /tmp/angular-socle has been deleted\n')

        git.Git("/tmp").clone("git@github.com:Liam-Esteffe/angular-socle.git")
    print("Done!")
    
    system_os = Prompt.ask("Enter your system name", choices=["Windows", "Macos", "Linux"], default="Linux")
    
    if system_os == "Windows":
        typer.echo("\n\nWindows system detected but not supported\n")
    
    elif system_os == "Macos":
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Processing to install Macos depiencies...", total=None)
            time.sleep(5)
            os.system('brew install jq')
    
    else:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Processing to install Linux depiencies...", total=None)
            time.sleep(5)
            os.system('sudo apt-get install jq')    
    
    project_name = Prompt.ask("Enter your project name", default='angular-template')
    
    project_dest = Prompt.ask("Enter your project destination", default='/tmp')
    
    os.system('cp -r /tmp/angular-socle {project_dest}' + project_name)
    
    os.system('cd {project_dest}' + project_name)
    
    os.system('npm install')
    
    server_choice = Prompt.ask("Do you want to start the server ?", choices=["Yes", "No"], default="Yes")
    
    nest_or_django = Prompt.ask("Do you want to use NestJS or Django ?", choices=["NestJS", "Django"], default="NestJS")
    
    if nest_or_django == "NestJS":
        init_nest(project_name, True)


    
@app.command()
def init_nest(project_name: str, options: bool):
    typer.echo(' _   _           _     ___ _____   _____                    _       _       ')
    typer.echo('| \ | |         | |   |_  /  ___| |_   _|                  | |     | |      ')
    typer.echo('|  \| | ___  ___| |_    | \ `--.    | | ___ _ __ ___  _ __ | | __ _| |_ ___ ')
    typer.echo('| |\  |  __/\__ \ |_/\__/ /\__/ /   | |  __/ | | | | | |_) | | (_| | ||  __/')
    typer.echo('\_| \_/\___||___/\__\____/\____/    \_/\___|_| |_| |_| .__/|_|\__,_|\__\___|')
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing to install NestJS depiencies...", total=None)
        time.sleep(5)
        os.system('npm install -g @nestjs/cli')
        os.system('npm install')
        os.system('npm install -g @angular/cli')
        os.system('npm install')
        os.system('npm install --save-dev @angular-devkit/build-angular')
        os.system('npm install --save-dev @angular-devkit/build-ng-packagr')
        os.system('npm install --save-dev @angular-devkit/build-webpack')
        os.system('npm install --save-dev @angular-devkit/core')
        os.system('npm install --save-dev @angular-devkit/schematics')
        os.system('npm install --save-dev @angular/cli')
        os.system('npm install --save-dev @angular/compiler-cli')
        os.system('npm install --save-dev @angular/language-service')
        os.system('npm install --save-dev @ngtools/webpack')
        os.system('npm install --save-dev @schematics/angular')
        os.system('npm install --save-dev @schematics/update')
        os.system('npm install --save-dev @types/jasmine')
        os.system('npm install --save-dev @types/jasminewd2')
        os.system('npm install --save-dev @types/node')
        os.system('npm install --save-dev codelyzer')
        os.system('npm install --save-dev core-js')
        os.system('npm install --save-dev jasmine-core')
        os.system('npm install --save-dev jasmine-spec-reporter')
        os.system('npm install --save-dev karma')
        os.system('npm install --save-dev karma-chrome-launcher')
        os.system('npm install --save-dev karma-coverage-istanbul-reporter')
        os.system('npm install --save-dev karma-jasmine')
        os.system('npm install --save-dev karma-jasmine-html-reporter')
        os.system('npm install --save-dev ng-packagr')
        os.system('npm install --save-dev protractor')
        
        
        os.system('ng add @nestjs/schematics')

        os.system('nest g module user')
        os.system('nest g service user')
        os.system('nest g controller user')

        os.system('nest g module auth')
        os.system('nest g service auth')
        os.system('nest g controller auth')

        os.system('nest g module admin')
        os.system('nest g service admin')
        os.system('nest g controller admin')

        os.system('nest g module database')


@app.command()
def init_django(project_name: str, options: bool):
    print(f"Creating django project {project_name}")
    print(f"Options: {options}")


@app.command()
def firebase_deploy(project_name: str, options):
    typer.echo(' _____ _  ____  _____ ____  ____  ____  _____   ____  _____ ____  _     ____ ___  _')
    typer.echo('/    // \/  __\/  __//  _ \/  _ \/ ___\/  __/  /  _ \/  __//  __\/ \   /  _ \\  \//')
    typer.echo('|  __\| ||  \/||  \  | | //| / \||    \|  \    | | \||  \  |  \/|| |   | / \| \  / ')
    typer.echo('| |   | ||    /|  /_ | |_\\| |-||\___ ||  /_   | |_/||  /_ |  __/| |_/\| \_/| / /  ')
    typer.echo('\_/   \_/\_/\_\\____\\____/\_/ \|\____/\____\  \____/\____\\_/   \____/\____//_/   ')

    os.system('npm install -g firebase-tools')
    os.system('firebase login')
    os.system('firebase init')
    os.system('npm install')
    os.system('ng build --prod')
    os.system('firebase deploy')

@app.command()
def init_mysqldb(sql_user: str, sql_password: str, sql_host: str, sql_port: str, sql_db: str, sql_file=None):
    typer.echo(' _____ ____  ____  ____  _____  _____  ____  ____ ')
    typer.echo('/  __//  _ \/  _ \/  _ \/  __/ /__ __\/  _ \/  _ \\')
    typer.echo('| |  _| / \|| / \|| / \||  \     / \  | / \|| / \||')
    typer.echo('| |_//| \_/|| \_/|| |-|||  /_    | |  | |-||| \_/||')
    typer.echo('\____\\____/\____/\_/ \|\____\   \_/  \_/ \|\____/')

    if sql_file == None:
        sql_file = open('sql.sql', 'w')
        sql_file.write("CREATE DATABASE IF NOT EXISTS " + sql_db + ";\n")
        ## create base tables
        sql_file.write("USE " + sql_db + ";\n")
        sql_file.write("CREATE TABLE IF NOT EXISTS users (\n")
        sql_file.write("id INT NOT NULL AUTO_INCREMENT,\n")
        sql_file.write("username VARCHAR(255) NOT NULL,\n")
        sql_file.write("password VARCHAR(255) NOT NULL,\n")
        sql_file.write("email VARCHAR(255) NOT NULL,\n")
        sql_file.write("PRIMARY KEY (id)\n")
        sql_file.write(");\n")
        sql_file.write("CREATE TABLE IF NOT EXISTS user_profile (\n")
        sql_file.write("id INT NOT NULL AUTO_INCREMENT,\n")
        sql_file.write("user_id INT NOT NULL,\n")
        sql_file.write("firstname VARCHAR(255) NOT NULL,\n")
        sql_file.write("lastname VARCHAR(255) NOT NULL,\n")
        sql_file.write("PRIMARY KEY (id),\n")
        sql_file.write("FOREIGN KEY (user_id) REFERENCES users(id)\n")
        sql_file.write(");\n")
        sql_file.write("CREATE TABLE IF NOT EXISTS user_settings (\n")
        sql_file.write("id INT NOT NULL AUTO_INCREMENT,\n")
        sql_file.write("user_id INT NOT NULL,\n")
        sql_file.write("setting_key VARCHAR(255) NOT NULL,\n")
        sql_file.write("setting_value VARCHAR(255) NOT NULL,\n")
        sql_file.write("PRIMARY KEY (id),\n")
        sql_file.write("FOREIGN KEY (user_id) REFERENCES users(id)\n")
        sql_file.write(");\n")
        sql_file.write("CREATE TABLE IF NOT EXISTS user_groups (\n")
        sql_file.write("id INT NOT NULL AUTO_INCREMENT,\n")
        sql_file.write("user_id INT NOT NULL,\n")
        sql_file.write("group_id INT NOT NULL,\n")
        sql_file.write("PRIMARY KEY (id),\n")
        sql_file.write("FOREIGN KEY (user_id) REFERENCES users(id),\n")
        sql_file.write("FOREIGN KEY (group_id) REFERENCES groups(id)\n")
        sql_file.write(");\n")
        sql_file.write("CREATE TABLE IF NOT EXISTS groups (\n")
        sql_file.write("id INT NOT NULL AUTO_INCREMENT,\n")
        sql_file.write("name VARCHAR(255) NOT NULL,\n")
        sql_file.write("PRIMARY KEY (id)\n")
        sql_file.write("USE " + sql_db + ";\n")
        sql_file.close()

    os.system('mysql -u {sql_user} -p{sql_password} -h {sql_host} -P {sql_port} -e "create database {sql_db}"')
    os.system('mysql -u {sql_user} -p{sql_password} -h {sql_host} -P {sql_port} {sql_db} < {sql_file}')



@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()