# El Sabio del Cine: recomendaciones de películas que no puedes ignorar

## 📝 Project Objective
In the streaming era, there is a vast amount of content available, making it challenging to find movies that match individual preferences. Recommendation systems offer a personalized experience by suggesting titles that are likely to interest viewers, helping to discover films that might otherwise go unnoticed.

## 📊 Dataset Description
### Data Sources
The dataset is sourced from [Kaggle](https://www.kaggle.com/) and includes nearly 5,000 movies. 

### Information Included:
- Movie ID
- Title
- Genres
- Summary
- Cast
- Production Crew
- Keywords

## Data Preprocessing

### Cleaning

### Combination of Information into Tags:

### Tokenization and Normalization:

## 🤖 Model Building 

### Model 1 - Content-Based Recommendation Model
This model recommends movies based on shared characteristics (like genre, actors, and synopsis) using text processing techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) to calculate similarity between movies.

### Model 2 - BERT Model
Utilizes the BERT model, a natural language processing neural network, to understand the context and meaning of movie descriptions, offering more accurate recommendations based on semantic content.

### Similarity Matrix Creation
Both the Content-Based Model and BERT Model can provide effective recommendations. However, the Content-Based Model has shown some shortcomings during testing.

## Retrieving Movie Posters with TMDb API in Streamlit
To enhance the visual appeal of the Streamlit app, movie posters of similar films are added using the TMDb API. 

## Project Structure
The project is organized as follows:

- **data/**: Contains the original dataset and a CSV file with embeddings for Streamlit to enhance movie recommendations.
- **notebook/FINAL_PROJECT.ipynb**: Jupyter notebook showcasing the entire workflow, from data exploration to model analysis and evaluation.
- **streamlit.py**: Streamlit application that allows users to input data and receive movie recommendations based on the trained models.
- **README.md**: File containing the project description and instructions on how to run it.

## ⚙️ Requirements
To run this project, ensure you have the following dependencies installed:

- ast: For abstract syntax trees.
- os: For interacting with the operating system.
- numpy: For numerical operations.
- pandas: For data manipulation and analysis.
- pickle: For serializing and de-serializing Python objects.
- torch: For PyTorch, a deep learning framework.
- nltk: For natural language processing tasks.
- sklearn: For machine learning algorithms and metrics.
- transformers: For using BERT and other transformer models.
- streamlit: For creating interactive web applications.

## 🌐 Streamlit

![image](https://github.com/user-attachments/assets/23c480be-bf78-407a-982e-fc89d8fa9535)
![image](https://github.com/user-attachments/assets/62d9a850-29ef-4f6f-8b10-0906c1f48f4c)


## 🖥️ Presentation
You can view the presentation that summarizes the project, its findings, and key takeaways at the following link to the presentation.


