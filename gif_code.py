import imageio
images = ['chicklet1.png', 'chicklet2.png','chicklet3.png','chicklet4.png']
data = [imageio.imread(img) for img in images]
imageio.mimsave('team.gif', data, duration=500, loop=0)
