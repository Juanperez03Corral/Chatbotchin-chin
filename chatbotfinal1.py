#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 11:28:06 2025

@author: juan
"""

import streamlit as st

# Configuración de la app
st.set_page_config(page_title="Chin Chin - Tu Sumiller Virtual", page_icon="🍷", layout="centered")

# Estado de sesión
if 'bodega' not in st.session_state:
    st.session_state.bodega = []
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []
if 'supermercado_vinos' not in st.session_state:
    st.session_state.supermercado_vinos = [
        # Lidl
        ("Lidl", "Cepa Lebrel Crianza - 4,80€"),
        ("Lidl", "Rosso Toscano IGT - 5,20€"),
        ("Lidl", "Albanta Albariño - 6,50€"),
        ("Lidl", "Barón de Rivero Reserva - 5,90€"),
        ("Lidl", "Montequinto Verdejo - 4,30€"),
        ("Lidl", "Mademoiselle Comédie Rosé - 5,00€"),
        ("Lidl", "Arestel Cava Brut - 3,75€"),

        # Mercadona
        ("Mercadona", "Castillo de Liria Tinto - 3,20€"),
        ("Mercadona", "Marqués de Cáceres Crianza - 8,50€"),
        ("Mercadona", "Pata Negra Apasionado - 5,40€"),
        ("Mercadona", "Blume Verdejo - 4,50€"),
        ("Mercadona", "Señorío de los Llanos Reserva - 4,90€"),
        ("Mercadona", "Gran Castillo Rosé - 3,80€"),
        ("Mercadona", "Viña Tendida Semi Seco - 3,60€"),

        # Carrefour
        ("Carrefour", "Viña Albali Reserva - 6,95€"),
        ("Carrefour", "Ramón Bilbao Crianza - 9,50€"),
        ("Carrefour", "Marqués de Cáceres Verdejo - 7,20€"),
        ("Carrefour", "Legaris Roble - 8,90€"),
        ("Carrefour", "Campo Viejo Rosado - 6,00€"),
        ("Carrefour", "Segura Viudas Brut Reserva - 7,80€"),
        ("Carrefour", "Viñas del Vero Chardonnay - 8,50€"),

        # Alcampo
        ("Alcampo", "Protos Roble - 11,00€"),
        ("Alcampo", "Enate Chardonnay 234 - 14,00€"),
        ("Alcampo", "Viñas del Vero Merlot - 8,70€"),
        ("Alcampo", "Señorío de Lazán Reserva - 10,50€"),
        ("Alcampo", "Alquez Garnacha - 13,90€"),
        ("Alcampo", "Faustino VII Rosado - 6,20€"),
        ("Alcampo", "Codorníu Clasico Brut - 5,90€"),

        # Otros
        ("Otros", "Mar de Frades Albariño - 16,00€"),
        ("Otros", "Pago de Carraovejas Crianza - 36,00€"),
        ("Otros", "Taittinger Brut Réserve - 42,00€"),
        ("Otros", "Dominio de Atauta - 48,00€"),
        ("Otros", "El Grifo Malvasía Seco - 18,00€"),
        ("Otros", "Jean Leon 3055 Rosé - 14,00€"),
        ("Otros", "Juve & Camps Reserva de la Familia - 21,00€")
    ]

# === FUNCIONES ===

def mostrar_planes():
    st.markdown("## 🧾 Planes de suscripción")
    st.info("""
    **Plan básico – Gratis**  
    - Comparación de vinos en supermercados  
    - Acceso a rankings  
    - 3 recomendaciones semanales  

    **Plan rioja – 9,99€/mes**  
    - Recomendaciones ilimitadas  
    - Registro y control de bodega  

    **Plan albariño – 24,99€/mes**  
    - Todo lo anterior  
    - Pack mensual de 3 vinos  
    - Catas virtuales  

    **Plan cabernet sauvignon – 49,99€/mes**  
    - Todo lo anterior  
    - Acceso a eventos y visitas a bodegas  
    - Descuentos en vinos y actividades  
    """)

def recomendaciones_comida(plan):
    st.subheader("🍽️ ¿Qué estás comiendo?")
    comida = st.selectbox("Tipo de comida", [
        "Carne roja", "Carne blanca", "Pescado", "Marisco",
        "Pasta con salsa", "Quesos fuertes", "Quesos suaves", "Dulces",
        "Ensaladas", "Vegetariano", "Barbacoa"
    ])

    recomendaciones = {
        "Carne roja": "Cabernet Sauvignon, Syrah, Ribera del Duero",
        "Carne blanca": "Garnacha suave, Chardonnay con barrica",
        "Pescado": "Albariño, Verdejo, Godello",
        "Marisco": "Rías Baixas, Sauvignon Blanc",
        "Pasta con salsa": "Chianti, Tempranillo joven",
        "Quesos fuertes": "Oporto, Syrah",
        "Quesos suaves": "Rosado seco o Chardonnay",
        "Dulces": "Moscatel, PX, cava semiseco",
        "Ensaladas": "Verdejo, rosado joven",
        "Vegetariano": "Pinot Noir, Riesling",
        "Barbacoa": "Zinfandel, Malbec"
    }

    st.success(f"🍷 Recomendación: {recomendaciones[comida]}")
    if plan != "Gratis" and st.button("Guardar en favoritos"):
        st.session_state.favoritos.append(f"{comida}: {recomendaciones[comida]}")
        st.toast("¡Añadido a favoritos!")

def gestion_bodega(plan):
    if plan in ["9,99€/mes", "24,99€/mes", "49,99€/mes"]:
        st.subheader("📦 Tu Bodega Personal")
        for vino in st.session_state.bodega:
            st.write(f"🍾 {vino}")
        nuevo = st.text_input("Añadir vino")
        if st.button("Agregar"):
            if nuevo:
                st.session_state.bodega.append(nuevo)
                st.success(f"'{nuevo}' añadido a tu bodega.")
            else:
                st.warning("Introduce un nombre válido.")
    else:
        st.warning("Función disponible a partir del Plan rioja.")

def comparar_supermercados():
    st.subheader("🛒 Comparativa de Vinos en Supermercados")
    supermercado = st.selectbox("Supermercado", ["Mercadona", "Carrefour", "Lidl", "Alcampo", "Otros"])

    st.write(f"### Vinos disponibles en **{supermercado}**:")
    for tienda, vino in st.session_state.supermercado_vinos:
        if tienda == supermercado:
            st.write(f"🍾 {vino}")

def buscar_por_tipo():
    st.subheader("🔎 Buscar por tipo de vino")
    tipo = st.selectbox("Selecciona el tipo de vino", ["Tinto", "Blanco", "Rosado", "Espumoso", "Dulce"])

    ejemplos = {
        "Tinto": ["Protos Roble", "Ramón Bilbao Crianza", "Pago de Carraovejas Crianza"],
        "Blanco": ["Enate Chardonnay", "Albanta Albariño", "Blume Verdejo"],
        "Rosado": ["Jean Leon 3055 Rosé", "Gran Castillo Rosé", "Campo Viejo Rosado"],
        "Espumoso": ["Codorníu Clasico Brut", "Segura Viudas Brut Reserva", "Juve & Camps Reserva de la Familia"],
        "Dulce": ["Viña Tendida Semi Seco", "Moscatel Oro Floralis", "PX Alvear"]
    }

    st.success(f"🍷 Algunos ejemplos de vinos {tipo.lower()}s:")
    for vino in ejemplos[tipo]:
        st.write(f"👉 {vino}")

def ver_favoritos():
    st.subheader("⭐ Favoritos")
    if st.session_state.favoritos:
        for fav in st.session_state.favoritos:
            st.write(f"👉 {fav}")
    else:
        st.info("No tienes favoritos guardados.")

def suscripcion_mensual(plan):
    if plan in ["24,99€/mes", "49,99€/mes"]:
        st.success("""
        Tu pack mensual de 3 vinos está en camino.  
        Incluye cata virtual con nota de cata y maridaje.
        """)
    else:
        st.warning("Disponible desde el Plan albariño.")

def actividades_y_visitas(plan):
    if plan == "49,99€/mes":
        st.balloons()
        st.markdown("""
        ### 🍇 Próximas experiencias
        - Visita a la bodega Marqués de Riscal – 24 de junio  
        - Cata de blancos–  30 de junio  
        - Paint and Wine– 10 de julio   
        **Descuento aplicado automáticamente.**
        """)
    else:
        st.warning("Disponible solo para el Plan cabernet sauvignon.")

# === APP ===

st.title("🍷 Chin Chin – Tu Sumiller Virtual para Particulares")

mostrar_planes()

plan = st.selectbox("Selecciona tu plan actual", ["Gratis", "9,99€/mes", "24,99€/mes", "49,99€/mes"])

seccion = st.radio("¿Qué quieres hacer?", [
    "📌 Recomendaciones por comida",
    "📦 Mi bodega",
    "⭐ Favoritos",
    "📬 Suscripción mensual",
    "🎟️ Actividades y eventos",
    "🛒 Comparar vinos de supermercado",
    "🔎 Buscar por tipo de vino"
])

if seccion == "📌 Recomendaciones por comida":
    recomendaciones_comida(plan)

elif seccion == "📦 Mi bodega":
    gestion_bodega(plan)

elif seccion == "⭐ Favoritos":
    ver_favoritos()

elif seccion == "📬 Suscripción mensual":
    suscripcion_mensual(plan)

elif seccion == "🎟️ Actividades y eventos":
    actividades_y_visitas(plan)

elif seccion == "🛒 Comparar vinos de supermercado":
    comparar_supermercados()

elif seccion == "🔎 Buscar por tipo de vino":
    buscar_por_tipo()
