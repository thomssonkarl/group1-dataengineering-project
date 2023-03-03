import h5py


hdf5_file = h5py.File('./A/TRAAAAW128F429D538.h5', 'r')

song = hdf5_file['/analysis/songs']

tempo = song[0]['tempo'][()]
print(f"Song: tempo = {tempo}")

