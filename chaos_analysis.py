import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

import chaos_classes as cf
import warnings

#suppress warnings
warnings.filterwarnings('ignore')

# plotting parameters
plt.rcParams.update({'font.size': 6})

# variables
amplitude = 1
a = -np.pi
b = np.pi
n = 5000
h = (b-a)/n

# functions
def p_title(_p1, _p2):
    if _p1 and _p2:
        return str(r'$exponents\;p_1=%s$ $\;p_2=%s$' % (_p1,_p2))
    if _p1:
        return str(r'$exponent\;p=%s$' % _p1)

# linear space and functions
q = np.linspace(a, b, n)

# set plot parameters
fig, ax = plt.subplots(figsize=(5, 5),dpi=600)
ax.set_ylim(-amplitude, amplitude)
ax.set_xlim(a,b)
ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\\pi$'))
ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))


def set_plot():
    import argparse
    from sys import exit
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--plot", type=str, help="cos_sin_2, cos_sin_1, cos_1, sin_1, sin_2, sinc")
    args = parser.parse_args()
    if args.plot is None:
        parser.print_help()
        exit()
    else:
        return args.plot

if __name__ == '__main__':
    try:
        plot = set_plot()
        print(f'plotting {plot} ...')
        # based on product of cosine and sine
        if plot == 'cos_sin_1':
            chaos_function, plot_color, label, p1, p2 = cf.ChaosFunctionsMultiExponent(q, 3, 5, 1).cos_sin_1()
            plot_name = 'cos_sin_1.png'

        if plot == 'cos_sin_2':
            chaos_function, plot_color, label, p1, p2 = cf.ChaosFunctionsMultiExponent(q, 5, 4, 1).cos_sin_2()
            plot_name = 'cos_sin_2.png'

        # based on cosine
        if plot == 'cos_1':
            chaos_function, plot_color, label, p1, p2 = cf.ChaosFunctions(q, 3, 1).cos_1()
            plot_name = 'cos_1.png'

        # based on sine
        if plot == 'sin_1':
            chaos_function, plot_color, label, p1, p2 = cf.ChaosFunctions(q, 15, 1).sin_1()
            plot_name = 'sin_1.png'
        if plot == 'sin_2':
            chaos_function, plot_color, label, p1, p2 = cf.ChaosFunctions(q, 1, 1).sin_2()
            plot_name = 'sin_2.png'
        if plot == 'sinc':
            chaos_function, plot_color, label, p1, p2 = cf.SincFunction(q,10, 0.75).sinc()
            plot_name = 'sinc.png'

        # plot
        ax.plot(q, chaos_function, label=label, linewidth=0.95, color=plot_color,linestyle='solid', alpha=0.65)

        # plot details
        plt.title(p_title(p1,p2) + str(r'$\;\;samples = %s$' % n), fontsize=5)
        plt.yticks(fontsize=5)
        plt.xticks(fontsize=5)
        plt.grid(linestyle='--', linewidth=0.65, color='black')
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig('/home/xmondo/Desktop/figures/%s' % plot_name)

    except Exception as err:
        print(err)