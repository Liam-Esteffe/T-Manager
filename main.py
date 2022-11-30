import typer
import time
from rich.progress import track
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
import git
import os

app = typer.Typer()

# Angular init command controller
# --------------------------------*
# Init angular base auth app client

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
        try:
            if os.path.isdir('/tmp/angular-socle'):
                typer.echo('\n\nThe folder /tmp/angular-socle already exists\n')
                os.system('rm -rf /tmp/angular-socle\n')
                time.sleep(5)
                typer.echo('\nThe folder /tmp/angular-socle has been deleted\n')
        except:
            print('Error while deleting the folder /tmp/angular-socle')
            typer.Typer(pretty_exceptions_short=False)
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
            try:
                progress.add_task(description="Processing to install Macos depiencies...", total=None)
                time.sleep(5)
                os.system('brew install jq')
            except:
                print('Error while installing jq')
                typer.Typer(pretty_exceptions_short=False)
    else:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            try:
                progress.add_task(description="Processing to install Linux depiencies...", total=None)
                time.sleep(5)
                os.system('sudo apt-get install jq')    
            except:
                print('Error while installing jq')
                typer.Typer(pretty_exceptions_short=False)
   
    project_name = Prompt.ask("Enter your project name", default='angular-template')
    
    project_dest = Prompt.ask("Enter your project destination", default='/tmp')
    
    try:
        os.system('cp -r /tmp/angular-socle {project_dest}' + project_name)
        
        os.system('cd {project_dest}' + project_name)
        
        os.system('npm install')
    except:
        print('Error while installing the angular template')
        typer.Typer(pretty_exceptions_short=False)
    
    server_choice = Prompt.ask("Do you want to start the server ?", choices=["Yes", "No"], default="Yes")
    
    nest_or_django = Prompt.ask("Do you want to use NestJS or Django ?", choices=["NestJS", "Django"], default="NestJS")
    
    if nest_or_django == "NestJS":
        init_nest(project_name, True)
    elif nest_or_django == "Django":
        init_django(project_name, True)


# NestJS init command controller
# --------------------------------*
# Init NestJS base auth app server

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
        try:
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
        
        except:
            print('Error while installing NestJS')
            typer.Typer(pretty_exceptions_short=False)
            
        ## add mysl connection in app.module.ts
        


# Django init command controller
# --------------------------------*
# Init Django base auth app server
@app.command()
def init_django(project_name: str, options: bool):
    typer.echo('  _____  _                         ')
    typer.echo(' |  __ \(_)                        ')
    typer.echo(' | |  | |_  __ _ _ __   __ _  ___  ')
    typer.echo(' | |  | | |/ _` |  _ \ / _ |/  _ \ ')
    typer.echo(' | |__| | | (_| | | | | (_| | (_) |')
    typer.echo(' |_____/| |\__,_|_| |_|\__, |\___/ ')
    typer.echo('       _/ |             __/ |      ')
    typer.echo('      |__/             |___/       ')
                                         
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing to install Django depiencies...", total=None)
        time.sleep(5)
        os.system('pip3 install django')
        os.system('pip3 install djangorestframework')
        os.system('pip3 install django-cors-headers')
        os.system('pip3 install django-extensions')
        os.system('pip3 install django-rest-auth')
        os.system('pip3 install django-allauth')
        os.system('pip3 install django-rest-auth[with_social]')
        os.system('pip3 install django-rest-auth[with_social]')

        os.system('django-admin startproject {project_name}')
        os.system('cd {project_name}')
        os.system('python3 manage.py startapp user')
        os.system('python3 manage.py startapp auth')
        os.system('python3 manage.py startapp admin')
        os.system('python3 manage.py startapp database')
        os.system('python3 manage.py startapp social')
        
        ## add mysl connection in app.module.ts


# Firebase deployer
# --------------------------------*
# Deploy firebase app

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


# MYSQL init command controller
# --------------------------------*
# Init MYSQL base auth app database

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

# Dockerfile builders
# --------------------------------*
# Build dockerfile for base auth app

@app.command()
def dockerfile():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing to writing Dockerfile and nginx configuration...", total=None)
        time.sleep(5)
        try:
            dockerfile = open('Dockerfile', 'w')
            dockerfile.write("FROM node:10.16.0-alpine as build\n")
            dockerfile.write("WORKDIR /app\n")
            dockerfile.write("COPY package.json package-lock.json .\n")
            dockerfile.write("RUN npm install\n")
            dockerfile.write("COPY . .\n")
            dockerfile.write("RUN npm run build --prod\n")
            dockerfile.write("FROM nginx:1.16.0-alpine\n")
            dockerfile.write("COPY --from=build /app/dist/authapp /usr/share/nginx/html\n")
            dockerfile.write("COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf\n")
            dockerfile.write("EXPOSE 80\n")
            dockerfile.write("CMD [\"nginx\", \"-g\", \"daemon off;\"]\n")
            dockerfile.close()

            nginxfile = open('nginx-custom.conf', 'w')
            nginxfile.write("server {\n")
            nginxfile.write("listen 80;\n")
            nginxfile.write("server_name  localhost;\n")
            nginxfile.write("root /usr/share/nginx/html;\n")
            nginxfile.write("index index.html index.htm;\n")
            nginxfile.write("location / {\n")
            nginxfile.write("try_files $uri $uri/ /index.html;\n")
            nginxfile.write("}\n")
            nginxfile.write("location /api {\n")
            nginxfile.write("proxy_pass http://localhost:8080/api;\n")
            nginxfile.write("proxy_set_header Host $host;\n")
            nginxfile.write("proxy_set_header X-Real-IP $remote_addr;\n")
        except:
            typer.echo("Error creating Dockerfile")
            typer.Typer.exit()
    print('-----------Dockerfile---------------\n\n')
    print(dockerfile)
    print('-----------Nginxfile---------------\n\n')
    print(nginxfile)
    print('--------------------------')

if __name__ == "__main__":
    app()