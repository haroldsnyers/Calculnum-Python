from scipy import misc

face = misc.face (gray = True )
misc.imsave('face.orig.jpg', face)

c = face.copy()
c[c >100] = 255
misc . imsave ('face_new.jpg', c)
