def load_css():
    return """
    <style>

    /* Hide Streamlit default menu & footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main page */
    .main {
        padding-top: 1rem;
        background-color: #F8FAFC;
    }

    /* Hero Card */
    .hero-card{
        background: linear-gradient(135deg,#2563EB,#7C3AED);
        color:white;
        padding:30px;
        border-radius:20px;
        box-shadow:0px 10px 25px rgba(0,0,0,0.15);
        margin-bottom:25px;
    }

    .hero-title{
        font-size:40px;
        font-weight:700;
    }

    .hero-subtitle{
        font-size:18px;
        margin-top:10px;
        opacity:0.95;
    }

    /* Section Cards */
    .info-card{
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0 4px 12px rgba(0,0,0,.08);
        margin-top:15px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background:#EEF2FF;
    }

    /* Buttons */
    div.stButton > button{
        width:100%;
        border-radius:10px;
        height:45px;
        font-weight:bold;
    }

    /* Chat Input */
    div[data-testid="stChatInput"]{
        position:fixed;
        bottom:20px;
        width:60%;
    }

    </style>
    """