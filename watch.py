import os
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate_coords(i):
    os.system("wsl.exe bash ./generate_image.sh")
    with open('data/output/test/results/json/processed.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    ax1.clear()
    ax1.set_title('Random Sequence')
    ax1.set_xlabel('X Coordinate')
    ax1.set_ylabel('Y Coordinate')
    vmin, vmax = 0, 1000
    for line in lines:
        b, x, y = line.strip().split(' ')
        x, y = float(x), float(y)
        vmin = min(vmin, x, y)
        vmax = max(vmax, x, y)
        ax1.text(float(x), float(y), b, fontsize=8, ha='center', va='center')
    ax1.set_xlim(vmin, vmax)
    ax1.set_ylim(vmin, vmax)

def animate_png(i):
    os.system("wsl.exe bash ./generate_image.sh")
    img = mpimg.imread('data/output/test/results/svg/random_sequence.colored.png')
    ax1.clear()
    ax1.imshow(img)

if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, animate_coords, interval=1000)
    plt.show()