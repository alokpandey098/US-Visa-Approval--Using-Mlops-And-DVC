from USvisa.pipline.training_pipeline import TrainPipeline

# Instantiate the pipeline class and run it
obj = TrainPipeline()
obj.run_pipeline()

# import os
# url = os.getenv('MONGODB_URL')
# print(url)