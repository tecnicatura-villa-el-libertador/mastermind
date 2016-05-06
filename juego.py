def reportar(numero,plenos,parciales):
	
	if plenos + parciales <2:
		s = "El numero {} tiene {} pleno y {} parcial:estas mas lejos"
	if plenos >=2  or parciales >=3:
		s = "El numero {} tiene {} plenos y {} parciales:dale que va"
	else: 
   	    s = "El numero {} tiene {} plenos y {} parciales:ya lo tenes"
    

	return s.format(numero,plenos,parciales)   

print (reportar(1234, 0, 4 ))
