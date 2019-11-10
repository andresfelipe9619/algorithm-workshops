from tkinter import * 

"""3ER PUNTO"""
"""
cursos: arreglo[]
curso[]
nombre: cadena
creditos: entero
nota: float
nxc: float

nombre = ingresa valor
agrega nombre en curso

creitos = ingresa valor
agrega creditos en curso

nota = ingresa valor
agrega nota en curso

nxc = nota * curso
agrega nxc en cursos

agrega curso en cursos

saca promedio
    resultado: float
    por cada curso en cursos suma sus creditos y nxc
    divide suma nxc sobre suma 
    muestra resultado"""

cursos = []
def miCurso():
    """
    nombre = ingresa valor
    agrega nombre en curso

    creitos = ingresa valor
    agrega creditos en curso

    nota = ingresa valor
    agrega nota en curso

    nxc = nota * creditos
    agrega nxc en cursos

    """
    curso = []
    nombre = ENombre.get()
    creditos = int(ECreditos.get())
    nota = float(ENota.get())
    nxc = creditos * nota

    curso.append(nombre)
    curso.append(creditos)
    curso.append(nota)
    curso.append(nxc)
    
    return curso

def agregaCurso():
    """agrega curso en cursos"""
    curso = miCurso()
    cursos.append(curso)
    ENombre.delete(0, END)
    ECreditos.delete(0, END)
    ENota.delete(0, END)

def promedio():
    """
    resultado: float
    por cada curso en cursos suma sus creditos y nxc
    divide suma nxc sobre suma 
    muestra resultado   
    """
    sumaNC = 0
    sumaC = 0
    
    for curso in cursos:
        sumaC += curso[1]#creditos del curso
        sumaNC += curso[3]#creditos * notas
    
    resultado = sumaNC/sumaC
    EResultado.delete("1.0", END)
    EResultado.insert("1.0", "El promedio ponderado de su semestre es "+ str(resultado))
    

def listarCursos():
    """
    por cada curso en curso imprimir su informacion
    """
    EResultado.delete("1.0", END)
    EResultado.insert(END, "Los cursos que tiene matriculados son:\n")
    texto = "Cursos     Creditos        Nota\n"
    for curso in cursos:
        texto += curso[0]+"             "+str(curso[1])+"           "+str(curso[2])+"\n"#imprime nombre, creditos y nota del curso
    EResultado.insert(END, texto)

gui = Tk()

gui.geometry("450x450")

LNombre = Label(gui, text="Nombre Curso")
ENombre = Entry(gui, width=30)
LCreditos= Label(gui, text="Creditos")
ECreditos = Entry(gui, width=30)
LNota = Label(gui, text="Nota")
ENota = Entry(gui, width=30)

BIngresa = Button(gui, text="Ingresar Curso", command=agregaCurso)
BPromedio = Button(gui, text="Calcular Promedio", command=promedio)
EResultado = Text(gui, width=50, height=10)
BListar = Button(gui, text="Listar", command=listarCursos)

LNombre.place(x=20, y=20)
ENombre.place(x=140, y=20)
LCreditos.place(x=20, y=70)
ECreditos.place(x=140, y=70)
LNota.place(x=20, y=120)
ENota.place(x=140, y=120)
BIngresa.place(x=330, y=70)
BPromedio.place(x=20, y=170)
EResultado.place(x=20, y=220)
BListar.place(x=340, y=170)


gui.mainloop()
