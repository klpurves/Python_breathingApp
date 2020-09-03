"""App to test time stamp accuracy compared with SCR collected from empatico.

Idea is simple, click a button when you start breathing in, another when you reach peak,
another when you start breathing out and last button click when your lungs aere empty.

Can try map this onto SCR timestamps.

KLP
09/2012"""


#NOTE: taken base code from blog example of animation using matplotlib
#https://gist.github.com/hugke729/ac3cf36500f2f0574a6f4ffe40986b4f.
#Major adaptations, including animation featues:
#Wrapped withing an animate function and added pause functionality
#And data features:
#added time stamping and other features.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Use matplotlib ggplot stylesheet if available
try:
    plt.style.use('ggplot')
except:
    pass

# Set which type of animation will be plotted. One of:
#  pcolor,  contour
animation_type = 'contour'

# Create three-dimensional array of data G(x, z, t)
x = np.linspace(-4, 4, 91)
t = np.linspace(0, 25, 30)
y = np.linspace(-4, 4, 91)
X3, Y3, T3 = np.meshgrid(x, y, t)
sinT3 = np.sin(2*np.pi*T3 /
               T3.max(axis=2)[..., np.newaxis])
G = (X3**2 + Y3**2)*sinT3


# ----------------------------------------------------------------------------
# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

if animation_type not in ['line', 'scatter']:
    ax.set_aspect('equal')


# ----------------------------------------------------------------------------
if animation_type == 'pcolor':
    cax = ax.pcolormesh(x, y, G[:-1, :-1, 0], vmin=-4, vmax=1, cmap='Blues')
    fig.colorbar(cax)

    def animate(i):
        cax.set_array(G[:-1, :-1, i].flatten())

# ----------------------------------------------------------------------------


if animation_type == 'contour':
    # Keyword options used in every call to contour
    contour_opts = {'levels': np.linspace(-9, 9, 10), 'cmap':'RdBu', 'lw': 2}
    cax = ax.contour(x, y, G[..., 0], **contour_opts)

    def animate(i):
        ax.collections = []
        ax.contour(x, y, G[..., i], **contour_opts)


## set up animarion function including play/pause

def run_animation():
    anim_running = True

    def onClick(event):
        current_datetime = datetime.now() # NOTE: Acquire the date time (to ms) on each click
        print(current_datetime)
        nonlocal anim_running
        if anim_running:
            anim.event_source.stop()
            anim_running = False
        else:
            anim.event_source.start()
            anim_running = True

    fig.canvas.mpl_connect('button_press_event', onClick)

    anim = FuncAnimation(fig, animate, interval=300, frames=len(t)-1, repeat=True)

    plt.show()

run_animation()
