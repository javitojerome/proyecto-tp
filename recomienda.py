# Definición de los arreglos
alimentos = [
    "Proteínas magras: Pechuga de pollo, pescado, tofu, claras de huevo",
    "Verduras y hortalizas: Espinacas, brócoli, zanahorias, pimientos",
    "Frutas: Manzanas, bayas, naranjas",
    "Granos enteros: Avena, quinoa, arroz integral",
    "Legumbres: Lentejas, garbanzos, frijoles",
    "Proteínas: Carne magra (res, cerdo), pescado, huevos, productos lácteos",
    "Carbohidratos complejos: Patatas, batatas, arroz integral, avena",
    "Grasas saludables: Aguacate, nueces, semillas, aceite de oliva",
    "Lácteos ricos en proteínas: Yogur griego, queso cottage",
    "Batidos de proteínas",
    "Proteínas equilibradas: Pescado, huevos, legumbres",
    "Frutas y verduras variadas",
    "Granos enteros: Avena, quinoa, cebada",
    "Hidratación: Beber suficiente agua",
    "Grasas saludables: Frutos secos, pescado, aceite de oliva"
]

ejercicios = [
    "Cardio: Correr, nadar, ciclismo, saltar la cuerda",
    "Entrenamiento en intervalos de alta intensidad (HIIT)",
    "Entrenamiento de fuerza: Sentadillas, flexiones, levantamiento de pesas ligeras",
    "Entrenamiento con pesas: Sentadillas, press de banca, peso muerto, dominadas",
    "Entrenamiento en circuito",
    "Ejercicios compuestos: Press militar, estocadas, remo con barra",
    "Entrenamiento de resistencia: Caminar, nadar, andar en bicicleta",
    "Ejercicios de flexibilidad: Yoga, estiramientos",
    "Entrenamiento funcional: Movimientos que imitan actividades diarias"
]

# Diccionario de recomendaciones con elementos directamente
recomendaciones = {
    "bajar_de_peso": {
        "alimentos_recomendados": [
            alimentos[0],  # Proteínas magras
            alimentos[1],  # Verduras y hortalizas
            alimentos[2],  # Frutas
            alimentos[3],  # Granos enteros
            alimentos[4]   # Legumbres
        ],
        "ejercicios_recomendados": [
            ejercicios[0],  # Cardio
            ejercicios[1],  # HIIT
            ejercicios[2]   # Entrenamiento de fuerza
        ]
    },
    "ganar_masa_muscular": {
        "alimentos_recomendados": [
            alimentos[5],  # Proteínas
            alimentos[6],  # Carbohidratos complejos
            alimentos[7],  # Grasas saludables
            alimentos[8],  # Lácteos ricos en proteínas
            alimentos[9]   # Batidos de proteínas
        ],
        "ejercicios_recomendados": [
            ejercicios[3],  # Entrenamiento con pesas
            ejercicios[4],  # Entrenamiento en circuito
            ejercicios[5]   # Ejercicios compuestos
        ]
    },
    "mantener_estilo_de_vida_saludable": {
        "alimentos_recomendados": [
            alimentos[10], # Proteínas equilibradas
            alimentos[11], # Frutas y verduras variadas
            alimentos[12], # Granos enteros
            alimentos[13], # Hidratación
            alimentos[14]  # Grasas saludables
        ],
        "ejercicios_recomendados": [
            ejercicios[6],  # Entrenamiento de resistencia
            ejercicios[7],  # Ejercicios de flexibilidad
            ejercicios[8]   # Entrenamiento funcional
        ]
    }
}