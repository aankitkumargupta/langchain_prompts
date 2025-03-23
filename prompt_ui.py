from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables
load_dotenv()

# Define the Hugging Face model
llm = HuggingFaceEndpoint(repo_id="Qwen/QwQ-32B", task="text-generation")

# Create the chat model
model = ChatHuggingFace(llm=llm)

st.header("Paper Summarizer")

# List of breakthrough papers
papers = st.selectbox(
    "Please select your paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "ResNet: Deep Residual Learning",
        "U-Net: Convolutional Networks for Biomedical Image Segmentation",
        "AlexNet: ImageNet Classification with Deep CNNs",
        "VGGNet: Deep Convolutional Networks for Image Recognition",
        "YOLO: Real-Time Object Detection",
        "Diffusion Models: Denoising Diffusion Probabilistic Models",
        "NeRF: Neural Radiance Fields for 3D Synthesis",
    ],
)

# Explanation styles
styles = st.selectbox(
    "Please select the explanation Style",
    ["Technical", "Non-Technical", "Beginner-friendly"],
)

# Explanation length options
length = st.selectbox("Please Select length", ["50 words", "100 words", "200 words"])


template = load_prompt("template.json")

# Fill the placeholders
prompt = template.invoke({"paper": papers, "style": styles, "length": length})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
