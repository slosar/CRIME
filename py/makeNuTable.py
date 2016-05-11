#!/usr/bin/env python
import numpy as np
for line in open('param_GetHI.ini').readlines():
    try:
        key,val=line.split()
    except:
        continue
    
    if 'nu_min' in key:
        nu_min=float(val)
    elif 'nu_max' in key:
        nu_max=float(val)
    elif 'n_nu' in key:
        n_nu=int(val)

of=open('output/nuTable.txt','w')
nu21=1420.40575177
for i in range(n_nu):
    fmin=nu_min+(nu_max-nu_min)*(i+0.)/n_nu
    fmax=nu_min+(nu_max-nu_min)*(i+1.)/n_nu
    zmin,zmax=nu21/fmin-1, nu21/fmax-1
    of.write("%i %g %g %g %g\n"%(i+1,fmin,fmax, zmax,zmin))
of.close()

    
