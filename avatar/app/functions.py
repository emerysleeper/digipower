import pagan


def creation(input_string):
    img = pagan.Avatar(input_string, pagan.SHA512).img
    return img





# Open the avatar image in an
# external image viewer.
# img.show()

# Set an output path and a file name.
# You don't need to specify a file ending.
# Choose a path depending on your OS.
# outpath = 'output/'
# filename = inpt

# Saves the avatar image as a .png file
# by omitting the path and name. The
# file endings will be generated automatically.
# img.save(outpath, filename)

# You can change the avatar input and
# hash function anytime.
# img.change('new input', pagan.SHA256)