import legibilidad

TextoDePrueba = '''
El sistema circulatorio es un complejo sistema de órganos, tejidos y fluidos que se encarga de transportar nutrientes, oxígeno y otros compuestos vitales a través del cuerpo humano. El corazón es el motor principal del sistema circulatorio, y está conectado a una red de vasos sanguíneos que forman dos circuitos: el sistema circulatorio pulmonar y el sistema circulatorio sistémico.
En el sistema circulatorio pulmonar, el corazón bombea la sangre a través de las arterias pulmonares hacia los pulmones, donde se realiza el intercambio de dióxido de carbono por oxígeno. La sangre oxigenada regresa al corazón a través de las venas pulmonares y se dirige al sistema circulatorio sistémico.
En el sistema circulatorio sistémico, el corazón bombea la sangre rica en oxígeno y nutrientes a través de la arteria aorta hacia los diferentes órganos y tejidos del cuerpo. La sangre es transportada a través de arterias más pequeñas y capilares, donde se produce el intercambio de nutrientes y oxígeno con las células. La sangre venosa, pobre en oxígeno, regresa al corazón a través de las venas y se dirige hacia los pulmones para su oxigenación.
'''

# Lecturabilidad 
fernandez = legibilidad.fernandez_huerta(TextoDePrueba)

# Comprensibilidad
gutierrez = legibilidad.gutierrez(TextoDePrueba)

# Perspicuidad
pazos = legibilidad.szigriszt_pazos(TextoDePrueba)

# Legibilidad
mu = legibilidad.mu(TextoDePrueba)

# Comprensibilidad de Crawford
crawford = legibilidad.crawford(TextoDePrueba)


# Interpretación de la lecturabilidad

print(f"Lecturabilidad: {legibilidad.interpretaL(fernandez)}")

# Interpretación de la comprensibilidad de Gutierrez
print(f"Comprensibilidad de Gutierrez: {legibilidad.gutierrez_interpret(gutierrez)}")

# Interpretación de la perspicuidad
print(f"Perspicuidad: {legibilidad.interpretaP(pazos)}")

# Interpretación de la perspicuidad de Inflesz
print(f"Perspicuidad de inflesz: {legibilidad.inflesz(pazos)}")

# Interpretación de la legibilidad
print(f"Legibilidad: {legibilidad.mu_interpret(mu)}")

# Años de escolaridad
print(f"Años de escolaridad: {crawford}")
