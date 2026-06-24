import joblib

print(joblib.load('X_train_processed.pkl'))
print(joblib.load('X_test_processed.pkl'))
print(joblib.load('preprocessing_pipeline.pkl'))