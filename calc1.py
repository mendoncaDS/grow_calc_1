import streamlit as st

def lightFromPPF(ppf):
    if ppf<=50:
        return ["Área pequena demais",0]
    elif ppf<= 130:
        return ["65W LM281B+PRO",130]
    elif ppf<= 160:
        return ["65W LM301H",160]
    elif ppf<= 230:
        return ["TS100W Mars Hydro",230]
    elif ppf<= 294:
        return ["120W LM301H",294]
    elif ppf<= 352.5:
        return ["150W LM301B",352.5]
    elif ppf<= 564:
        return ["240W LM301B",564]
    elif ppf<= 588:
        return ["240W LM301H",588]
    elif ppf<= 784:
        return ["LED BAR 320W LM301H",784]
    else:
        return ["Para mensurar espaços maiores, fale conosco no whatsapp",1176]
        
#st.set_page_config(layout="wide")

st.title("Calculadora Grow")
st.write("by donsa")
st.markdown("""---""")

st.header("Input")

minSideLen = 5.
maxSideLen = 200.

comprimentoLateral = st.slider("Comprimento lateral (cm)",minSideLen,maxSideLen,minSideLen+(maxSideLen-minSideLen)/2)
areaQuadrada = comprimentoLateral*comprimentoLateral

vegaPPF = round(areaQuadrada*300/10000,ndigits=2)
[vegaPainel,vegaPainelPPF] = lightFromPPF(vegaPPF)

floraPPF = round(areaQuadrada*700/10000,ndigits=2)
[floraPainel,floraPainelPPF] = lightFromPPF(floraPPF)

st.markdown("""---""")
st.header("Resultados")
st.subheader("Área considerada:")
st.write(f"{round((areaQuadrada)/10000,ndigits=4)} m²")

col1, col2 = st.columns(2)

col1.subheader("PPF ótimo para vega:")

col1.write(f"{vegaPPF} μmol/s")

col1.subheader("Painel recomendado para vega:")

col1.write(f"{vegaPainel}")

col1.subheader("PPF do painel recomendado para vega:")

col1.write(f"{vegaPainelPPF} μmol/s")

col2.subheader("PPF ótimo para flora:")

col2.write(f"{floraPPF} μmol/s")

col2.subheader("Painel recomendado para flora:")

col2.write(f"{floraPainel}")

col2.subheader("PPF do painel recomendado para flora:")

col2.write(f"{floraPainelPPF} μmol/s")



