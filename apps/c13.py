#Graficado-simple.py

from bokeh.plotting import figure, output_file, show

#ejecucion normal
#if __name__ == '__main__':
#Ejecucion desde main
def run(parameters):
    output_file('graficado_simple.html')
    fig = figure()
    
    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}: '))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)