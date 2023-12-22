# Importing necessary libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the DataFrame from the CSV file
file_path = 'category_product_search_corpus_EF.csv'
df = pd.read_csv(file_path)

# Set the title
st.title('Case técnico - Dadosfera')

# Sidebar page selection using radio buttons
selected_page = st.sidebar.radio('Select Page', ['Analysis by category', 'Analysis by similarity'])

if selected_page == 'Analysis by category':
    # Displaying the DataFrame for 'Analysis by category'
    st.subheader('Item 5 - Eduardo Ferreira ')
    st.subheader('DataFrame Preview')
    st.dataframe(df)

    # Checkbox for selecting all categories
    select_all = st.sidebar.checkbox('Select All Categories', value=True)

    # Sidebar filter for category selection
    if select_all:
        selected_categories = st.sidebar.multiselect('Select Categories', df['category'].unique(), df['category'].unique())
    else:
        selected_categories = st.sidebar.multiselect('Select Categories', df['category'].unique())

    # Filter the DataFrame based on selected categories
    filtered_df = df[df['category'].isin(selected_categories)]

    # Vertical bar chart of product counts by category
    st.subheader('Product Count by Category')
    category_counts = filtered_df['category'].value_counts()
    st.bar_chart(category_counts)

elif selected_page == 'Analysis by similarity':
    # Analysis: Visualizing Word Vectors with t-SNE (by category)
    st.subheader('Item 5 - Eduardo Ferreira')
    st.subheader('Analysis by similarity')

    # Tokenize and vectorize product names using TF-IDF, grouped by category
    vectorizer = TfidfVectorizer()
    category_names = df['category'].dropna().values.astype('U')
    X = vectorizer.fit_transform(category_names)

    # Reduce dimensionality using t-SNE
    tsne = TSNE(n_components=2, random_state=42)
    X_tsne = tsne.fit_transform(X.toarray())

    # Create a DataFrame for visualization
    tsne_df = pd.DataFrame(X_tsne, columns=['Dimension 1', 'Dimension 2'])
    tsne_df['Category'] = df['category'].dropna().values.astype('U')

    # Scatter plot for t-SNE visualization by category
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(x='Dimension 1', y='Dimension 2', data=tsne_df, hue='Category', palette='viridis', ax=ax)
    plt.title('t-SNE Visualization of Word Vectors by Category')

    # Display the Matplotlib figure using st.pyplot()
    st.pyplot(fig)

# Other analyses and visualizations can be added as needed

# Run the application using the command in the terminal: streamlit run app.py