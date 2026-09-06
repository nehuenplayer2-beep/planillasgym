import textwrap

import streamlit as st

# ============================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================
st.set_page_config(
    page_title="PERFORM | Entrenamiento y Nutrición de Alto Rendimiento",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS PERSONALIZADO (estética dark / premium tipo Lathos Academy)
# ============================================================
CUSTOM_CSS = """
<style>
    /* ---------- Variables de color ---------- */
    :root {
        --bg-primary: #17181c;
        --bg-secondary: #1e1f24;
        --bg-card: #232429;
        --accent: #c9ff3d;       /* verde lima neón */
        --accent-soft: rgba(201, 255, 61, 0.12);
        --text-primary: #f5f5f5;
        --text-secondary: #a3a3ab;
        --border-subtle: #33343a;
    }

    /* ---------- Reset general ---------- */
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', 'Segoe UI', sans-serif;
        background-color: var(--bg-primary);
        color: var(--text-primary);
    }

    .stApp {
        background: radial-gradient(circle at top, #202127 0%, #17181c 60%);
    }

    #MainMenu, footer, header {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* ---------- Navbar simple ---------- */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0 2rem 0;
        border-bottom: 1px solid var(--border-subtle);
        margin-bottom: 2rem;
    }
    .navbar .logo {
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 2px;
        color: var(--text-primary);
    }
    .navbar .logo span { color: var(--accent); }

    /* ---------- Hero ---------- */
    .hero {
        text-align: center;
        padding: 4rem 1rem 3rem 1rem;
    }
    .hero-badge {
        display: inline-block;
        padding: 0.35rem 1rem;
        border: 1px solid var(--accent);
        border-radius: 30px;
        color: var(--accent);
        font-size: 0.8rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    .hero h1 {
        font-size: 3.4rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 1rem;
        letter-spacing: -1px;
    }
    .hero h1 .highlight { color: var(--accent); }
    .hero p.subtitle {
        font-size: 1.15rem;
        color: var(--text-secondary);
        max-width: 620px;
        margin: 0 auto 2.2rem auto;
        line-height: 1.6;
    }

    /* ---------- Botones CTA ---------- */
    .cta-row {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    .stButton>button {
        border-radius: 8px;
        padding: 0.7rem 1.8rem;
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        border: 1px solid var(--border-subtle);
        transition: all 0.25s ease;
    }
    .stButton>button[kind="primary"] {
        background-color: var(--accent);
        color: #0a0a0a;
        border: none;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(201, 255, 61, 0.18);
    }

    /* Botones tipo <a> con la misma pinta que los de Streamlit (para anchors y WhatsApp) */
    .cta-link-row {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }
    .cta-link {
        display: inline-block;
        text-decoration: none;
        border-radius: 8px;
        padding: 0.7rem 1.8rem;
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        transition: all 0.25s ease;
    }
    .cta-link.secondary {
        border: 1px solid var(--border-subtle);
        color: var(--text-primary);
        background-color: transparent;
    }
    .cta-link.primary {
        background-color: var(--accent);
        color: #0a0a0a;
        border: none;
    }
    .cta-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(201, 255, 61, 0.18);
    }

    /* ---------- Secciones ---------- */
    .section-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        margin-top: 1rem;
    }
    .section-subtitle {
        text-align: center;
        color: var(--text-secondary);
        margin-bottom: 3rem;
        font-size: 1rem;
    }

    /* ---------- Tarjetas de producto ---------- */
    .product-card {
        background-color: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 2rem 1.6rem;
        height: 100%;
        position: relative;
        box-shadow: 0 4px 18px rgba(0,0,0,0.35);
        transition: transform 0.25s ease, border-color 0.25s ease;
    }
    .product-card:hover {
        transform: translateY(-6px);
        border-color: var(--accent);
    }
    .product-card.popular {
        border: 1px solid var(--accent);
    }
    .badge-popular {
        position: absolute;
        top: -12px;
        right: 20px;
        background-color: var(--accent);
        color: #0a0a0a;
        font-size: 0.7rem;
        font-weight: 800;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .product-title {
        font-size: 1.3rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
    }
    .product-desc {
        color: var(--text-secondary);
        font-size: 0.92rem;
        line-height: 1.5;
        margin-bottom: 1.2rem;
        min-height: 45px;
    }
    .product-features {
        list-style: none;
        padding: 0;
        margin: 0 0 1.5rem 0;
    }
    .product-features li {
        font-size: 0.9rem;
        color: var(--text-primary);
        margin-bottom: 0.6rem;
        display: flex;
        align-items: flex-start;
        gap: 0.5rem;
    }
    .product-features li::before {
        content: "✓";
        color: var(--accent);
        font-weight: 800;
    }
    .product-price {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 1.2rem;
    }
    .product-price span {
        font-size: 0.95rem;
        color: var(--text-secondary);
        font-weight: 400;
    }

    /* ---------- Testimonios ---------- */
    .testimonial-card {
        background-color: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 1.8rem;
        height: 100%;
    }
    .testimonial-result {
        display: inline-block;
        background-color: var(--accent-soft);
        color: var(--accent);
        font-weight: 800;
        font-size: 0.85rem;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin-bottom: 1rem;
    }
    .testimonial-quote {
        font-size: 0.95rem;
        color: var(--text-primary);
        font-style: italic;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    .testimonial-name {
        font-weight: 700;
        color: var(--text-secondary);
        font-size: 0.88rem;
    }

    /* ---------- FAQ (expanders) ---------- */
    .streamlit-expanderHeader {
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
    }
    .streamlit-expanderContent {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-subtle) !important;
        border-top: none !important;
        color: var(--text-secondary) !important;
        border-radius: 0 0 10px 10px !important;
    }

    /* ---------- Footer ---------- */
    .footer {
        margin-top: 4rem;
        padding-top: 2.5rem;
        border-top: 1px solid var(--border-subtle);
        text-align: center;
        color: var(--text-secondary);
        font-size: 0.85rem;
    }
    .footer a {
        color: var(--text-secondary);
        text-decoration: none;
        margin: 0 0.8rem;
    }
    .footer a:hover { color: var(--accent); }
    .footer .socials {
        margin-bottom: 1rem;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ============================================================
# NAVBAR
# ============================================================
st.markdown(
    """
    <div class="navbar">
        <div class="logo">PERFORM<span>.</span></div>
        <div style="color:#9a9a9a; font-size:0.9rem;">ENTRENAMIENTO · NUTRICIÓN · CIENCIA</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">Alto Rendimiento · Basado en Ciencia</div>
        <h1>Transformá tu cuerpo.<br>Redefiní tu <span class="highlight">límite</span>.</h1>
        <p class="subtitle">
            Programas de entrenamiento y planes de nutrición diseñados con base científica
            para llevar tu físico y tu rendimiento al siguiente nivel. Sin atajos, sin humo:
            resultados medibles.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# TODO: reemplazá este número por tu WhatsApp real, formato: 549 + código de área + número (sin espacios ni +)
WHATSAPP_NUMERO = "TU_NUMERO_AQUI"
WHATSAPP_LINK_GENERAL = f"https://wa.me/{WHATSAPP_NUMERO}?text=Hola%2C%20quiero%20empezar%20con%20un%20programa"

st.markdown(
    f"""
    <div class="cta-link-row">
        <a href="#planes" class="cta-link secondary">Ver Programas</a>
        <a href="{WHATSAPP_LINK_GENERAL}" target="_blank" class="cta-link primary">Empezar Ahora</a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# SECCIÓN: NUESTROS INFOPRODUCTOS / PROGRAMAS
# ============================================================
st.markdown('<div id="planes" class="section-title">Nuestros Programas</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Elegí el plan que se ajusta a tu objetivo</div>',
    unsafe_allow_html=True,
)

productos = [
    {
        "titulo": "Hipertrofia · Definición/Volumen",
        "descripcion": "Rutina de 12 semanas para maximizar ganancia muscular o definición según tu fase.",
        "features": [
            "Rutina progresiva de 12 semanas",
            "Videos demostrativos de cada ejercicio",
            "Plantilla de seguimiento de cargas",
        ],
        "precio": "$49",
        "nota": "pago único",
        "popular": False,
    },
    {
        "titulo": "Nutrición Personalizada",
        "descripcion": "Ajuste de macros a tu medida con guía práctica de compras y recetas.",
        "features": [
            "Cálculo de macros personalizado",
            "Guía de compras semanal",
            "Recetario alto en proteína",
        ],
        "precio": "$39",
        "nota": "pago único",
        "popular": False,
    },
    {
        "titulo": "Pack Integral",
        "descripcion": "Entrenamiento + nutrición combinados en un solo sistema de alto rendimiento.",
        "features": [
            "Rutina de 12 semanas completa",
            "Plan de nutrición y macros",
            "Seguimiento y ajustes incluidos",
        ],
        "precio": "$69",
        "nota": "pago único",
        "popular": True,
    },
]

cols = st.columns(3)
for col, producto in zip(cols, productos):
    with col:
        popular_class = "product-card popular" if producto["popular"] else "product-card"
        badge_html = '<div class="badge-popular">Más Popular</div>' if producto["popular"] else ""
        features_html = "".join(f"<li>{f}</li>" for f in producto["features"])

        card_html = (
            f'<div class="{popular_class}">'
            f'{badge_html}'
            f'<div class="product-title">{producto["titulo"]}</div>'
            f'<div class="product-desc">{producto["descripcion"]}</div>'
            f'<ul class="product-features">{features_html}</ul>'
            f'<div class="product-price">{producto["precio"]} <span>/ {producto["nota"]}</span></div>'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)
        if st.button("Obtener Plan", key=f"btn_{producto['titulo']}", use_container_width=True, type="primary"):
            st.session_state["checkout_producto"] = producto["titulo"]

if "checkout_producto" in st.session_state:
    st.success(
        f"Redirigiendo a la pasarela de pago para: **{st.session_state['checkout_producto']}**... "
        f"(simulación — acá integrarías Stripe, MercadoPago, etc.)"
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================
# SECCIÓN: TESTIMONIOS / CASOS DE ÉXITO
# ============================================================
st.markdown('<div class="section-title">Casos de Éxito</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Resultados reales de personas reales</div>',
    unsafe_allow_html=True,
)

testimonios = [
    {
        "nombre": "Martina G.",
        "logro": "-8kg en 12 semanas",
        "cita": "Nunca pensé que podía ver resultados tan rápido siguiendo un plan estructurado. Cambió mi relación con el entrenamiento.",
    },
    {
        "nombre": "Lucas F.",
        "logro": "+6kg de masa magra",
        "cita": "La combinación de rutina y nutrición fue clave. Por primera vez entendí qué y por qué estaba comiendo.",
    },
    {
        "nombre": "Camila R.",
        "logro": "-12% grasa corporal",
        "cita": "El seguimiento y la claridad del plan me dieron la disciplina que me faltaba. Totalmente recomendable.",
    },
]

t_cols = st.columns(3)
for col, t in zip(t_cols, testimonios):
    with col:
        testimonial_html = (
            f'<div class="testimonial-card">'
            f'<div class="testimonial-result">{t["logro"]}</div>'
            f'<div class="testimonial-quote">"{t["cita"]}"</div>'
            f'<div class="testimonial-name">— {t["nombre"]}</div>'
            f'</div>'
        )
        st.markdown(testimonial_html, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================
# SECCIÓN: PREGUNTAS FRECUENTES (FAQ)
# ============================================================
st.markdown('<div class="section-title">Preguntas Frecuentes</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

faqs = [
    (
        "¿Cómo recibo mi plan tras la compra?",
        "Una vez confirmado el pago, recibís un correo con el acceso a tu plan en formato digital "
        "(PDF y/o planilla editable), junto con las instrucciones para empezar.",
    ),
    (
        "¿Es apto para principiantes?",
        "Sí. Todos los programas incluyen niveles de progresión, por lo que se pueden adaptar tanto "
        "a quienes recién empiezan como a quienes ya tienen experiencia entrenando.",
    ),
    (
        "¿Qué equipo necesito para las rutinas?",
        "La mayoría de las rutinas están pensadas para gimnasio convencional, pero también incluimos "
        "variantes con equipo mínimo o peso corporal según el plan elegido.",
    ),
]

for pregunta, respuesta in faqs:
    with st.expander(pregunta):
        st.write(respuesta)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <div class="footer">
        <div class="socials">
            <a href="#" target="_blank">Instagram</a>
            <a href="#" target="_blank">TikTok</a>
            <a href="#" target="_blank">YouTube</a>
        </div>
        <div>
            <a href="#">Términos de Servicio</a> ·
            <a href="#">Política de Privacidad</a>
        </div>
        <div style="margin-top: 1rem; opacity: 0.6;">
            © 2026 PERFORM. Todos los derechos reservados.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)