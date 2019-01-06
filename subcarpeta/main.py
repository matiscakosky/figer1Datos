# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:02:18 2019

@author: Usuario
"""
import subprocess
import pathlib
a=pathlib.Path(r"/mnt/c/users/usuario/desktop/fiuba/Organizacion de datos/La otra/finger 4/subcarpeta")


def main():
    subir()
    
def subir():
    git(["add", "--no-ignore-removal", "."])
    s=git(["commit", "-m", "commit desde pythoN"])
    print(s.output)
    s=git(["push", "--force-with-lease", "origin", "master"])
    print(s.output)
    
def git(args):
    print("gola")
    subprocess.run(["git"] + args, cwd=a,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return

main()