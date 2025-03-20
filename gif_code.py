import imageio
images = ['team-pic1.png', 'team-pic2.png']
data = [imageio.imread(img) for img in images]
imageio.mimsave('team.gif', data, duration=500, loop=0)
