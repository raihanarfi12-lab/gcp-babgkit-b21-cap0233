import pickle
from google.cloud import storage
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import LSTM
from google.cloud import bigquery

def hello_rtdb(event,context):
     if "status" in event["delta"].keys() and "name" in event["delta"].keys():
          data = event["delta"]["status"]
          user = event["delta"]["name"]
          storage_client = storage.Client()
          bucket = storage_client.get_bucket('ml-bangkit-bucket')
          blob_weight1 = bucket.blob('variables.index')
          blob_weight2 = bucket.blob('variables.data-00000-of-00001')
          blob_tfidf = bucket.blob('tokenizer.pickle')
          blob_weight1.download_to_filename('/tmp/variables.index')
          blob_weight2.download_to_filename('/tmp/variables.data-00000-of-00001')
          embedding_dim = 128
          maxlen = 150
          vocab_size = 20000
          model = tf.keras.Sequential([
          tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=maxlen),
          tf.keras.layers.Bidirectional(LSTM(55, return_sequences = True, recurrent_dropout = 0.15)),
          tf.keras.layers.GlobalMaxPool1D(),
          tf.keras.layers.Dropout(0.1),
          tf.keras.layers.Dense(55, activation = 'relu'),
          tf.keras.layers.Dropout(0.1),
          tf.keras.layers.Dense(1, activation = 'sigmoid')
          ])
          model.load_weights("/tmp/variables")
          blob_tfidf.download_to_filename("/tmp/tokenizer.pickle")
          tokenizer= pickle.load(open('/tmp/tokenizer.pickle','rb'))
          print(data)
          text_list = []
          text_list.append(data)
          sequenced_text = tokenizer.texts_to_sequences(text_list)[0]
          sequenced_text = pad_sequences([sequenced_text], padding='post', maxlen=maxlen)
          prediction = model.predict(sequenced_text)
          print(prediction[0])
          if prediction[0][0]<0.5:
               category = "Non Toxic status"
          else:
               category = "Toxic status,need to make status look good"
               bq = bigquery.Client()
               table_ref = bq.dataset('jobstify').table('toxic_status')
               table = bq.get_table(table_ref)
               rows = [(user,data)]
               bq.insert_rows(table,rows)
          print(f"{user} status: {data},category: {category}")

     else:
          pass