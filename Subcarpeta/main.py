# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:02:18 2019

@author: Usuario
"""
import subprocess
import pathlib
a=pathlib.Path(r"/mnt/c/users/usuario/desktop/fiuba/Organizacion de datos/La otra/finger 4/Subcarpeta")


def main():
    subir()
    
def subir():
    git(["add", "--no-ignore-removal", "."])
    s=git(["commit", "-m", "commit desde pythoN2"])
    s=git(["push", "--force-with-lease", "origin", "master"])
    print("termino")
    
def git(args):
    print("Holaaaa")
    subprocess.run(["git"] + args, cwd=a,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return

main()