# import os

# url = os.getenv("MONGODB_URL")
# print(url)
from USvisa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()