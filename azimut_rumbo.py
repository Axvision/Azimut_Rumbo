import streamlit as st
from math import atan2, degrees

st.title("Calculadora de Azimut y Rumbo")

st.markdown("Ingrese las coordenadas de los puntos A y B:")

col1, col2 = st.columns(2)

with col1:
    x1 = st.number_input("X1", value=0.0)
    y1 = st.number_input("Y1", value=0.0)

with col2:
    x2 = st.number_input("X2", value=0.0)
    y2 = st.number_input("Y2", value=0.0)

if st.button("Calcular"):
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        st.error("Los puntos A y B son iguales. No se puede calcular el azimut.")
    else:
        azimut = (degrees(atan2(dx, dy)) + 360) % 360

        # Determinar rumbo
        if azimut < 90:
            rumbo = f"{azimut:.2f}° NE"
        elif azimut < 180:
            rumbo = f"{180 - azimut:.2f}° SE"
        elif azimut < 270:
            rumbo = f"{azimut - 180:.2f}° SW"
        else:
            rumbo = f"{360 - azimut:.2f}° NW"

        st.success(f"**Azimut:** {azimut:.2f}°")
        st.info(f"**Rumbo:** {rumbo}")
