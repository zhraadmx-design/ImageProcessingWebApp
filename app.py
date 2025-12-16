import streamlit as st
from PIL import Image
import numpy as np

# ================== KONFIGURASI ==================
st.set_page_config(
    page_title="Group 11 - Image Processing",
    page_icon="Sakura",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ================== TERJEMAHAN ==================
translations = {
    "id": {"lang": "Indonesia", "title": "GROUP 11", "subtitle": "Aplikasi Pengolahan Citra",
           "home": "HOME", "aplikasi": "APLIKASI", "about": "TENTANG KAMI",
           "tentang": "Tentang Aplikasi", "desc": "Aplikasi pengolahan citra berbasis Aljabar Linear dengan transformasi geometri & filtering menggunakan operasi matriks manual.",
           "fitur": "Fitur Tersedia:", "feat1": "Translation • Scaling • Rotation • Shearing • Reflection",
           "feat2": "Blur • Sharpen • Edge Detection • Grayscale • Negative",
           "tools": "Tools Transformasi", "upload": "Upload Gambar", "pilih": "Pilih transformasi",
           "original": "Original", "hasil": "Hasil:", "ourteam": "Our Team", "footer": "GROUP 11 • 2025"},
    "en": {"lang": "English", "title": "GROUP 11", "subtitle": "Image Processing Web",
           "home": "HOME", "aplikasi": "APP", "about": "ABOUT US",
           "tentang": "About the App", "desc": "An image processing app based on Linear Algebra featuring geometric transformations and filtering using manual matrix operations.",
           "fitur": "Available Features:", "feat1": "Translation • Scaling • Rotation • Shearing • Reflection",
           "feat2": "Blur • Sharpen • Edge Detection • Grayscale • Negative",
           "tools": "Transformation Tools", "upload": "Upload Image", "pilih": "Select transformation",
           "original": "Original", "hasil": "Result:", "ourteam": "Our Team", "footer": "GROUP 11 • 2025"},
    "zh": {"lang": "中文", "title": "GROUP 11", "subtitle": "图像处理应用",
           "home": "首页", "aplikasi": "应用", "about": "关于我们",
           "tentang": "关于应用", "desc": "基于线性代数的图像处理应用，手动矩阵运算实现几何变换和滤波。",
           "fitur": "可用功能：", "feat1": "平移 • 缩放 • 旋转 • 错切 • 反射",
           "feat2": "模糊 • 锐化 • 边缘检测 • 灰度 • 负片",
           "tools": "变换工具", "upload": "上传图片", "pilih": "选择变换",
           "original": "原图", "hasil": "结果：", "ourteam": "我们的团队", "footer": "GROUP 11 • 2025"}
}

lang = st.sidebar.selectbox("Bahasa • Language • 语言", ["Indonesia", "English", "中文"], index=0)
code = {"Indonesia": "id", "English": "en", "中文": "zh"}[lang]
t = translations[code]

# ================== TEMA PINK-BIRU MUDA (CANTIK BANGET!) ==================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&family=Playfair+Display:wght@700&display=swap');
    .stApp {background: linear-gradient(135deg, #fff0fb 0%, #fce7f9 20%, #f8d7f7 40%, #e0f2fe 70%, #ccedff 100%);}
    h1, h2, h3, h4 {font-family: 'Playfair Display', serif; background: linear-gradient(90deg, #ff6bcb, #6bb6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .stButton>button {background: linear-gradient(45deg, #ff6bcb, #6bb6ff); color: white; border: none; border-radius: 50px; padding: 1rem 3rem; font-size: 1.4rem; font-weight: 700; box-shadow: 0 10px 30px rgba(255,107,203,0.4);}
    .stButton>button:hover {transform: translateY(-8px); box-shadow: 0 20px 40px rgba(107,182,255,0.5);}
    .sidebar-title {font-size: 2.8rem; text-align: center; background: linear-gradient(90deg, #ff6bcb, #6bb6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .sidebar-subtitle {font-size: 1.3rem; text-align: center; color: #6bb6ff; font-weight: 600;}
    hr {border: 2px solid #ff6bcb; border-radius: 5px;}
</style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
st.sidebar.markdown('<div class="sidebar-title">GROUP 11</div>', unsafe_allow_html=True)
st.sidebar.markdown(f'<div class="sidebar-subtitle">{t["subtitle"]}</div>', unsafe_allow_html=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# ================== HEADER ==================
st.markdown(f"<h1 style='text-align:center; font-size:5rem;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align:center; font-size:2.5rem; margin-bottom:4rem; color:#6bb6ff;'>{t['subtitle']}</h2>", unsafe_allow_html=True)

# ================== NAVIGASI ==================
c1, c2, c3 = st.columns(3)
with c1: 
    if st.button(t["home"], width="stretch"): st.session_state.page = "home"
with c2: 
    if st.button(t["aplikasi"], width="stretch"): st.session_state.page = "aplikasi"
with c3: 
    if st.button(t["about"], width="stretch"): st.session_state.page = "about"

if "page" not in st.session_state:
    st.session_state.page = "home"

# ================== HOME ==================
if st.session_state.page == "home":
    st.markdown(f"<h2 style='text-align:center; margin-top:3rem;'>{t['tentang']}</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.9); padding:3rem; border-radius:30px; border:4px solid #ff6bcb; margin:2rem;">
        <p style="font-size:1.35rem; line-height:2; color:#2d1b4e; text-align:justify;">
        {t['desc']}
        </p>
        <h3 style="color:#6bb6ff; text-align:center;">{t['fitur']}</h3>
        <div style="columns:2; font-size:1.25rem; color:#9f56d3;">
            <ul><li>{t['feat1']}</li></ul>
            <ul><li>{t['feat2']}</li></ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================== APLIKASI ==================
elif st.session_state.page == "aplikasi":
    st.markdown(f"<h2 style='text-align:center; margin:4rem 0;'>{t['tools']}</h2>", unsafe_allow_html=True)
    
    uploaded = st.file_uploader(t["upload"], type=["jpg","jpeg","png"])
    
    if uploaded:
        img = Image.open(uploaded)
        img_array = np.array(img)
        
        st.markdown("### " + t["pilih"])
        option = st.selectbox("opt", [
            t["pilih"], "Grayscale", "Negative", "Blur", "Sharpen", "Edge Detection",
            "Translation", "Scaling", "Rotation 90°", "Reflection Horizontal", "Reflection Vertical"
        ])
        
        if option != t["pilih"]:
            # --- Transformasi ---
            if option == "Grayscale":
                gray = np.dot(img_array[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
                result = Image.fromarray(gray)
            elif option == "Negative":
                result = Image.fromarray(255 - img_array)
            elif option == "Blur":
                kernel = np.ones((7,7))/49
                result = Image.fromarray(np.clip(convolution(img_array, kernel),0,255).astype(np.uint8))
            elif option == "Sharpen":
                kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
                result = Image.fromarray(np.clip(convolution(img_array, kernel),0,255).astype(np.uint8))
            elif option == "Edge Detection":
                kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
                result = Image.fromarray(np.clip(convolution(img_array, kernel),0,255).astype(np.uint8))
            elif option == "Translation":
                dx = st.slider("Horizontal (px)", -400, 400, 0)
                dy = st.slider("Vertical (px)", -400, 400, 0)
                result = img.transform(img.size, Image.AFFINE, (1,0,dx,0,1,dy))
            elif option == "Scaling":
                scale = st.slider("Scale", 0.2, 3.0, 1.0, 0.1)
                result = img.resize((int(img.width*scale), int(img.height*scale)), Image.LANCZOS)
            elif option == "Rotation 90°":
                result = img.transpose(Image.ROTATE_90)
            elif option == "Reflection Horizontal":
                result = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif option == "Reflection Vertical":
                result = img.transpose(Image.FLIP_TOP_BOTTOM)
            else:
                result = img
                
            col1, col2 = st.columns(2)
            with col1: st.image(img, caption=t["original"], width="stretch")
            with col2: st.image(result, caption=f"{t['hasil']} {option}", width="stretch")
    else:
        st.info("Silakan upload gambar • Please upload an image • 请上传图片")

# ================== ABOUT US ==================
elif st.session_state.page == "about":
    st.markdown(f"<h2 style='text-align:center; margin:5rem 0;'>{t['ourteam']}</h2>", unsafe_allow_html=True)
    
    # Alya
    a1, a2 = st.columns([1,2])
    with a1:
        try: st.image("assets/alya.jpg", width="stretch")
        except: st.image("https://via.placeholder.com/300/ffc2e6/000?text=Alya", width="stretch")
    with a2:
        st.markdown("<div style='padding-left:2rem;'><h3>Alya</h3><p><strong>NIM:</strong> 240123456<br><strong>Role:</strong> Project Leader</p><p style='color:#6bb6ff; font-style:italic;'>Leading with grace</p></div>", unsafe_allow_html=True)
    
    # Nabila
    n1, n2 = st.columns([2,1])
    with n1:
        st.markdown("<div style='text-align:right; padding-right:2rem;'><h3>Nabila</h3><p><strong>NIM:</strong> 240123457<br><strong>Role:</strong> UI/UX Designer</p><p style='color:#6bb6ff; font-style:italic;'>Beauty in every pixel</p></div>", unsafe_allow_html=True)
    with n2:
        try: st.image("assets/nabila.jpg", width="stretch")
        except: st.image("https://via.placeholder.com/300/cbf0ff/000?text=Nabila", width="stretch")
    
    # Talytha
    t1, t2 = st.columns([1,2])
    with t1:
        try: st.image("assets/talytha.jpg", width="stretch")
        except: st.image("https://via.placeholder.com/300/f9e2ff/000?text=Talytha", width="stretch")
    with t2:
        st.markdown("<div style='padding-left:2rem;'><h3>Talytha</h3><p><strong>NIM:</strong> 240123458<br><strong>Role:</strong> Main Developer</p><p style='color:#6bb6ff; font-style:italic;'>Code is poetry</p></div>", unsafe_allow_html=True)
    
    # Zahra
    z1, z2 = st.columns([2,1])
    with z1:
        st.markdown("<div style='text-align:right; padding-right:2rem;'><h3>Zahra</h3><p><strong>NIM:</strong> 240123459<br><strong>Role:</strong> Researcher & Testing</p><p style='color:#6bb6ff; font-style:italic;'>Exploring the unknown</p></div>", unsafe_allow_html=True)
    with z2:
        try: st.image("assets/zahra.jpg", width="stretch")
        except: st.image("https://via.placeholder.com/300/d8f3ff/000?text=Zahra", width="stretch")

# ================== FOOTER ==================
st.markdown(f"""
<hr>
<p style='text-align:center; font-size:2.6rem; background: linear-gradient(90deg, #ff6bcb, #6bb6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
    {t['footer']}
</p>
""", unsafe_allow_html=True)

# ================== KONVOLUSI ==================
def convolution(img, kernel):
    if len(img.shape) == 3:
        h, w, c = img.shape
        kh, kw = kernel.shape
        pad = kh//2
        padded = np.pad(img, ((pad,pad),(pad,pad),(0,0)), mode='edge')
        out = np.zeros_like(img)
        for i in range(h):
            for j in range(w):
                for k in range(c):
                    out[i,j,k] = np.sum(padded[i:i+kh, j:j+kw, k] * kernel)
        return out
    return img