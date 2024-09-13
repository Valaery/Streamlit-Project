from pickle import load
import streamlit as st

# Cargar el modelo
model = load(open("decision_tree_diabetes.sav", "rb"))

# Diccionario de clases
class_dict = {
    "0": "Negativo en diabetes",
    "1": "Positivo en diabetes"
}

st.title("Predicción de Diabetes")

# Sliders para las entradas del modelo
val1 = st.slider("Número de embarazos (Pregnancies)", min_value=0, max_value=20, step=1)
val2 = st.slider("Glucosa (Glucose)", min_value=0, max_value=200, step=1)
val3 = st.slider("Presión sanguínea (BloodPressure)", min_value=0, max_value=140, step=1)
val4 = st.slider("Espesor de la piel (SkinThickness)", min_value=0, max_value=100, step=1)
val5 = st.slider("Insulina (Insulin)", min_value=0, max_value=900, step=1)
val6 = st.slider("Índice de masa corporal (BMI)", min_value=0.0, max_value=70.0, step=0.1)
val7 = st.slider("Función de Pedigrí de Diabetes (DiabetesPedigreeFunction)", min_value=0.0, max_value=2.5, step=0.01)
val8 = st.slider("Edad (Age)", min_value=0, max_value=100, step=1)

if st.button("Predecir"):
    # Realizar la predicción
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])[0])
    pred_class = class_dict[prediction]
    st.write("Predicción:", pred_class)