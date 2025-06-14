import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kalkulator Integral", layout="centered")

st.title("🧮 Aplikasi Integral dengan Python")
st.markdown("""
Masukkan fungsi yang ingin diintegralkan. Anda bisa memilih integral tak tentu atau tentu (dengan batas).
""")

# Input fungsi
fungsi_input = st.text_input("Fungsi f(x):", value="x**2")

# Pilih jenis integral
jenis = st.radio("Pilih jenis integral:", ["Tak Tentu", "Tentu"])

# Simbol
x = sp.symbols('x')

try:
    fungsi = sp.sympify(fungsi_input)

    # Jika integral tentu, masukkan batas
    if jenis == "Tentu":
        a = st.number_input("Batas bawah (a):", value=0.0)
        b = st.number_input("Batas atas (b):", value=2.0)
        hasil_integral = sp.integrate(fungsi, (x, a, b))
        st.latex(r"\int_{%s}^{%s} %s \,dx = %s" % (a, b, sp.latex(fungsi), sp.latex(hasil_integral)))

        # Plot grafik
        st.subheader("Visualisasi Kurva dan Area Integral")
        fx = sp.lambdify(x, fungsi, "numpy")
        x_vals = np.linspace(float(a)-1, float(b)+1, 400)
        y_vals = fx(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"f(x) = {fungsi_input}")
        ax.fill_between(x_vals, y_vals, where=(x_vals >= a) & (x_vals <= b), color='skyblue', alpha=0.5)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.set_title("Area di bawah kurva")
        ax.legend()
        st.pyplot(fig)

    else:
        hasil_integral = sp.integrate(fungsi, x)
        st.latex(r"\int %s \,dx = %s + C" % (sp.latex(fungsi), sp.latex(hasil_integral)))

except Exception as e:
    st.error(f"Terjadi kesalahan dalam memproses fungsi: {e}")
