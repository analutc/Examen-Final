import streamlit as st

# Diccionario de ejemplo con información de fármacos
drug_info = {
    "Paracetamol": {
        "Grupo Farmacológico": "Analgésico y antipirético",
        "Vías de Administración": "Oral, Rectal, Intravenosa",
        "Mecanismo de Acción": "Inhibe la síntesis de prostaglandinas en el sistema nervioso central",
        "Efectos Adversos": "Hepatotoxicidad, reacciones alérgicas"
    },
    "Ibuprofeno": {
        "Grupo Farmacológico": "Antiinflamatorio no esteroideo (AINE)",
        "Vías de Administración": "Oral, Tópica",
        "Mecanismo de Acción": "Inhibe la enzima ciclooxigenasa (COX), reduciendo la síntesis de prostaglandinas",
        "Efectos Adversos": "Gastrointestinales, renales, cardiovasculares"
    }
    # Agrega más fármacos según sea necesario
}

# Título de la aplicación
st.title("Información de Fármacos")
st.text("En el curso de Farmacología es importante tener información básica de un fármaco. Con está app se podrá tener información básica de utilidad sobre los fármacos. Actualmente tiene solo dos en su base de datos Paracetamol e Ibuprofeno. Si es otro fármaco dirá Fármaco no encotrado")
# Entrada de texto para el nombre del fármaco
drug_name = st.text_input("Introduce el nombre del fármaco:")

# Buscar y mostrar la información del fármaco
if drug_name:
    info = drug_info.get(drug_name)
    if info:
        st.subheader(f"Información sobre {drug_name}")
        st.write(f"**Grupo Farmacológico:** {info['Grupo Farmacológico']}")
        st.write(f"**Vías de Administración:** {info['Vías de Administración']}")
        st.write(f"**Mecanismo de Acción:** {info['Mecanismo de Acción']}")
        st.write(f"**Efectos Adversos:** {info['Efectos Adversos']}")
    else:
        st.error("Fármaco no encontrado. Por favor, verifica el nombre e intenta nuevamente.")

# Ejecuta la aplicación con: streamlit run app.py
