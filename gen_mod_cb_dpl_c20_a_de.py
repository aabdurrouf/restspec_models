import os, sys
import numpy as np
from astropy.cosmology import *

from piXedfit.piXedfit_model import save_models_rest_spec

imf_type = 1 			# Chabrier (2003)
sfh_form = 4 			# double power law SFH form
dust_law = 1    	# Calzetti (2000) dust attenuation law
duste_switch = 1    	# turn on dust emission
add_neb_emission = 1 	# turn on nebular emission
add_agn = 1 			# turn on AGN dusty torus emission

nmodels = 100000
nproc = 5

params_range={'logzsol':[-2.0,0.2],'log_tau':[-1.0,1.5],'log_age':[-2.0,1.14],'log_alpha':[-2.0,2.0],
        'log_beta':[-2.0,2.0],'dust2':[0.0,4.0], 'gas_logu':[-4.0,-1.0], 
	'gas_logz':[-2.0,0.2], 'log_fagn':[-5.0,0.48], 'log_gamma': [-4.0,0.0], 'log_qpah': [-3.0,1.0], 
	'log_tauagn': [0.7,2.18], 'log_umin': [-1.0,1.39]}

name_out = 'mod_cb_dpl_c20_a_de_100k.hdf5'
save_models_rest_spec(imf_type=imf_type, sfh_form=sfh_form, dust_law=dust_law, params_range=params_range,
			duste_switch=duste_switch, add_neb_emission=add_neb_emission, add_agn=add_agn,
			nmodels=nmodels, nproc=nproc, name_out=name_out)


