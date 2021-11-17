import os

def py(File_Path,idle:bool = False):
    if idle == False:
        os.system("F:")
        os.system(f"open F:/projectpy/{File_Path}")

    elif idle == True:
        os.system("F:")
        os.system(f"python -m idlelib {File_Path}")

def b4a(File_Path):
    os.system("F:")
    os.system(f"open F:/projectb4a/{File_Path}")

def cs(File_Path):
    os.system("F:")
    os.system(f"open F:/projectc#/{File_Path}")

def js(File_Path):
    os.system("F:")
    os.system(f"open F:/projectjs/{File_Path}")

def vb(File_Path):
    os.system("F:")
    os.system(f"open F:/projectvb/{File_Path}")

def web(File_Path):
    os.system("F:")
    os.system(f"open F:/projectweb/{File_Path}")