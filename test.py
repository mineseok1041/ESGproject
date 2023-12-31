# 학습된 모델 테스트
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import keras
import pickle

DATA_PATH = 'D:\9\Workspace\VScode\AI_Friend_School\ESGproject\CLEAN_DATA/' #TODO 데이터 경로 설정
INPUT_TEST_DATA = 'nsmc_test_input.npy'
LABEL_TEST_DATA = 'nsmc_test_label.npy'
SAVE_FILE_NM = 'weights.h5'

test_input = np.load(open(DATA_PATH+INPUT_TEST_DATA,'rb'))
test_input = pad_sequences(test_input,maxlen=test_input.shape[1])
test_label_data = np.load(open(DATA_PATH + LABEL_TEST_DATA, 'rb'))

model = keras.models.load_model('D:\9\Workspace\VScode\AI_Friend_School\ESGproject\my_models/') #TODO 데이터 경로 설정
model.load_weights('D:\9\Workspace\VScode\AI_Friend_School\ESGproject\DATA_OUT\cnn_classifier_kr/weights.h5') #TODO 데이터 경로 설정
model.evaluate(test_input, test_label_data)