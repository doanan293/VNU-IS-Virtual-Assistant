import pandas as pd
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
import json

# from huggingface_hub import login
import torch
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.info("Start embedding docs")
load_dotenv()

# ----------------Get the Hugging Face access token from environment variables--------------------------
# hf_token = os.getenv("PROJECTCB1_HUGGINGFACE_ACCESS_TOKEN")

# Log in to Hugging Face using the access token
# if hf_token:
#     login(token=hf_token)
# else:
#     print(
#         "Access token not found. Please set the HUGGINGFACE_ACCESS_TOKEN in your .env file."
#     )

device = "cuda" if torch.cuda.is_available() else "cpu"
logging.info(f"Using {device}")
# device = "cpu"
model_path = os.getenv("PROJECTCB1_EMBEDDING_MODEL")
embedding_model = SentenceTransformer(
    model_name_or_path=model_path,
    device=device,
    model_kwargs={"torch_dtype": "bfloat16"},
    trust_remote_code=True,
)
file_path = os.getenv("PROJECTCB1_DATA_DB")
df = pd.read_csv(file_path, usecols=["Relevant docs"], dtype={"Relevant docs": str})
df.drop_duplicates(keep="first", ignore_index=True, inplace=True)
question_list = df["Relevant docs"].to_list()

if device == "cuda":
    batch_size = 32
else:
    batch_size = 4

logging.info("Start encoding")
start_time = time.time()
embeddings = embedding_model.encode(
    question_list,
    batch_size=batch_size,
    show_progress_bar=True,
    convert_to_tensor=False,
)
end_time = time.time()
load_time = end_time - start_time
print(load_time)

df["embedding"] = [json.dumps(embedding.tolist()) for embedding in embeddings]
logging.info("Start saving to file")
embeddings_df_save_path = os.getenv("PROJECTCB1_DATA_DB")
df.to_csv(embeddings_df_save_path, index=False)
logging.info("Saved_to file")
