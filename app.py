#%%
# from flask import Flask, request, jsonify
from src.AI_ML.logger import logging
from src.AI_ML.exception import CustomException
import sys
from src.AI_ML.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.AI_ML.components.data_transformation import DataTransformation,DataTransformationConfig
from src.AI_ML.components.model_trainer import ModelTrainer,ModelTrainerConfig

#%%
if __name__ == '__main__':
    logging.info("Execution has started")

    try:
        # Data Ingestion Process
        ## data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

        # Data Transformation Process
        data_transformation = DataTransformation()
        train_arr,test_arr,_ = data_transformation.initiate_data_transformation(
                                                                        train_path= train_data_path,
                                                                        test_path=test_data_path)
        
        # Training of our Model
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_train_model(train_arr,test_arr))

    except Exception as e:
        logging.info(f"Custom Exception raised : {CustomException(e, sys)}")
        raise CustomException(e, sys)
    # app.run(debug=True)

