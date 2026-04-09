import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import time

# --- FUNÇÕES -----------------------------------------------------------------------------------------
# Cria N pontos num espaço 1000 X 1000
def cria_pontos(N):
    np.random.seed(42) # Evita que pontos diferentes sejam gerados para um mesmo N em Runs diferentes

    x = np.random.randint(0,1000,N)
    y = np.random.randint(0,1000,N,)

    pontos = list(zip(x,y))

    return pontos 

# Função criada para aplicação do K_Means e plotagem (Gerado por IA)
def K_Means(df, N_clusters, max_iter=15, random_state=42):
    np.random.seed(random_state)

    X = df[['X', 'Y']].values

    # Inicializa centróides aleatórios
    indices = np.random.choice(len(X), N_clusters, replace=False)
    centroids = X[indices]

    placeholder = st.empty()  # espaço para atualizar gráfico

    for epoch in range(max_iter):
        # --- Etapa 1: atribuir clusters ---
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        # --- Plot ---
        fig, ax = plt.subplots()

        for k in range(N_clusters):
            cluster_points = X[labels == k]
            ax.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {k}")

        # Plot centróides
        ax.scatter(centroids[:, 0], centroids[:, 1],
                   c='black', marker='X', s=200, label='Centroides')

        ax.set_title(f"Epoch {epoch + 1}")
        ax.legend()

        placeholder.pyplot(fig)  # atualiza o gráfico

        # --- Etapa 2: atualizar centróides ---
        new_centroids = np.array([
            X[labels == k].mean(axis=0) if len(X[labels == k]) > 0 else centroids[k]
            for k in range(N_clusters)
        ])

        # Critério de parada
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

        # Pequena pausa pra visualizar melhor (opcional)
        import time
        time.sleep(0.5)


def clustering(algortimo, df, N_clusters):
    match algortimo:
        case "K-Means":
            K_Means(df, N_clusters)
        # case "DBSCAN":
        #     DBSCAN(df)

# --- APLICAÇÃO -----------------------------------------------------------------------------------------
st.markdown("# Visualização de algoritmos de agrupamento com Streamlit")
st.markdown("## Visualização dos dados")

# st.sidebar.camera_input("Esse é um exemplo de conexão com a câmera.")
st.sidebar.title("Visualização de algoritmos de agrupamento com Streamlit")

menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Configurações"]
)

# Definição do número de Pontos
N = st.slider("Número de pontos: ", min_value= 0, max_value=500, value=250)
# N = st.number_input("Número de pontos: ", min_value=0, max_value=500, value=250)
pontos = cria_pontos(N)

#Criação do Dataframe de pontos
df = pd.DataFrame(pontos,
                  columns=['X', 'Y'])

if st.checkbox('Show dataframe'):
    st.write("Dataframe dos pontos:")
    st.dataframe(df.style.highlight_max(axis=0)) # Destaca o valor mais alto em cada coluna

# Plotagem do mapa 2D usando figura do Matplotlib
st.markdown("### Mapa 2D dos indivíduos - Matplotlib")
fig, ax = plt.subplots()
ax.scatter(df['X'], df['Y'], c="green", alpha=0.7)
ax.set_xlabel("X")
ax.set_ylabel("Y")
# ax.set_title("Mapa 2D de pontos aleatórios")

st.pyplot(fig)

# Plotagem do mapa 2D usando mapa interativo no Streamlit
st.markdown("### Mapa 2D dos indivíduos - Streamlit")
st.scatter_chart(df, 
                 x="X", y="Y",
                 color=["green"])

st.markdown("### Algoritmos de Agrupamento:")
left_column, right_column = st.columns(2)
N_clusters = left_column.number_input('Número de clusters: ', min_value=1, max_value=5, value=2)

with right_column: 
    chosen = st.radio(
        'Escolha o Algoritmo a ser aplicado:',
        ("K-Means", "DBSCAN"))
    
if st.button('Clique para iniciar agrupamento'):
        on_click=clustering(chosen, df, N_clusters)



