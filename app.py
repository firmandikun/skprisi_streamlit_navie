# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Komentar': [
        'Prabowo sangat baik dalam debat',
        'Anies membuat kebijakan yang kontroversial',
        'Prabowo membangkitkan semangat rakyat',
        'Anies tidak efektif dalam penanganan banjir',
        'Prabowo adalah pemimpin yang kuat',
        'Anies tidak mendukung pengembangan transportasi publik',
        'Prabowo memiliki kebijakan yang kontroversial',
        'Anies berhasil mengatasi permasalahan pendidikan',
        'Prabowo dan Anies sama-sama mendukung pembangunan infrastruktur'
    ],
    'Sentimen': ['Positif', 'Negatif', 'Positif', 'Negatif', 'Positif', 'Negatif', 'Negatif', 'Positif', 'Netral'],
    'Calon': ['Prabowo', 'Anies', 'Prabowo', 'Anies', 'Prabowo', 'Anies', 'Prabowo', 'Anies', 'Prabowo & Anies']
}



df = pd.DataFrame(data)

def crawling_data(keyword, data_count):
    crawled_data = [f"Data {i + 1} for {keyword}" for i in range(data_count)]
    return crawled_data

def crawling():
    st.subheader("Crawling Data")
    keyword = st.text_input("Masukkan Kata Kunci", "")

    data_count = st.number_input("Masukkan Jumlah Data", min_value=1, max_value=100, step=1, value=5)

    st.button("Crawl Data")

def preprocessing():
    st.subheader("Analisis Kalimat")

    sentence = st.text_area("Masukkan Kalimat:", "")
    st.button("Analisis")

def display_data():
    st.subheader("Praproses")
    st.button('Praproses Data', type='primary')

    file_path = "assets/tweet.csv"
    df = pd.read_csv(file_path)
    st.dataframe(df, width=1000)

def analysis():
    st.subheader("Visualisasi")

    # Create separate dataframes for Prabowo and Anies
    df_prabowo = df[df['Calon'] == 'Prabowo']
    df_anies = df[df['Calon'] == 'Anies']
    df_both = df[df['Calon'] == 'Prabowo & Anies']

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5))

    sns.countplot(x='Sentimen', data=df_prabowo, palette='viridis', ax=ax1)
    ax1.set_title('Analisis Sentimen: Prabowo')
    ax1.set_xlabel('Sentimen')
    ax1.set_ylabel('Jumlah')

    sns.countplot(x='Sentimen', data=df_anies, palette='viridis', ax=ax2)
    ax2.set_title('Analisis Sentimen: Anies')
    ax2.set_xlabel('Sentimen')
    ax2.set_ylabel('Jumlah')

    sns.countplot(x='Sentimen', data=df_both, palette='viridis', ax=ax3)
    ax3.set_title('Analisis Sentimen: Prabowo & Anies')
    ax3.set_xlabel('Sentimen')
    ax3.set_ylabel('Jumlah')

    plt.tight_layout()

    # Display the plots
    st.pyplot(fig)


def home():
    st.markdown(
        """
        <style>
            .centered {
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='centered'>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Selamat Datang Di Web Analisis Sentimen Lihut</h1>", unsafe_allow_html=True)
    st.write("Calon Potensial Presiden 2024")

    image_path = "assets/naviebayes.webp"
    st.image(image_path, caption="", use_column_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

def main():

    home_button = st.sidebar.button("Home")
    crawling_button = st.sidebar.button("Crawling Data")
    display_button = st.sidebar.button("Praproses")
    preprocessing_button = st.sidebar.button("Analisis Kalimat")
    analysis_button = st.sidebar.button("Visualisasi")

    # Display content based on button click
    if home_button:
        home()
    elif crawling_button:
        crawling()
    elif preprocessing_button:
        preprocessing()
    elif analysis_button:
        analysis()
    elif display_button:
        display_data()
    else:
        # If no button is clicked, show the content for the "Home" page
        home()

if __name__ == "__main__":
    main()
