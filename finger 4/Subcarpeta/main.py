# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:02:18 2019

@author: Usuario
"""
import subprocess
import pathlib
from git import Git
import os
a=pathlib.Path(r"/mnt/c/users/usuario/desktop/fiuba/Organizacion de datos/La otra/finger 4/Subcarpeta")


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.environ['GIT_ASKPASS'] = os.path.join(project_dir, 'askpass.py')
    os.environ['GIT_USERNAME'] = "matiscakosky"
    os.environ['GIT_PASSWORD'] = "mati38707339"
    g = Git("/mnt/c/users/usuario/desktop/fiuba/Organizacion de datos/La otra/finger 4") #path to local repo
    subir()
    g.push("origin","master")
    
def subir():
    git(["add", "--no-ignore-removal", "."])
    s=git(["commit", "-m", "commit desde pythoN2"])
    print("comiteo")
    
def git(args):
    print("Holaaaaaaa")
    subprocess.run(["git"] + args, cwd=a)
    return

main()