import os
import streamlit as st
import psycopg2

st.set_page_config(page_title="GestMarket SaaS", page_icon="🛒", layout="wide")
st.title("GestMarket SaaS — Online ✅")

db_url = os.getenv("DATABASE_URL", "")
ok, err = False, None

if db_url:
    try:
        # Assicura SSL su Render
        if "sslmode" not in db_url:
            db_url += ("&" if "?" in db_url else "?") + "sslmode=require"
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS healthcheck (id serial PRIMARY KEY, note text)")
        conn.commit()
        cur.close(); conn.close()
        ok = True
    except Exception as e:
        err = str(e)

st.subheader("Stato Database")
if ok:
    st.success("Connessione OK e tabella di prova pronta.")
else:
    st.error("Connessione NON riuscita.")
    if err:
        st.code(err)

st.caption("Versione minima. Poi aggiungiamo login, piani e moduli fornitori/marketplace.")
